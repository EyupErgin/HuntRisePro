# core/scanner.py
import sys
import requests
import time
import urllib3
import warnings
from bs4 import BeautifulSoup
import threading
import pandas as pd
from tabulate import tabulate
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

def load_json_config():
    try:
        with open("config/config.json", "r") as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        print("[ERROR] CONFIG file not found.")
        return None
    except json.JSONDecodeError:
        print("[ERROR] Invalid JSON format in CONFIG.")
        return None


def get_title(url):
    try:
        response = requests.get(url, verify=False, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("title")
        return title
    except requests.exceptions.RequestException:
        return None


def sanitize_url(url):
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
    return url


def get_first_word(string):
    words = string.split()
    if words:
        return words[0]
    return ""


def scan_directory_items(ip, directory_items, title):
    for item in directory_items:
        url = f"http://{sanitize_url(ip)}{item}"
        title_result = get_title(url)

        if title_result is None or (title not in title_result.text):
            continue

        api_url = f"http://ip-api.com/json/{ip}"
        response = requests.get(api_url)
        data = response.json()

        if "countryCode" not in data or "as" not in data:
            continue

        as_info = get_first_word(data["as"])

        result = {
            "STATUS": "[C2 DETECTED]",
            "IP ADDRESS": ip,
            "CN": data.get("countryCode", ""),
            "ASN": as_info,
            "PAGE TITLE": title_result.text,
            "FULL URL": url
        }

        results.append(result)


def scan_ip_with_thread(ip_list, lock, success_count):
    config = load_json_config()
    if config is None:
        return

    title = config.get("title")
    directory = config.get("directory")

    if not title or not directory:
        print("[ERROR] Invalid CONFIG JSON format: 'title' and 'directory' fields are required.")
        return

    if not isinstance(directory, list):
        print("[ERROR] 'directory' field must be a list.")
        return

    for ip in ip_list:
        scan_directory_items(ip, directory, title)


def run_scan(ip_list, num_threads=None):
    global results
    results = []
    success_count = {}
    lock = threading.Lock()

    def loading_animation():
        animation = ["[    ]", "[=   ]", "[==  ]", "[=== ]", "[ ===]", "[  ==]", "[   =]", "[    ]"]
        for frame in animation:
            time.sleep(0.2)
            print("" + frame, end="\r")

    def process_ips(ip_list):
        if num_threads:
            for ip in ip_list:
                ip = ip.strip()
                if ip not in success_count:
                    success_count[ip] = 0
                print(f"\tScanning IP address: {ip}", end="\r")
                loading_animation()
                scan_ip_with_thread([ip], lock, success_count)

            sys.stdout.write("\033[K")
            total_scanned = len(ip_list)
            detected_c2_count = sum(success_count.values())

        else:
            for ip in ip_list:
                ip = ip.strip()
                if ip not in success_count:
                    success_count[ip] = 0
                print(f"\tScanning IP address: {ip}", end="\r")
                loading_animation()
                scan_ip_with_thread([ip], lock, success_count)

            sys.stdout.write("\033[K")
            total_scanned = len(ip_list)
            detected_c2_count = sum(success_count.values())

            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print(f"\n[INFO] Total Scanned IP Addresses: {total_scanned}", end="\n" + "\n")

    if num_threads:
        thread_count = min(max(num_threads, 1), 5)
        threads = []
        split_size = (len(ip_list) + thread_count - 1) // thread_count
        for i in range(thread_count):
            start = i * split_size
            end = (i + 1) * split_size
            thread = threading.Thread(target=process_ips, args=(ip_list[start:end],))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    else:
        process_ips(ip_list)

    return results
