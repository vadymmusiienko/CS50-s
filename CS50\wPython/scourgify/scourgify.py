import csv
import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few comman-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit(f"{sys.argv[1]} is not a CSV file")
elif not sys.argv[2].endswith(".csv"):
        sys.exit(f"{sys.argv[2]} is not a CSV file")

new = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(",")
            new.append({"last": last.strip(), "first": first.strip(), "house": row["house"] })

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in new:
        writer.writerow(row)

