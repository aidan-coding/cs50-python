problem = input("Expression: ")
char = problem.split()
x = char[0]
y = char[1]
z = char[2]
if y == "+":
    final = float(x) + float(z)
    print(float(final))
elif y == "-":
    print(float(x) - float(z))
elif y == "/":
    print(float(x) / float(z))
elif y == "*":
    print(float(x) * float(z))
else:
    print("Enter math equation")