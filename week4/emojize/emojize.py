import emoji
input = input("Input: ")
input = emoji.emojize(input, language = "alias")
print("Output:",input)