import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'src="(https?://(?:www\.)?youtube\.com/embed/\w+)"', s, re.IGNORECASE):
        return re.sub(r"https?://(?:www\.)?youtube\.com/embed", "https://youtu.be", match.group(1))


if __name__ == "__main__":
    main()