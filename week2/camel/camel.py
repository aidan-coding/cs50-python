camel = input("camelCase ")
snake = []
for i in camel:
    if i.isupper() == True:
        snake.append("_",)
        snake.append(i.lower())
    else:
        snake.append(i)
snake = "".join(snake)
print(camel)
print(snake)
        