def swap1(a,b): 
    #Code to swap 'a' and 'b'
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print ("After swapping: a =", a, "b =", b)

def swap2(a, b): 
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1

swap1(4,7)
swap2(4,7)