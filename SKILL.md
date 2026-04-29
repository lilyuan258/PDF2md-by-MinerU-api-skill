---
name: mineru-pdf-reader
description: “Use this skill whenever the user asks to read, parse, or process one or more PDF files (.pdf). It converts PDFs into Markdown using the MinerU (TextIn) API, preserving images, tables, and complex layouts, then reads the resulting Markdown and images to fulfill the user's request. Use when opening PDFs, extracting PDF content, analyzing documents, or batch-processing multiple PDF files into structured output.”
---

# MinerU PDF Reader

Convert PDF files to Markdown with images via the MinerU (TextIn) API, then read all outputs (text and images) to answer user queries.

## Workflow

For each PDF file the user provides:

1. **Locate the PDF**: Resolve the full path to the target `.pdf` file.
2. **Locate the conversion script**: The script is at `scripts/convert_pdf.py` relative to this SKILL.md. Resolve its absolute path before running.
3. **Determine output folder**: Strip the `.pdf` extension and append ` md文档`. Example: `论文A.pdf` → `论文A md文档`.
4. **Convert**: Run the script to produce Markdown and extracted images.
   ```bash
   python /home/user/.claude/skills/mineru-pdf-reader/scripts/convert_pdf.py report.pdf “report md文档”
   ```
   Expected output folder contents: `document.md`, `image_0.jpg`, `image_1.png`, ...
5. **Read ALL outputs (mandatory)**: After conversion, use `list_directory` on the output folder, then call `read_file` on **every** file — `document.md` and all `.jpg`/`.png` images. Reading only the Markdown without the images violates this workflow.
6. **Answer the user**: Combine the Markdown structure and image contents to fulfill the original request.

For multiple PDFs, run steps 1–6 independently for each file with its own output folder.

## Error Handling

- If the script exits with a missing-token error, prompt the user to set `MINERU_API_TOKEN` as a persistent environment variable.
- If the output folder is empty or missing `document.md` after conversion, report the script's stderr output to the user and do not attempt to read the PDF directly.

## Constraints

- Never read a `.pdf` file directly — always convert first via the script.
- The script requires the `MINERU_API_TOKEN` environment variable.
- Dependencies: `requests`, `urllib3` (see `requirements.txt`).
