def main(amount_left):
    while amount_left > 0:
        print("Amount Due: " + str(amount_left))
        amount_left = amount_left - coins_check(amount_left)
    debt(amount_left)


def coins_check(_):
    coins = [25, 10, 5]
    coin = int(input("Insert Coin: "))
    if coin not in coins:
        return 0
    else:
        return coin


def debt(amount_of_change):
    change = 0 - amount_of_change
    print("Change Owed: " + str(change))

main(50)