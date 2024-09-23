def main():
    fuel = input("Fraction: ")
    result = gauge(convert(fuel))
    print(result)


def convert(fraction):
    while True:
        num1, num2 = fraction.split("/")
        percent = round(int(num1) / int(num2) * 100)
        if 0 <= percent <= 100:
            return percent
        else:
            raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return str(percentage) + "%"


if __name__ == "__main__":
    main()