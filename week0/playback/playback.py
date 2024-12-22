str1 = input("> ")
str2 = []
for i in str1:
    if i == " ":
        str2.append("...")
    else:
        str2.append(i)
str3 = "".join(str2)
print(str3)