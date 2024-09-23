import sys
import csv
from tabulate import tabulate

menu = []

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for line in reader:
            menu.append(line)

except FileNotFoundError:
    sys.exit("The file does not exist")

except IndexError:
    sys.exit("Too few command-line arguments")

print(tabulate(menu, tablefmt="grid", headers="keys"))