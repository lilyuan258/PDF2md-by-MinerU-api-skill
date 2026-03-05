---
name: mineru-pdf-reader
description: Use this skill whenever the user asks to read, parse, or process one or more PDF files (.pdf). It converts the PDFs into Markdown using the MinerU (TextIn) API to handle long contexts, text, images, and tables perfectly, and then reads the resulting Markdown to fulfill the user's request. It also supports processing multiple PDFs simultaneously by creating separate output folders.
---

# MinerU PDF Reader

This skill is designed to handle PDF files effectively by converting them into Markdown (with images) using the MinerU / TextIn API before answering user queries. 

**核心动机与优势 (Core Motivation & Advantage):** 
传统的 PDF 解析工具往往只能生硬地提取纯文本，这会导致文档中的图片、复杂的表格布局等关键信息大量丢失。而通过本工作流，AI Agent 可以**直接读取高质量的 Markdown 排版并结合本地保存的图片进行视觉分析**。这不仅避免了因上下文过长导致的崩溃，更使得机器能够像人类一样完整、准确地阅读文档里的图表和复杂结构。

## 工作流 (Workflow)

对于用户提供的每一个 PDF 文件，执行以下步骤：

1. **定位目标 PDF 文件**: 找到用户想要阅读或处理的 `.pdf` 文件路径（例如 `论文A.pdf`）。
2. **定位转换脚本**: 脚本 `convert_pdf.py` 位于本 Skill 目录下的 `scripts` 文件夹中（即与此 `SKILL.md` 同级的 `scripts/convert_pdf.py`）。在执行命令前，你必须先动态获取或拼接出该脚本在当前系统中的绝对路径。
3. **确定输出文件夹名称**: 根据 PDF 的文件名动态创建一个专属的文件夹名称。规则为：去掉 `.pdf` 后缀，加上 ` md文档`。例如：对于 `论文A.pdf`，输出文件夹名称应为 `论文A md文档`。对于多篇论文（如论文A和论文B），分别对应 `论文A md文档` 和 `论文B md文档`。
4. **转换 PDF**: 运行打包好的 Python 脚本，将 PDF 转换为 Markdown 文档及包含图片的文件夹。
   - 运行命令: `python <转换脚本的绝对路径> <PDF的路径> "<输出文件夹名称>"`
   - 例如：`python C:\path\to\skill\scripts\convert_pdf.py 论文A.pdf "论文A md文档"`
5. **主动读取相关图片**: 当你读取 `document.md` 时，如果文档内部存在图片链接（例如 `![img](images/xxx.jpg)`），**你必须主动调用文件读取工具（如 `read_file` 等你的视觉/多模态工具）去读取这些图片文件**。不能仅仅把它们当做纯文本链接忽略过去。
6. **完成用户需求**: 结合 Markdown 的排版结构以及你亲眼读取的图片、表格内容，回答用户的原始请求或进行综合分析。

## 重要指令 (Critical Instructions)

- **绝对不要直接使用普通工具读取 PDF 文件**。在执行任何读取操作前，必须先使用脚本进行转换。
- **强制视觉读取**：转换完成后，去读取 `document.md` 的同时，**必须解析其中的图片路径，并使用你的工具去读取这些图片**。不读取图片就无法实现本工作流“保留图表和复杂排版信息”的核心目的！
- 处理多个 PDF 时，请确保为每个 PDF 单独运行脚本，并指定各自独立的输出文件夹（基于其原文件名）。
- Python 脚本是独立运行的。它依赖 `requests` 和 `urllib3` 库，并且需要读取系统环境变量 `MINERU_API_TOKEN` 作为访问凭证。如果脚本执行提示缺失 token，请提醒用户配置该环境变量。
