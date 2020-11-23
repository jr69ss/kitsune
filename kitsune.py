import os
import sys
import subprocess
from colorama import Fore, Style
from modules.name_scraper.namescraper import *


def banner():
    print("\n")
    print(Fore.LIGHTBLACK_EX  + '='*90)
    print(Fore.MAGENTA + "000      000        000                                                                      ")
    print(Fore.MAGENTA + "000     000   000   000             Y0000   000     000   000  A000A         .d0000000b.     ")
    print(Fore.MAGENTA + "000   000     000   000          0000       000     000   00000    0000     d000P   Y000b    ")
    print(Fore.MAGENTA + "000000              000000     0000         000     000   000        000   d000P     Y00b    ")
    print(Fore.MAGENTA + "000  000      000   000           Y0000     000     000   000        000   000000000000000   ")
    print(Fore.MAGENTA + "000   000     000   000              Y000   000     000   000        000    Y00000b.         ")
    print(Fore.MAGENTA + "000    000    000   Y00b.         0000Y     000     000   000        000      Y000000b.      ")
    print(Fore.MAGENTA + "000     000   000    'Y0000    0000Y          Y0000Y      000        000        'Y000000     ")
    print(Fore.LIGHTBLACK_EX  + '='*90)
    print(Fore.MAGENTA + "Who would you like to own today?")
    print(Style.RESET_ALL)


def options():
    print(Fore.CYAN + "[1] Name")
    print(Fore.CYAN + "[2] Website")
    print(Fore.CYAN + "[3] IP")
    print(Fore.CYAN + "[4] Email")
    print(Fore.CYAN + "[5] Company")
    print(Fore.CYAN + "[6] Username")
    print(Fore.CYAN + "[7] Picture")
    target = input(Fore.CYAN + "Select a choice :: ")
    print(Style.RESET_ALL)

    if target == "1":
        name()
    if target == "2":
        web()
    if target == "3":
        ip()
    if target == "4":
        email()
    if target == "5":
        company()
    if target == "6":
        username()


def name():
    name = input("Enter name :: ")
    print(Fore.GREEN + "[*] Recon Starting...")
    print(Style.RESET_ALL)
    search(name)




def web():
    web = input("Enter website URL :: ")
    print(Fore.GREEN + "[*] Recon Starting...")


def ip():
    ip = input("Enter IP :: ")
    print(Fore.GREEN + "[*] Recon Starting...")


def email():
    email = input("Enter email :: ")
    print(Fore.GREEN + "[*] Recon Starting...")

def company():
    company = input("Enter company name :: ")
    print(Fore.GREEN + "[*] Recon Starting...")

def username():
    username = input("Enter username :: ")
    print(Fore.GREEN + "[*] Username Recon Starting...")


def pic():
    print(Fore.YELLOW + "[!] Make sure you already put an image (jpg, jpeg, png, or bmp) in the known folder")
    print(Fore.GREEN + "[*] Reverse Searching...")


def main():
    banner()
    options()
    
    

            


            
if __name__ == '__main__':
    main()
