list1=("Volkswagen", "Volkswagen", "Mercedes-Benz", "Jeep", "Hyundai", "Nissan")
print(list1)

tuple1=("Volkswagen", "Volkswagen", "Mercedes-Benz", "Jeep", "Hyundai", "Nissan")
print(list1)

set1={"Volkswagen", "Volkswagen", "Mercedes-Benz", "Jeep", "Hyundai", "Nissan"}
print(set1)

set2={"Mercedes-Benz", "Toyota", "BYD"}
print(set2)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))