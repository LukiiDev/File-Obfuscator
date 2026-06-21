# File-Obfuscator

A Python tool to obfuscate and deobfuscate .py and .txt files using Base64 encoding.

## What It Does

Obfuscates your Python and text files into unreadable Base64 so others cannot easily read your code. You can also deobfuscate them back to the original format.

## Installation

1. Clone the repository:
```
git clone https://github.com/LukiiDev/file-obfuscator.git
cd file-obfuscator
```

2. Install the required package:
```
pip install colorama
```

## How to Use

Run the script:
```
python obfuscator.py
```

You will see a menu with three options:

1. Obfuscate a file - Enter the path to your .py or .txt file
2. Deobfuscate a file - Enter the path to an .obfuscated file
3. Exit - Close the program

## Example

Original file (script.py):
```
print("Hello World")
password = "secret123"
```

After obfuscation (script.py.obfuscated):
```
cHJpbnQoIkhlbGxvIFdvcmxkIikKcGFzc3dvcmQgPSAic2VjcmV0MTIzIgo=
```

When you deobfuscate it, you get the original code back.

## Features

- Obfuscate .py and .txt files
- Deobfuscate files back to original format
- Red colored CLI with animations
- No password or key needed
- Original files are never deleted
- Fast and lightweight

## Important Notes

This is obfuscation, not encryption. It makes code unreadable but anyone with basic knowledge can decode Base64. For real security, use actual encryption.

## Supported Files

- Python files (.py)
- Text files (.txt)

