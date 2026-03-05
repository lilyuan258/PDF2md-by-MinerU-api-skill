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

1. You need a MinerU (TextIn) API Token. **Note: The Token is used to verify your account identity when calling the MinerU API. It is valid for 90 days, after which it must be recreated as renewal is not supported.**
2. Python 3.7+ installed.

## Installation

1. Clone this project:
   ```bash
   git clone https://github.com/lilyuan258/PDF2md-by-MinerU-api-skill.git
   cd PDF2md-by-MinerU-api-skill
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Environment Variable:
   Set your API Token as the environment variable `MINERU_API_TOKEN`. **This must be configured as a persistent system/user environment variable** so that the AI Agent can read it from any working directory, rather than needing to set it every time you open a new terminal.

   - **Windows**: Search for "Environment Variables" in the Start menu -> Edit the system environment variables -> Environment Variables -> Add a new User variable named `MINERU_API_TOKEN` with your token.
   - **Linux/macOS**: Add the following line to your shell profile file (e.g., `~/.bashrc`, `~/.zshrc`):
     ```bash
     export MINERU_API_TOKEN="your_token_here"
     ```
     Then, run `source ~/.bashrc` or `source ~/.zshrc` to apply the changes.

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