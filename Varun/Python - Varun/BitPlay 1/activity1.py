def checkbits(input1): 
    ones=0
    zeros=0
    while(input1): 
        if(input1&1==1): 
            ones=ones+1
        else: 
            zeros=zeros+1
        input1>>=1
    print("No of zeros:", zeros)
    print()
    print("No of ones:", ones)
input1=int(input("Enter desired number: "))
checkbits(input1)