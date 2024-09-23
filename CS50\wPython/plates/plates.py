def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    num_indicator = False
    if not 1 < len(plate) < 7:
        return False

    for character in plate:
        if character.isalpha() or character.isnumeric():
            if num_indicator:
                if character.isalpha():
                    return False
            else:
                if character.isnumeric():
                    if character == "0":
                        return False
                    else:
                        num_indicator = True
        else:
            return False


    return True

if __name__ == "__main__":
    main()