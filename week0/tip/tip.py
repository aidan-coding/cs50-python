def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    x = ""
    for i in d:
        if i != "$":
            x += i
    return float(x)



def percent_to_float(p):
    x = ""
    for i in p:
        if i != "%":
            x += i
    x = int(x) *.01
    return float(x)
    

main()