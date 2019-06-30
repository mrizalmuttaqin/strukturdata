fileName = "GuestList.txt"
accessMode = "w"
myFile = open(fileName,accessMode)
myFile.write("Hi there!\n")
myFile.write("How are you?")
myFile.close()
