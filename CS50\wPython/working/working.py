import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if match := re.search(r"^((?:(?:[1][0-2])|(?:[1-9]))(?::(?:(?:[5][0-9])|(?:[0-4][0-9])))? (?:AM|PM)) to ((?:(?:[1][0-2])|(?:[1-9]))(?::(?:(?:[5][0-9])|(?:[0-4][0-9])))? (?:AM|PM))$", s):
        # match.group(1) = 1-12 hours +? 00- 59 min + AM or PM
        # match.group(2) = 1-12 hours +? 00- 59 min + AM or PM
        times = []
        for case in match.groups():
            if case.endswith(" AM"):
                if ":" in case:
                    hours, minutes = case.replace(" AM", "").split(":")
                    if int(hours) < 10:
                        hours = "0" + hours
                    elif int(hours) == 12:
                        hours = "00"
                    times.append(f"{hours}:{minutes}")
                else:
                    hours = case.replace(" AM", "")
                    if int(hours) < 10:
                        hours = "0" + hours
                    elif int(hours) == 12:
                        hours = "00"
                    times.append(f"{hours}:00")
            else:
                if ":" in case:
                    hours, minutes = case.replace(" PM", "").split(":")
                    if int(hours) != 12:
                        hours = str(int(hours) + 12)
                    times.append(f"{hours}:{minutes}")
                else:
                    hours = case.replace(" PM", "")
                    if int(hours) != 12:
                        hours = str(int(hours) + 12)
                    times.append(f"{hours}:00")
        return f"{times[0]} to {times[1]}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()