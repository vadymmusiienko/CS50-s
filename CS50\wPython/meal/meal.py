def main():
    time = input("What time is it? ")
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    if minutes.endswith("a.m."):
        minutes = minutes.replace("a.m.", "")

    elif minutes.endswith("p.m."):
        minutes = minutes.replace("p.m.", "")
        hours = float(hours) + 12
        
    minutes =float(minutes) / 60
    return float(hours) + minutes

if __name__ == "__main__":
    main()
