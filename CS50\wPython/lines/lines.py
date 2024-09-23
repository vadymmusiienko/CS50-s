import sys

count = 0
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    with open(sys.argv[1]) as program:
        for line in program:
            line = line.lstrip()
            if not line.startswith("#") and line != "":
                count +=1

except FileNotFoundError:
    sys.exit("File does not exist")

except IndexError:
    sys.exit("Too few command-line arguments")

print(count)
