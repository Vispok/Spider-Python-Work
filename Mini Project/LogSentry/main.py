import csv;

with open("data/sample_logs.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["source_ip"], row["status"])