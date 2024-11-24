file = open('sample2.txt', 'r')
print(file.read())

file = open('sample.txt', 'w')
file.write("Shreyas Iyer, maybe he is the appointed captain for PBKS for the folliwing IPL season")


file = open('sample.txt', 'a')
file.write("Mohamed Shami joining SRH in IPL 2025 after mission IPL 2024 due to injury in the world cup.")
file.close()