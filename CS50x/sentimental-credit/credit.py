import re


def main():
    # Regual expression patters for each card
    regex_numeric = r"\d+"
    regex_master = r"5[1-5]\d{14}"
    regex_visa = r"4\d{12}(\d{3})?"
    regex_amex = r"3[47]\d{13}"
    # Make sure to get a valid credit card number (numeric)
    while True:
        num = input("Credit card number: ")
        if re.fullmatch(regex_numeric, num):
            break

    # Find out which kind of card it is
    if re.fullmatch(regex_master, num):
        card = "MASTERCARD"
    elif re.fullmatch(regex_visa, num):
        card = "VISA"
    elif re.fullmatch(regex_amex, num):
        card = "AMEX"
    else:
        card = "INVALID"

    # Check if valid
    if checksum(int(num)):
        print(card)
    else:
        print("INVALID")

# Check luhn_algorithm


def checksum(n):
    # Find the sum of its digits (by an algorithm)
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
        sum += dig_sum((n % 10) * 2)
        n = n // 10

    if sum % 10 == 0:
        return True

    return False


def dig_sum(i):
    sum = 0
    while i > 0:
        sum += i % 10
        i = i // 10
    return sum


if __name__ == "__main__":
    main()
