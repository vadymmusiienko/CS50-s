import time
from rich.console import Console
from rich.table import Table
from wonderwords import RandomSentence
from pyfiglet import Figlet
from random import choice


# random sentences generator
s = RandomSentence()

# ASCII art generator
f = Figlet(font="varsity")


def main():
    # Number of typos
    typos = 0

    # Number of words typed
    word_counter = 0

    # Greetings and instructions
    display_instructions()

    # Get the difficulty
    difficulty = get_difficulty()

    # Get the time limit
    time_limit = get_time_limit(difficulty)

    # Countdown timer till the start of the typing test
    countdown()

    # Get the start time
    start_time = get_start_time()

    while not check_time_limit(start_time, time_limit):
        # prints a sentence and gathers info about it
        temp_typos, temp_word_counter = type_sentence()
        typos += temp_typos
        word_counter += temp_word_counter

    # calculate the total time spent, because a user can spend more time than they are supposed to
    total_time_spent = time.time() - start_time

    # calculate the gross speed (as if a user didn't make any typos)
    gross_speed = word_counter / (total_time_spent / 60)

    # calculate accuracy in decimal
    accuracy = (word_counter - typos) / word_counter

    # calculate accuracy in percentage
    percent_accuracy = accuracy * 100

    # calculate actual speed (taking typos into account)
    net_speed = gross_speed * accuracy

    # print the statistics about this trial
    stats(typos, percent_accuracy, gross_speed, net_speed, difficulty, word_counter)


def display_instructions():
    """
    Displays the instructions and explains the difficulty levels
    """
    print(f.renderText("Welcome to the Typing Test!"))
    print(
        "You will be given a text to type within a specific time limit based on the selected difficulty"
    )
    print("After the time is up, your speed and accuracy will be calculated")
    print("Lets get started by selecting a difficulty level")
    print("Easy = 30 sec |", "Medium = 1 min |", "Hard = 2 min")


def get_difficulty():
    """
    Asks user for the difficulty level and makes sure its valid, otherwise prompts again
    :return: (str), the level of difficulty: "easy", "medium" or "hard"
    """
    difficulty = input("Select Difficulty: ").strip().lower()
    while difficulty not in ["easy", "medium", "hard"]:
        print(
            "There is no such difficulty, these are the options:\nEasy | Medium | Hard"
        )
        difficulty = input("Try again: ").strip().lower()
    return difficulty


def get_time_limit(difficulty):
    """
    Sets a time limit according to a difficulty level (easy = 30sec, medium = 60sec, hard = 120sec)
    :param difficulty: (str), the level of difficulty ("easy", "medium" or "hard")
    :return: (float), the number of seconds a user has to type for
    """
    if difficulty == "easy":
        return 30.0
    elif difficulty == "medium":
        return 60.0
    else:
        return 120.0


def get_start_time():
    """
    Records the start time
    :return: (float), the start time in seconds
    """
    return time.time()


def check_time_limit(start, limit, current_time=None):
    """
    return True when the time is out
    :param current_time: (float), the current time, defaults to None.
    :param start: (float), the start of the timer
    :param limit: (float), the number of seconds to run this timer for
    :return: (bool), True when the time is out, False when there is time left
    """
    if current_time is None:
        current_time = time.time()
    return (current_time - start) > limit


def countdown():
    """
    The countdown for the type test
    """
    time.sleep(0.4)
    print("The test starts in...")
    time.sleep(1)
    for num in range(3, 0, -1):
        print(f.renderText(str(num)))
        time.sleep(1.2)
    print(f.renderText("GO!"))
    time.sleep(0.4)


def type_sentence():
    """
    Displays a random generated sentence for the user to retype, calculates the number of typos and total words
    :return: (tuple), a tuple of integers, first is a number of typos in a sentence, second - total number of words
    """
    local_typos = 0

    output_sentence = choice(
        [
            s.sentence(),
            s.bare_bone_sentence(),
            s.bare_bone_with_adjective(),
            s.simple_sentence(),
        ]
    )
    print(output_sentence)
    input_sentence = input(": ")
    output_sentence_words = output_sentence.split()
    input_sentence_words = input_sentence.split()

    if input_sentence_words != output_sentence_words:
        local_typos += typos_count(input_sentence_words, output_sentence_words)

    return local_typos, len(output_sentence_words)


def typos_count(typed, original):
    """
    Counts the number of misspelled words in a sentence as well as extra words and missing ones
    :param typed:
    :param original:
    :return:
    """
    sentence_typos = 0
    if len(typed) <= len(original):
        sentence_typos += len(original) - len(typed)

        for index, word in enumerate(typed):
            if word != original[index]:
                sentence_typos += 1
    else:
        sentence_typos += len(typed) - len(original)

        for index, word in enumerate(original):
            if word != typed[index]:
                sentence_typos += 1

    return sentence_typos


def stats(
    total_typos,
    accuracy_percentage,
    typing_speed,
    actual_speed,
    difficulty_level,
    words,
):
    """
    Shows the statistics of this speed test trial
    :param total_typos: (int), number of mistakes made by the user
    :param accuracy_percentage: (float), shows how accurate the user was (in terms of typos)
    :param typing_speed: (float), the gross typing speed (as if the user didn't make any typos)
    :param actual_speed: (float), the net speed (gross speed * accuracy)
    :param difficulty_level: (str), the difficulty of the test (timewise)
    :param words: (int), the number of words given to the user to retype
    """
    # create a table
    table = Table(title="Speed Test Results")

    # create columns
    table.add_column("Metric", style="red", no_wrap=True)
    table.add_column("Result", style="green", no_wrap=True)

    # create rows
    table.add_row("Difficulty", f"{difficulty_level} level".title())
    table.add_row("Number of words", f"{words} Words")
    table.add_row("Number of typos", f"{total_typos} Typos")
    table.add_row("Accuracy", f"{accuracy_percentage:.2f} %")
    table.add_row("Gross Typing Speed", f"{typing_speed:.2f} WPS")
    table.add_row("Net Typing Speed", f"{actual_speed:.2f} WPS")

    # print the net speed
    print(f.renderText(f"Your speed is {actual_speed:.2f} WPS"))

    # display the table
    console = Console()
    console.print(table)


if __name__ == "__main__":
    main()
