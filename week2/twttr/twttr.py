str = input("Input: ")
final = ""
for i in str:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        i = ""
    if  i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        i = ""
    final += i
print(final)