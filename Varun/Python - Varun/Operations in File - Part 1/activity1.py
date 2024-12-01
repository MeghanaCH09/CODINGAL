file = open('sample1.txt', 'r')
print(file.read(12))

file = open('sample1.txt', 'r')
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readlines())
file.close()

file = open('sample1.txt', 'r')
for x in file: 
    print(x)
file.close()

file = open('sample1.txt', 'r')
file2 = open('sample1-2.txt', 'w')
print('sample1.txt.readlines()')
for i in file: 
    if (i.startswith("Volkswagen")): 
        pass
    else: 
        file2.write(i)
file.close()


