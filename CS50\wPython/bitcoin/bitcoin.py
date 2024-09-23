import requests
import sys


def main():
    amount = get_price() * input_check()
    print(f"${amount:,.4f}")


def get_price():
    try:
        page = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin_rate = page.json()
        price =  bitcoin_rate["bpi"]["USD"]["rate"]
        return float(price.replace(",", ""))
    except requests.RequestException:
        sys.exit("There is an issue with JSON")

def input_check():
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")


if __name__ == "__main__":
    main()