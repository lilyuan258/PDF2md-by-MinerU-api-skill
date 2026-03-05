# mineru-pdf-reader

[**🇺🇸 English**](README.md) | [**🇨🇳 中文**](README_zh.md)

---

这是一个为 Claude Code、Antigravity、Cursor、Gemini CLI 等 AI Agent 设计的 Skill，用于在阅读用户上传的 PDF 文档时，自动调用 [MinerU](https://github.com/opendatalab/MinerU) (TextIn) 官方 API 接口，将 PDF 转换为对机器更友好的 Markdown 文件。

通过这个过程，可以极大地减少大模型的上下文 Token 消耗。更重要的是，它使得机器能够**准确阅读图表和复杂排版结构**，避免了传统 PDF 解析工具直接提取纯文本导致的关键信息（图片、表格）丢失问题。

## 特性

- 🚀 自动将 PDF 转换为 Markdown
- 🖼️ 自动提取 PDF 中的图片并保存在本地
- 📉 保留表格和复杂排版信息
- 🧠 极大地减少大型语言模型 (LLM) 处理 PDF 时的 Token 开销
- 🤖 无缝集成到 Agent 工作流中

## 前置条件

1. 你需要拥有一个 MinerU (TextIn) 的 API Token。
2. 安装 Python 3.7+。

## 安装

1. 克隆本项目：

   ```bash
   git clone https://github.com/lilyuan258/PDF2md-by-MinerU-api-skill.git
   ```
2. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```
3. 配置环境变量：
   将你的 API Token 设置为环境变量 `MINERU_API_TOKEN`。

   - **Windows (PowerShell)**:
     ```powershell
     $env:MINERU_API_TOKEN="your_token_here"
     ```
   - **Linux/macOS**:
     ```bash
     export MINERU_API_TOKEN="your_token_here"
     ```

## 作为 Agent Skill 使用

将本文件夹链接或放置在您的 Gemini CLI skills 目录中。当用户请求阅读 PDF 时，Agent 将自动调用本 skill 里的指令。

> **注意**: 在 `SKILL.md` 中定义了如何调用 Python 脚本来完成文件转换与读取的详细工作流。

## 手动运行脚本

您也可以独立使用该脚本：

```bash
python scripts/convert_pdf.py <输入的PDF路径> <输出的文件夹名称>
```

示例：

```bash
python scripts/convert_pdf.py ./sample.pdf ./sample_md_output
```

## 许可证

MIT License.
