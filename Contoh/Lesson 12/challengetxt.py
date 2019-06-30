myFile = open('challenge.txt','w')
myFile.write("Susan, 32\n")
myFile.write("Mike, 33\n")
myFile.write("Christopher, 80\n")
myFile.write("Bill, 100")
myFile.close()

myFile = open('challenge.txt','r')
print(myFile.read()+"\n")


