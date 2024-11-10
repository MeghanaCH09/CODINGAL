myset={}
print(myset)

myset={1, 2, 3, 5, 5, 5, 6, 7, 7, 7, 9, 9}
print(myset)

set1=myset
set2={1, 3, 10, 4, 7, 9, 11, 22}
print("Set 1: ", set1)
print("Set 2: ", set2)

print("Difference: ")
print(set1.difference(set2))
print("Symetric Difference")
print(set1.symmetric_difference(set2))
