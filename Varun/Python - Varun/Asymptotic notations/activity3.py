def ONSquareTime(n):
    iteration=0
    for i in range(0, n): 
        for j in range(0, n): 
            print("*", end =" ")
            iteration+=1
        print(" ")
    print("\n When is", n, "Iteration = ", iteration, "\n")
ONSquareTime(5)
ONSquareTime(4)
ONSquareTime(3)