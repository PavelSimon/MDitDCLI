import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Convert files to Markdown using MarkItDown")
    parser.add_argument("input_file", help="Path to the input file to convert")
    
    args = parser.parse_args()
    
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' does not exist.")
        sys.exit(1)
    
    print(f"Input file: {input_path}")
    # TODO: Add conversion logic here


if __name__ == "__main__":
    main()
