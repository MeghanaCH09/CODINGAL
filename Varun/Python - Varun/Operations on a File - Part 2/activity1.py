# creating a new file 
file = open("text2.txt", "x")
# opening and then reading the file
with open("text1.txt", "r") as file: 
    data = file.readlines()
    print (data)
    for line in data:
        word = line.split()
        print (word)
import os
if os.path.exists("textfile.txt"):
    print("File exists!!!")
else: 
    print("The file does not exist")
import os
os.remove("text2.txt")
file.close()