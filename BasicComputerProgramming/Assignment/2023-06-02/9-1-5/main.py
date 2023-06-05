file = open("text.txt","w")

while True:
    text = input("Input Text,,, If you not empty program is stopped...")
    if len(text) == 0:
        break
    else:
        file.write("\n"+text)
