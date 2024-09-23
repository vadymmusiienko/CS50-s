def main():
    # Prompt for text
    text = input("Text: ")

    # Number of letters and sentences and words
    letters = 0
    sentences = 0
    words = 0
    for l in text:
        if l.isalpha():
            letters += 1
        elif l.isspace():
            words += 1
        elif l in [".", "!", "?"]:
            sentences += 1
    words += 1

    # Find Coleman-Liau index
    L = (letters / words) * 100
    S = (sentences / words) * 100
    grade = round(0.0588 * L - 0.296 * S - 15.8)

    # Print out the grade
    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")


if __name__ == "__main__":
    main()
