def main():
    """
    Reads a list of integers, sorts it, and prints the difference according to the rules:
      - If the list length N is even, print the difference between the two middle elements.
      - If the list length N is odd, print the difference between the elements right after and right at the middle.
    """
    # Read the number of elements from input and convert to integer
    N = int(input())
    
    # Read the list of integers as input, split by spaces, map to int, and convert to list
    d = list(map(int, input().split()))
    
    # Sort the list d in ascending order
    d.sort()
    
    # If the number of elements is even,
    # print the difference between the two central elements
    if N % 2 == 0:
        # For even length: difference between element at position N//2 and the previous one
        print(d[N // 2] - d[N // 2 - 1])
    else:
        # For odd length: difference between element right after the middle and at the middle
        print(d[N // 2 + 1] - d[N // 2])

if __name__ == "__main__":
    main()