import random


def main():
    solution, level = get_rand_int()
    print(guess(solution, level))


def guess(solution, level):
    while True:
        try:
            attempt = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if 0 < attempt <= level:
                if attempt == solution:
                    return "Just right!"
                elif attempt > solution:
                    print("Too large!")
                else:
                    print("Too small!")


def get_rand_int():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level > 0:
                return random.randint(1, level), level


if __name__ == "__main__":
    main()
