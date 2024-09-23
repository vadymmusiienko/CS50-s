def main():
    greeting = input(": ")
    print(f"${value(greeting)}")


def value(greeting):
    value = 100
    word = ""
    for letter in greeting.strip().lower():
        if letter == "h":
            value = 20
        break
    if value == 20:
        for letter in greeting.strip().lower():
            word = word + letter
            if len(word) == 5:
                break
        if word == "hello":
            value = 0
    return value


if __name__ == "__main__":
    main()