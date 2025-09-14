# MDitDCLI - MarkItDown CLI Tool

A command-line tool that converts various file formats to Markdown using Microsoft's MarkItDown library.

## Development Plan

### Overview
This CLI app takes an input file as an argument and outputs a Markdown file with the same name and .md extension.

### Development Steps

1. **Add MarkItDown dependency to pyproject.toml**
   - Status: Completed
   - Description: Added the `markitdown` package to project dependencies in pyproject.toml

2. **Implement CLI argument parsing in main.py**
   - Status: Completed
   - Description: Implemented argparse in main.py to accept input file path as command-line argument, with basic file existence check

3. **Add file conversion logic using markitdown**
   - Status: Completed
   - Description: Integrated markitdown library in main.py to convert input file to Markdown, with basic error handling

4. **Implement output file handling**
   - Status: Completed
   - Description: Implemented output file creation with same base name + .md extension in main.py

5. **Add error handling**
   - Status: Completed
   - Description: Added error handling for file not found, conversion errors, and output write errors in main.py

6. **Test basic functionality**
   - Status: Completed
   - Description: Tested with sample .txt file, successfully converted to .md

7. **Add help and usage documentation to README.md**
   - Status: Completed
   - Description: Updated README.md with usage instructions, installation, and examples

8. **Test edge cases**
   - Status: Completed
   - Description: Tested error cases: non-existent file, no arguments, help flag

9. **Add logging/output messages**
   - Status: Completed
   - Description: Added print statements for conversion progress and success/failure feedback

10. **Final testing and documentation**
    - Status: Completed
    - Description: All tests passed, documentation updated with final status

## Usage

Once implemented:

```bash
uv run main.py input_file.txt
# Outputs: input_file.md
```

## Installation

```bash
uv sync
```

## Dependencies

- Python >= 3.13
- markitdown
