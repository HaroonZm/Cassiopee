def main():
    """
    Main function to read input, process the array according to the specified logic, 
    and print the required output.
    """
    # Read the number of elements in the array
    N = int(input())
    # Read the N integers as a list
    *A, = map(int, input().split())
    
    # Compute the list of absolute values of the elements in A
    aA = [abs(a) for a in A]
    # Calculate the sum of absolute values
    asum = sum(aA)
    # Count how many elements in A are negative
    c = sum([(a < 0) for a in A])

    # If the count of negative numbers is odd,
    # subtract twice the smallest absolute value from the sum to make the minimal sum
    if c % 2:
        print(asum - min(aA) * 2)
    # If the count of negative numbers is even,
    # the minimal sum is just the sum of absolute values
    else:
        print(asum)

if __name__ == "__main__":
    main()