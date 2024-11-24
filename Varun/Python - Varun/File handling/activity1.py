file = open('sample1.txt', 'r')
print(file.read())

file = open('sample.txt', 'w')
file.write("Hi there! Don't forget to take a look at my wonderful website!!!")


file = open('sample.txt', 'a')
file.write("Volkswagen is the best car brand in the world")
file.close()