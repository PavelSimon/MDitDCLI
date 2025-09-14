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
   - Status: Pending
   - Description: Integrate markitdown library to convert input file to Markdown

4. **Implement output file handling**
   - Status: Pending
   - Description: Create output file with same base name + .md extension

5. **Add error handling**
   - Status: Pending
   - Description: Handle file not found, conversion errors, unsupported formats

6. **Test basic functionality**
   - Status: Pending
   - Description: Test with sample file (e.g., .txt or .docx)

7. **Add help and usage documentation to README.md**
   - Status: Pending
   - Description: Update README with usage instructions and examples

8. **Test edge cases**
   - Status: Pending
   - Description: Test various file types and error scenarios

9. **Add logging/output messages**
   - Status: Pending
   - Description: Provide user feedback on conversion progress

10. **Final testing and documentation**
    - Status: Pending
    - Description: Comprehensive testing and complete documentation

## Usage

Once implemented:

```bash
python main.py input_file.txt
# Outputs: input_file.md
```

## Installation

```bash
pip install -e .
```

## Dependencies

- Python >= 3.14
- markitdown (to be added)
