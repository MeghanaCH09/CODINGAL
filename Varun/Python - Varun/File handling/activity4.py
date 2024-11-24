file = open('sample4a.txt', 'r')
print(file.read())
file.close()
file = open('sample4b.txt', 'r')
print(file.read())
file.close()

file = open('sample4a.txt', 'w')
file.write("Shreyas Iyer, maybe he is the appointed captain for PBKS for the folliwing IPL season")

file = open('sample4b.txt', 'a')
file.write("Mohamed Shami joining SRH in IPL 2025 after mission IPL 2024 due to injury in the world cup.")
file.close()

