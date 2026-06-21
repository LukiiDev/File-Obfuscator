import os
import sys
import base64
import time
from colorama import init, Fore, Style

init(autoreset=True)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def animate_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_welcome():
    ascii_art = r"""
 ██████╗ ██████╗ ███████╗██╗   ██╗███████╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗
██╔═══██╗██╔══██╗██╔════╝██║   ██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║   ██║██████╔╝█████╗  ██║   ██║███████╗██║     ███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══██╗██╔══╝  ██║   ██║╚════██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝██████╔╝██║     ╚██████╔╝███████║╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
"""
    print(Fore.RED + ascii_art)
    animate_text(Fore.RED + "[ O B F U S C A T O R ]", delay=0.02)

def loading_animation(text, duration=1):
    for i in range(int(duration * 10)):
        print(f"\r{Fore.RED}{text} {'.' * (i % 4)}", end='', flush=True)
        time.sleep(0.1)
    print(f"\r{Fore.RED}{text} ✓{Style.RESET_ALL}")

def show_menu():
    print(f"\n{Fore.RED}{'='*40}")
    animate_text(Fore.RED + "Please choose an option:", delay=0.03)
    print(f"{Fore.RED}{'='*40}")
    print(f"{Fore.YELLOW}1. Obfuscate a file (.py or .txt)")
    print(f"{Fore.YELLOW}2. Deobfuscate a file")
    print(f"{Fore.YELLOW}3. Exit")
    print(f"{Fore.RED}{'='*40}{Style.RESET_ALL}")
    choice = input(Fore.RED + "Enter your choice (1-3): " + Style.RESET_ALL)
    return choice

def is_valid_file(file_path):
    if not os.path.exists(file_path):
        print(f"{Fore.RED}✗ File not found: {file_path}{Style.RESET_ALL}")
        return False
    if not (file_path.endswith('.py') or file_path.endswith('.txt')):
        print(f"{Fore.RED}✗ Only .py and .txt files are supported!{Style.RESET_ALL}")
        return False
    return True

def obfuscate_file():
    print(f"\n{Fore.RED}[OBFUSCATE FILE]{Style.RESET_ALL}")
    file_path = input(Fore.RED + "Enter the path to the file you want to obfuscate: " + Style.RESET_ALL).strip()
    if not is_valid_file(file_path):
        return
    try:
        loading_animation(Fore.RED + "Reading file", duration=1)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_data = file.read()
        
        loading_animation(Fore.RED + "Obfuscating", duration=1.5)
        obfuscated_data = base64.b64encode(file_data.encode('utf-8')).decode('utf-8')
        
        obfuscated_file_path = file_path + '.obfuscated'
        loading_animation(Fore.RED + "Saving file", duration=1)
        with open(obfuscated_file_path, 'w', encoding='utf-8') as obfuscated_file:
            obfuscated_file.write(obfuscated_data)
        
        print(f"{Fore.GREEN}✓ File obfuscated successfully!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✓ Saved as: {obfuscated_file_path}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✓ Obfuscated file size: {os.path.getsize(obfuscated_file_path)} bytes{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}✗ Error obfuscating file: {e}{Style.RESET_ALL}")

def deobfuscate_file():
    print(f"\n{Fore.RED}[DEOBFUSCATE FILE]{Style.RESET_ALL}")
    file_path = input(Fore.RED + "Enter the path to the obfuscated file: " + Style.RESET_ALL).strip()
    if not os.path.isfile(file_path):
        print(f"{Fore.RED}✗ Invalid file. Please provide a valid obfuscated file.{Style.RESET_ALL}")
        return
    try:
        loading_animation(Fore.RED + "Reading file", duration=1)
        with open(file_path, 'r', encoding='utf-8') as file:
            obfuscated_data = file.read()
        
        loading_animation(Fore.RED + "Deobfuscating", duration=1.5)
        deobfuscated_data = base64.b64decode(obfuscated_data.encode('utf-8')).decode('utf-8')
        
        if file_path.endswith('.obfuscated'):
            deobfuscated_file_path = file_path[:-11]
        else:
            deobfuscated_file_path = file_path + '.deobfuscated'
        
        loading_animation(Fore.RED + "Saving file", duration=1)
        with open(deobfuscated_file_path, 'w', encoding='utf-8') as deobfuscated_file:
            deobfuscated_file.write(deobfuscated_data)
        
        print(f"{Fore.GREEN}✓ File deobfuscated successfully!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✓ Saved as: {deobfuscated_file_path}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}✗ Error deobfuscating file: {e}{Style.RESET_ALL}")

def main():
    while True:
        clear_screen()
        show_welcome()
        choice = show_menu()
        if choice == '1':
            obfuscate_file()
        elif choice == '2':
            deobfuscate_file()
        elif choice == '3':
            animate_text(Fore.RED + "Exiting...", delay=0.05)
            sys.exit(0)
        else:
            print(f"{Fore.RED}✗ Invalid choice. Please try again.{Style.RESET_ALL}")
        input(Fore.RED + "\nPress Enter to continue..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()