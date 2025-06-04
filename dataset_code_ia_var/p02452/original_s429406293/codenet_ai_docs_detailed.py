def main():
    """
    Main function to determine if set B is included in set A (i.e., if all elements in B are in A).
    Reads input from standard input and prints 1 if B ⊆ A, else 0.
    """
    # Read and discard the first line, which contains the number of elements in A (not used).
    _ = input()
    
    # Read the second line, split into elements, and convert to a set A.
    # This removes duplicates and allows for efficient set membership checking.
    A = set(input().split())
    
    # Read and discard the third line, which contains the number of elements in B (not used).
    _ = input()
    
    # Read the fourth line, split into elements, and convert to a set B.
    B = set(input().split())
    
    # Check if B is a subset of A by comparing the intersection of A and B to B.
    # If all elements of B are in A, then A & B == B.
    # Convert the boolean result to an integer (True=1, False=0) and print it.
    print(int(A & B == B))

if __name__ == "__main__":
    main()