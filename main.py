import argparse
import sys
from pathlib import Path
from markitdown import MarkItDown


def main():
    parser = argparse.ArgumentParser(description="Convert files to Markdown using MarkItDown")
    parser.add_argument("input_file", help="Path to the input file to convert")
    
    args = parser.parse_args()
    
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' does not exist.")
        sys.exit(1)
    
    print(f"Converting: {input_path}")
    
    # Initialize MarkItDown
    md = MarkItDown()
    
    # Convert the file
    try:
        result = md.convert(str(input_path))
        markdown_content = result.text_content
    except Exception as e:
        print(f"Error converting file: {e}")
        sys.exit(1)
    
    print("Conversion successful.")
    
    # Create output file path
    output_path = input_path.with_suffix('.md')
    
    # Write the markdown content to file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Output written to: {output_path}")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
