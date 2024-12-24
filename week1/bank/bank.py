greet = input("Greeting: ").lower().strip()
owe = 2
print(greet)
if greet[0] == "h":
    owe += -1
x = greet.find("hello")
if x > -1:
    owe = 0
if owe == 1:
    owe = 20
elif owe == 2:
    owe = 100
print("$", owe, sep = "")