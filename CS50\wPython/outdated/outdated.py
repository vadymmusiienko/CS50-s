months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def get_a_date():
    while True:
        original_date = input("Date: ")
        try:
            month, day, year = original_date.split("/")
            if int(month) > 12 or int(day) > 31:
                raise ValueError
        except ValueError:
            try:
                month_day, year = original_date.split(",")
                month, day = month_day.split(" ")
                month = month.lower().capitalize()
                if month not in months or int(day) > 31:
                    raise ValueError
            except ValueError:
                pass
            else:
                return month, day, year
        else:
            return month, day, year

def main():
    while True:
        month, day, year = get_a_date()
        try:
            print(f"{int(year)}-{int(month):02}-{int(day):02}")
            break
        except ValueError:
            print(f"{int(year)}-{months[month]:02}-{int(day):02}")
            break
        else:
            pass

if __name__ == "__main__":
    main()