file= open('new.txt', 'r')
print(file.read())
file.close()

file = open('new.txt', 'w')
file.write("I have added a text using append mode...")
file.close()

file = open('new.txt', 'r')
print(file.readline(15))
file.close()