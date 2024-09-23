def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # check if plate starts with 2 letters
    letter_count = 0
    for letter in plate:
        if letter.isalpha():
            letter_count += 1
            if letter_count == 2:
                break
        else:
            return False

    # check if plate is between 2 and 6 characters
    if not 2 <= len(plate) <= 6:
        return False

    # check if numbers come at the end
    trigger = False
    for character in plate:
        if trigger:
            if not character.isdigit():
                return False
        elif character.isdigit():
            if character == "0":
                return False
            trigger = True

    # checks if there are any periods, spaces, or punctuation marks
    for character in plate:
        if not character.isalpha():
            if not character.isdigit():
                return False

    # the plate is valid
    return True


if __name__ == "__main__":
    main()