number_Largest = int(input("Enter Largest number: "))
number_Smallest = int(input("Enter Smallest number: "))

#Eucliden Algorithms
while(number_Smallest): 
    number_Store = number_Smallest
    number_Smallest = number_Largest % number_Smallest
    print(number_Store)
    print(number_Smallest)
    number_Largest = number_Store

print("HCF/GCD: ", number_Largest)