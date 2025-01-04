
def main():
    time = input("What time is it? ")
    hour = convert(time)
    if hour >= 7 and hour <= 8:
        print("breakfast time")
    elif hour >= 12 and hour <= 13:
        print("lunch time")
    elif hour >= 18 and hour <= 19:
        print("dinner time")
def convert(time1):
    hour, minutes = time1.split(":")
    minutes = int(minutes)/60
    hours = int(hour) + minutes
    return(hours)


if __name__ == "__main__":
    main()