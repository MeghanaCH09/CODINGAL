class parrot:
    species="bird"

    def __init__(self,name,age):
         self.name=name
         self.age=age

falcon=parrot("Falcon",12)
owl=parrot("Owl",7)

print(f"Falcon is a {falcon.species}")
print(f"Owl is a {owl.species}")

print(f"{falcon.name} is {falcon.age} years old")
print(f"{owl.name} is {owl.age} years old")