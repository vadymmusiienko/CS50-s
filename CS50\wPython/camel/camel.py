def main():
    camel_case = input("camelCase: ")
    print("snake_case: " + snake_case(camel_case))


def snake_case(camel_case):
    result = ""
    for letter in camel_case:
        if letter.isupper():
            result = result + "_" + letter.lower()
        else:
            result = result + letter
    return result



main()