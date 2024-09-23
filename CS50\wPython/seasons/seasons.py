from datetime import date
import sys
import inflect

p = inflect.engine()


def get_date(date_of_birth):
    try:
        year, month, day = date_of_birth.split("-")
        birth_date = date(int(year), int(month), int(day))
        return birth_date
    except ValueError:
        sys.exit("Invalid date")


def get_minutes(birth_date):
    now_date = date.today()
    time_difference = now_date - birth_date
    words = p.number_to_words(round(time_difference.total_seconds() / 60), andword="")
    return f"{words} minutes".capitalize()


def main():
    date_of_birth = input("Date of birth: ")
    print(get_minutes(get_date(date_of_birth)))


if __name__ == "__main__":
    main()
