# mineru-pdf-reader

[**🇨🇳 中文**](README_zh.md) | [**🇺🇸 English**](README.md)

---

A Skill designed for AI Agents (like Claude Code、Antigravity、Cursor、Gemini CLI) to automatically call the official API of [MinerU](https://github.com/opendatalab/MinerU) (TextIn) when reading user-uploaded PDF documents. It converts PDFs into machine-friendly Markdown files.

Through this workflow, the context token consumption of Large Language Models (LLMs) is significantly reduced. More importantly, it enables the machine to **accurately read charts, tables, and complex layouts**, preventing the massive loss of information common in traditional text-only extraction tools.

## Features

- 🚀 Automatically convert PDF to Markdown
- 🖼️ Extract images from PDF and save them locally
- 📉 Retain tables and complex layout information
- 🧠 Drastically reduce Token overhead when LLMs process PDFs
- 🤖 Seamless integration into Agent workflows

## Prerequisites

1. You need a MinerU (TextIn) API Token.
2. Python 3.7+ installed.

## Installation

1. Clone this project:
   ```bash
   git clone https://github.com/lilyuan258/PDF2md-by-MinerU-api-skill.git
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

## Using as an Agent Skill

Link or place this folder in your Agent's (e.g., Gemini CLI) `skills` directory. When a user requests to read a PDF, the Agent will automatically invoke the instructions within this skill.

> **Note**: The exact workflow detailing how the Python script is called to convert and read files is defined in `SKILL.md`.

## Running Manually

You can also use the script standalone:

```bash
python scripts/convert_pdf.py <Input_PDF_Path> <Output_Directory_Name>
```

Example:
```bash
python scripts/convert_pdf.py ./sample.pdf ./sample_md_output
```

## License

MIT License.