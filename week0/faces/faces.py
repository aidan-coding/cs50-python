text = input("")
face = False
for i in range(len(text)):
    if face == True:
        if text[i] == "(":
            print("🙁", end = "")
        elif text[i] == ")":
            print("🙂", end = "")
        face = False
    elif text[i] == ":":
        if text[i+1] == ")":
            face = True
        elif text[i+1] == "(":
            face = True
        else:
            print(":", end = "")

    else:
        print(text[i], end = "")
