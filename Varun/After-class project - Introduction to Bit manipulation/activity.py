A = int(input("Enter the first binary number (0 or 1): "))
B = int(input("Enter the second binary number (0 or 1): "))

if A not in [0, 1] or B not in [0, 1]:
    print("Invalid input! Please enter only 0 or 1.")
else:
   
    and_result = A & B  
    or_result = A | B   
    xor_result = A ^ B  
    not_a_result = ~A & 1 

    print(f"Bitwise AND of {A} and {B}: {and_result}")
    print(f"Bitwise OR of {A} and {B}: {or_result}")
    print(f"Bitwise XOR of {A} and {B}: {xor_result}")
    print(f"Bitwise NOT of {A}: {not_a_result}")
