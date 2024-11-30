filereadmode = open("C:\Users\HP\Documents\CODINGAL\Meghana\PYTHON\File Handling", "r")
print("I am in read mode")
print(filereadmode.read())
filereadmode.close()

filewritemode = open('new.txt', 'w')
filewritemode.write("I am now in write mode...")
filewritemode.write("\nI have added a text using the write mode")
filewritemode.close()

fileappend = open('new.txt', 'a')
fileappend.write("\n\nI am now in the append mode")
fileappend.write("\nI have added a text using the append mode")
fileappend.close()