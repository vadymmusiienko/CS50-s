import random


def main():
    score = 0
    difficulty = get_level()
    for _ in range(10):
        n1, n2 = generate_integer(difficulty)
        result = n1 + n2
        for _ in range(3):
            try:
                user_answer = int(input(f"{n1} + {n2} = "))
                if user_answer != result:
                    raise ValueError
                score += 1
                break
            except ValueError:
                print("EEE")
        try:
            if user_answer != result:
                print(f"{n1} + {n2} = {n1 + n2}")
        except UnboundLocalError:
            print(f"{n1} + {n2} = {n1 + n2}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            difficulty = int(input("Level: "))
            if 0 < difficulty <= 3:
                return difficulty
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        n1, n2 = random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        n1, n2 = random.randint(10, 99), random.randint(10, 99)
    else:
        n1, n2 = random.randint(100, 999), random.randint(100, 999)
    return n1, n2


if __name__ == "__main__":
    main()
