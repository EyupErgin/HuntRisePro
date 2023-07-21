# main.py
import argparse
import json
from tabulate import tabulate
import pandas as pd

from core.banner import banner
from core.export import export_results
from core.scanner import run_scan

def main():
    banner()

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--target", help="Single IP address to scan")
    group.add_argument("-f", "--file", help="Text file containing IP addresses to scan")
    parser.add_argument("-oJ", "--output", help="Output JSON filename")
    parser.add_argument("-mT", "--multithread", type=int, metavar="N", help="Enable multithreading with N threads")
    args = parser.parse_args()

    if args.target:
        ip_list = [args.target]
    elif args.file:
        with open(args.file, "r") as f:
            ip_list = f.readlines()

    if not ip_list:
        print("[INFO] No IP addresses found in the input.")
        return

    try:
        results = run_scan(ip_list, args.multithread)

        if results:
            print_results(results)
            export_results(results, args.output)
        else:
            print("[INFO] No C2 servers detected.")
    except Exception as e:
        print("[ERROR] An error occurred:", e)

def print_results(results):
    table_data = []
    headers = ["STATUS", "IP ADDRESS", "CN", "ASN", "PAGE TITLE", "FULL URL"]

    for result in results:
        table_data.append([
            result.get("STATUS", ""),
            result.get("IP ADDRESS", ""),
            result.get("CN", ""),
            result.get("ASN", ""),
            result.get("PAGE TITLE", ""),
            result.get("FULL URL", "")
        ])

    df = pd.DataFrame(table_data, columns=headers)

    pd.set_option("display.max_colwidth", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)

    if not df.empty:
        df = df.reset_index(drop=True)
        df.index += 1
        print(tabulate(df, headers, tablefmt="simple"))
    else:
        print("[INFO] No C2 servers detected.")

if __name__ == "__main__":
    main()
