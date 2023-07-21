# core/export.py
import json

def export_results(results, output_filename):
    if output_filename:
        json_results = json.dumps(results, ensure_ascii=False)

        json_results = json_results.replace("\\/", "/")
        json_results = json_results.replace("\\u2014", "—")

        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(json_results)

        print(f"[INFO] Results saved to {output_filename}")
