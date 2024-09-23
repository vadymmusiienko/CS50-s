# Speedy Typing Challenge

#### Video Demo:  <URL HERE>

## Introduction

Welcome to the "Speedy Typing Challenge" - a Python-based typing test application designed to measure and improve your typing speed and accuracy! This project provides an interactive command-line interface where users can select a difficulty level and type randomly generated sentences within a given time limit. At the end of each session, detailed statistics on the user's typing speed, accuracy, and other relevant metrics are displayed.

## Project Structure

The project consists of several key components, each of which plays a significant role in the functionality of the application:

### `main.py`

This is the main script of the application, where the primary logic and user interactions are handled. It includes the `main()` function, which orchestrates the flow of the application, and several helper functions that contribute to different aspects of the typing test. Here's a quick overview of each function:

- `display_instructions()`: Displays introductory information and instructions to the user.
- `get_difficulty()`: Prompts the user to select a difficulty level ("Easy", "Medium", "Hard").
- `get_time_limit(difficulty)`: Sets the time limit for the typing test based on the selected difficulty level.
- `get_start_time()`: Records the start time of the typing test.
- `check_time_limit(start, limit)`: Checks whether the time limit for the typing test has been reached.
- `countdown()`: Provides a visual countdown before the start of the test.
- `type_sentence()`: Displays a random sentence for the user to type and evaluates their input.
- `typos_count(typed, original)`: Counts the number of typos in the user’s input compared to the original sentence.
- `stats(total_typos, accuracy_percentage, typing_speed, actual_speed, difficulty_level, words)`: Displays a summary of the user's performance in a structured table format.

### External Libraries

The project uses several external libraries to extend its functionality:

- `time`: Used to handle time-based operations such as measuring durations and implementing delays.
- `rich.console` and `rich.table`: Makes it easy to create visually appealing console output and structured tables.
- `wonderwords`: Generates random sentences for the typing test.
- `pyfiglet`: Used for generating ASCII art text for headers and titles.
- `random`: Provides functionality to randomly select sentences.

## Design Choices

The application was designed with user experience and performance measurement in mind. Key design decisions include:

- **Random Sentence Generation**: The use of the `wonderwords` library ensures a diverse set of sentences, making each typing test unique and challenging.
- **Difficulty Levels**: Offering different time limits for different difficulty levels (easy, medium, hard) allows users to choose how much time they are willing to spend on this test.
- **Real-Time Typing Analysis**: The application calculates both gross and net typing speeds, as well as accuracy, to give a comprehensive view of the user's typing ability.
- **Visual Feedback**: The use of `pyfiglet` for ASCII art and `rich` for table formatting makes the interface engaging and easy to read.

## Conclusion

The "Speedy Typing Challenge" is a simple yet effective tool for anyone looking to improve their typing skills. Whether you're a beginner or an experienced typist, this application provides a fun and challenging way to track your progress and push your limits. Enjoy your typing journey!

---

**Note**: To run the application, ensure you have Python installed along with the required external libraries (`rich`, `wonderwords`, `pyfiglet`). You can install these libraries using pip: `pip install rich wonderwords pyfiglet`.
