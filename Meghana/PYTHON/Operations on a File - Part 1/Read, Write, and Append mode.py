file = open('new.txt', 'r')
print(file.read())
file.close()

file = open('new.txt', 'w')
file.write("I have used the write mode to edit the text")
file.close()

file = open('new.txt', 'a')
file.write("I have used the append mode to edit the text")
file.close()

file = open('new.txt', 'r')
print(file.readline(10))
file.close()

file = open('new.txt', 'r')
print(file.readline())
file.close()