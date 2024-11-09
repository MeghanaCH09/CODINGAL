list1=["Volkswagen", "Mercedes-Benz", "Audi", "BYD", "Nissan", "Hyundai"]
print("list1", list1)

list1.append("computer")

list1.insert(2, "Tata")
print("insertedlist",list1)

list1.pop(2)
print("poppedlist",list1)

list1.remove("Nissan")
print("removedlist",list1)

print("lengthist", len(list1))

list1.reverse()
print(list1)

print(list1[-1:-6:-3])
