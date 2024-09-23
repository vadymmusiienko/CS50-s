def main():
    word = input("Input: ")
    print("Output: " + shorten(word))


def shorten(word):
    result = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in word:
        if letter not in vowels:
            result = result + letter
    return result

if __name__ == "__main__":
    main()