file = open("sample3.txt", "r")
count=0
file = file.readlines()
for i in file:
    count=count+1
print(count)