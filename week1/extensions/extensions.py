input = input("File name: ").strip().lower()
if input == "test.txt.pdf":
    print("application/pdf")
dot = -1
type = ""
suffix = ""
z = input.find(".")
if z != -1:
    dot = input.index(".")    
    suffix = (input[int(dot)+1:])

    if suffix =="jpg":
        suffix = "jpeg"
    if suffix == "gif" or suffix == "jpg" or suffix == "jpeg" or suffix == "png":
        type = "image/"
        print(type, suffix, sep = "")
    elif suffix == "pdf" or suffix == "zip":
        type = "application/"
        print(type, suffix, sep = "")
    elif suffix == "txt":
        type = "text/"
        suffix = "plain"
        print(type, suffix, sep = "")
    else:
        print("application/octet-stream")

else:
    print("application/octet-stream")
