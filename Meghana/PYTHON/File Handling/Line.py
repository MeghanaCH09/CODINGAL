import os
print(os.getcwd())

file=open("newfile.txt","r")
count=0

content=file.read()
conlist=content.split("\n")

for i in conlist:
    if i:
        count+=1

print("the number of line in the text",count)