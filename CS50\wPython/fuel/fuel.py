def main():
    fuel = input("Fraction: ")
    result = check(percantage(fuel))
    print(result)


def percantage(fraction):
    while True:
        try:
            num1, num2 = fraction.split("/")
            percent = round(int(num1) / int(num2) * 100)
            if 0 <= percent <= 100:
                return percent
            else:
                fraction = input("Fraction: ")
        except (ValueError, ZeroDivisionError):
            fraction = input("Fraction: ")
            pass

def check(n):
    if n <= 1:
        return "E"
    elif n >= 99:
        return "F"
    return str(n) + "%"


if __name__ == "__main__":
    main()