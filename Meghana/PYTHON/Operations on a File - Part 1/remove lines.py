f1=open('new.txt','r')
f2=open('another.txt','w')

for line in f1.readlines():
    if not (line.startswith('I have')):
        print(line)
        f2.write(line)

f1.close()
f2.close()