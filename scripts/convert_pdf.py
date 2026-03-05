import os
import sys
import json
import time
import zipfile
import io
import shutil
from pathlib import Path
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def download_file_with_retry(url, dest_path, retries=5):
    import urllib.request
    import ssl
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    # 修复因为本地代理导致 CDN 域名无法下载的问题
    url = url.replace("cdn-mineru.openxlab.org.cn", "mineru.oss-cn-shanghai.aliyuncs.com")
    
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=ctx, timeout=30) as response:
                with open(dest_path, 'wb') as out_file:
                    out_file.write(response.read())
            return True
        except Exception as e:
            print(f"下载重试 {i+1}/{retries} 失败: {e}")
            time.sleep(2)
    return False

def convert_pdf_to_markdown(pdf_path, output_dir):
    token = os.environ.get("MINERU_API_TOKEN")
    if not token:
        print("错误: 环境变量 MINERU_API_TOKEN 未设置。请在系统中配置您的 API Token。")
        return False
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    print(f"1. 正在获取上传链接: {pdf_path} ...")
    try:
        res = requests.post(
            "https://mineru.net/api/v4/file-urls/batch",
            json={"files": [{"name": Path(pdf_path).name, "data_id": "pdf_task"}], "model_version": "vlm"},
            headers=headers,
            verify=False
        )
        res_data = res.json()
        if 'data' not in res_data:
            print("获取链接失败: ", res_data)
            return False
            
        batch_id = res_data['data']['batch_id']
        upload_url = res_data['data']['file_urls'][0]
    except Exception as e:
        print(f"获取上传链接失败: {e}")
        return False
        
    print("2. 正在上传 PDF 到云端 ...")
    try:
        with open(pdf_path, 'rb') as f:
            upload_res = requests.put(upload_url, data=f, verify=False)
            
        if upload_res.status_code not in [200, 201]:
            print(f"上传失败，状态码: {upload_res.status_code}, 内容: {upload_res.text}")
            return False
    except Exception as e:
        print(f"上传文件失败: {e}")
        return False
        
    print("3. 正在云端进行解析 (这可能需要几分钟，请耐心等待) ...")
    try:
        while True:
            res = requests.get(f"https://mineru.net/api/v4/extract-results/batch/{batch_id}", headers=headers, verify=False)
            res_data = res.json()
            
            if 'data' not in res_data or not res_data['data'].get('extract_result'):
                print("查询状态异常: ", res_data)
                return False
                
            state = res_data['data']['extract_result'][0]['state']
            
            if state == 'done':
                full_zip_url = res_data['data']['extract_result'][0].get('full_zip_url')
                if not full_zip_url:
                    print("解析完成，但未找到下载链接。")
                    return False
                
                print("4. 解析完成，正在下载并提取结果 ...")
                
                out_path = Path(output_dir)
                out_path.mkdir(parents=True, exist_ok=True)
                
                zip_path = out_path / "temp_result.zip"
                
                if not download_file_with_retry(full_zip_url, zip_path):
                    print("下载结果失败。")
                    return False
                
                with zipfile.ZipFile(zip_path) as z:
                    md_filename = next((name for name in z.namelist() if name.endswith('.md')), None)
                    if md_filename:
                        md_content = z.read(md_filename).decode('utf-8')
                        img_dir = out_path / 'images'
                        img_dir.mkdir(parents=True, exist_ok=True)
                        
                        image_count = 0
                        for filename in z.namelist():
                            if filename.startswith('images/') or filename.startswith('auto/') or filename.endswith('.jpg') or filename.endswith('.png'):
                                file_data = z.read(filename)
                                base_name = Path(filename).name
                                if not base_name: continue
                                
                                with open(img_dir / base_name, 'wb') as img_f:
                                    img_f.write(file_data)
                                
                                md_content = md_content.replace(filename, f"images/{base_name}")
                                image_count += 1
                        
                        with open(out_path / 'document.md', 'w', encoding='utf-8') as f:
                            f.write(md_content)
                        
                        print(f"转换成功！Markdown 文件和 {image_count} 张图片已保存到目录：{output_dir}")
                
                os.remove(zip_path)
                return True
                
            elif state == 'failed':
                print("云端解析任务失败。")
                return False
            
            print(f"当前状态: {state}，等待 5 秒后重试...")
            time.sleep(5)
                
    except Exception as e:
        print(f"查询或下载结果时出错: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python convert_pdf.py <PDF文件路径> <输出文件夹路径>")
        sys.exit(1)
        
    pdf_path = sys.argv[1]
    output_dir = sys.argv[2]
    convert_pdf_to_markdown(pdf_path, output_dir)
