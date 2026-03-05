# mineru-pdf-reader

[English](#english) | [中文](#中文)

---

<a id="english"></a>
## 🇺🇸 English

A Skill designed for AI Agents (like Gemini CLI) to automatically call the official API of [MinerU](https://github.com/opendatalab/MinerU) (TextIn) when reading user-uploaded PDF documents. It converts PDFs into machine-friendly Markdown files.

Through this workflow, the context token consumption of Large Language Models (LLMs) is significantly reduced. More importantly, it enables the machine to **accurately read charts, tables, and complex layouts**, preventing the massive loss of information common in traditional text-only extraction tools.

### Features

- 🚀 Automatically convert PDF to Markdown
- 🖼️ Extract images from PDF and save them locally
- 📉 Retain tables and complex layout information
- 🧠 Drastically reduce Token overhead when LLMs process PDFs
- 🤖 Seamless integration into Agent workflows

### Prerequisites

1. You need a MinerU (TextIn) API Token.
2. Python 3.7+ installed.

### Installation

1. Clone this project:
   ```bash
   git clone https://github.com/your-username/mineru-pdf-reader.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Environment Variable:
   Set your API Token as the environment variable `MINERU_API_TOKEN`.
   
   - **Windows (PowerShell)**:
     ```powershell
     $env:MINERU_API_TOKEN="your_token_here"
     ```
   - **Linux/macOS**:
     ```bash
     export MINERU_API_TOKEN="your_token_here"
     ```

### Using as an Agent Skill

Link or place this folder in your Agent's (e.g., Gemini CLI) `skills` directory. When a user requests to read a PDF, the Agent will automatically invoke the instructions within this skill.

> **Note**: The exact workflow detailing how the Python script is called to convert and read files is defined in `SKILL.md`.

### Running Manually

You can also use the script standalone:

```bash
python scripts/convert_pdf.py <Input_PDF_Path> <Output_Directory_Name>
```

Example:
```bash
python scripts/convert_pdf.py ./sample.pdf ./sample_md_output
```

### License

MIT License.

---

<a id="中文"></a>
## 🇨🇳 中文

这是一个为 Gemini CLI 等 AI Agent 设计的 Skill，用于在阅读用户上传的 PDF 文档时，自动调用 [MinerU](https://github.com/opendatalab/MinerU) (TextIn) 官方 API 接口，将 PDF 转换为对机器更友好的 Markdown 文件。

通过这个过程，可以极大地减少大模型的上下文 Token 消耗。更重要的是，它使得机器能够**准确阅读图表和复杂排版结构**，避免了传统 PDF 解析工具直接提取纯文本导致的关键信息（图片、表格）丢失问题。

### 特性

- 🚀 自动将 PDF 转换为 Markdown
- 🖼️ 自动提取 PDF 中的图片并保存在本地
- 📉 保留表格和复杂排版信息
- 🧠 极大地减少大型语言模型 (LLM) 处理 PDF 时的 Token 开销
- 🤖 无缝集成到 Agent 工作流中

### 前置条件

1. 你需要拥有一个 MinerU (TextIn) 的 API Token。
2. 安装 Python 3.7+。

### 安装

1. 克隆本项目：
   ```bash
   git clone https://github.com/your-username/mineru-pdf-reader.git
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

### 作为 Agent Skill 使用

将本文件夹链接或放置在您的 Gemini CLI skills 目录中。当用户请求阅读 PDF 时，Agent 将自动调用本 skill 里的指令。

> **注意**: 在 `SKILL.md` 中定义了如何调用 Python 脚本来完成文件转换与读取的详细工作流。

### 手动运行脚本

您也可以独立使用该脚本：

```bash
python scripts/convert_pdf.py <输入的PDF路径> <输出的文件夹名称>
```

示例：
```bash
python scripts/convert_pdf.py ./sample.pdf ./sample_md_output
```

### 许可证

MIT License.