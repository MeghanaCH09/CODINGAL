def analyze_time_complexity():
    print("Analyzing the time complexity of each loop:")

    # First loop analysis
    print("First Loop:")
    print("This loop runs from 0 to n (inclusive), so it executes n+1 times.")
    print("Time complexity: O(n)\n")
    
    # Second loop analysis
    print("Second Loop:")
    print("This loop starts with j=1 and multiplies j by 2 each time, running until j > n+1.")
    print("The number of iterations is approximately log2(n+1).")
    print("Time complexity: O(log n)\n")
    
    # Third loop analysis
    print("Third Loop:")
    print("This loop always runs a fixed number of times (100 iterations), independent of n.")
    print("Time complexity: O(1)\n")
    
    # Total time complexity
    print("Overall Time Complexity:")
    print("The total time complexity is dominated by the loop with the highest growth rate.")
    print("Hence, the overall time complexity of the function is O(n).")

# Call the function to display the analysis
analyze_time_complexity()
