# File-Obfuscator

A simple Python tool to obfuscate and deobfuscate .py and .txt files using Base64 encoding. Keep your code hidden from casual viewers.

Features


🔐 Obfuscate .py and .txt files into unreadable Base64
🔓 Deobfuscate files back to original code
🎨 Red themed CLI with animations
⚡ Fast and lightweight
💾 No key file needed


Installation


Clone this repository:


bashgit clone https://github.com/LukiiDev/file-obfuscator.git
cd file-obfuscator


Install required dependency:


bashpip install colorama

Usage

Run the script:

bashpython obfuscator.py

Main Menu

1. Obfuscate a file (.py or .txt)
2. Deobfuscate a file
3. Exit

Obfuscate


Choose option 1
Enter the path to your .py or .txt file
File will be saved as filename.obfuscated
Original file remains unchanged


Deobfuscate


Choose option 2
Enter the path to the .obfuscated file
File will be decoded back to original format
Automatically removes .obfuscated extension


Example

Original file: script.py

pythonprint("Hello World")
password = "secret123"

After obfuscation: script.py.obfuscated

cHJpbnQoIkhlbGxvIFdvcmxkIikKcGFzc3dvcmQgPSAic2VjcmV0MTIzIgo=

After deobfuscation: back to script.py

pythonprint("Hello World")
password = "secret123"

How It Works


Obfuscation: Converts file content to Base64 encoding (unreadable but reversible)
Deobfuscation: Decodes Base64 back to original content


This is not encryption — it's obfuscation. Anyone can decode Base64, but it prevents casual code viewing.

Notes


Only works with .py and .txt files
Original file is never deleted
Obfuscated files are text-based (safe to share)
No password/key required
