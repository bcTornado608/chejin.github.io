import subprocess
import os
import sys
from shutil import which

# Path to your LaTeX file
latex_file = "cv_latex.tex"
# Desired HTML output file
html_file = "index.html"

# Check if LaTeX file exists
if not os.path.exists(latex_file):
    print(f"Error: LaTeX file '{latex_file}' not found!")
    sys.exit(1)


pandoc_path = r"C:\\Program Files\\Pandoc\\pandoc.exe"
# Try converting LaTeX to HTML
try:
    subprocess.run([
        pandoc_path,
        latex_file,
        "-s",           # standalone HTML
        "-o", html_file,
        "--mathjax"     # render math with MathJax
    ], check=True)
    print(f"Conversion successful! HTML saved as '{html_file}'")
except subprocess.CalledProcessError as e:
    print("Error: Conversion failed!")
    print(e)
