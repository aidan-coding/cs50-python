due = 50
change = 0
while due > 0:
    print("Amount Due:", due)
    give = int(input("Insert Coin: "))
    if give == 5 or give == 10 or give == 25:
        due = due - give
        change += give
change += -50
print("Change Owed:", change)