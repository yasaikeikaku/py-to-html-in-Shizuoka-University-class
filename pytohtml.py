#!/usr/bin/env python3

import sys
import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Usage: pytohtml <input.py> [output.html]")
    sys.exit(1)

input_file = sys.argv[1]

# Check if input file exists
if not os.path.isfile(input_file):
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)

output_dir = os.path.expanduser('~/pytohtml_output')
os.makedirs(output_dir, exist_ok=True)

if len(sys.argv) == 3:
    output_file = sys.argv[2]
else:
    # Default output name: input file name with .html extension
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = base_name + '.html'

output_path = os.path.join(output_dir, output_file)

# Read Python code from file
with open(input_file, 'r') as f:
    code = f.read()

# Convert to HTML with syntax highlighting
html = highlight(code, PythonLexer(), HtmlFormatter())

# Write to output file
with open(output_path, 'w') as f:
    f.write(html)

print(f"Converted {input_file} to {output_path}")
