import math
true = True
while true == True:
    try:
        fraction = input("Fraction: ")
        slash = fraction.find("/")
        x = fraction[:slash]
        y = fraction[slash+1:]
        final = int(x)/int(y)
        if int(x) > int(y):
            continue
        else:
            fuel = round(final * 100)
            if fuel <= 1:
                print("E")
            elif fuel>= 99:
                print("F")
            else:
                print(fuel, "%", sep="")
    except:
        pass
    else: break
