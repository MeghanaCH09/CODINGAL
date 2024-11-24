star_rows=int(input("enter number of rows:"))
for i in range(star_rows,1,-1):
    for j in range(i):
        print("*",end="")
    print()