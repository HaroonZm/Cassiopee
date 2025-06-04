def main():
    """
    Reads input for two lists of integers, processes them with a matching algorithm,
    and prints the resulting answer modulo 10^9+7.

    The function expects the following input:
    - An integer N (number of elements in each list)
    - N integers for the first list (A)
    - N integers for the second list (B)
    
    The goal is to pair elements between the two lists as per a custom greedy matching
    process and compute the number of valid arrangements modulo 10^9+7.
    """
    mod = 10 ** 9 + 7  # Large prime modulus for result normalization to prevent overflow
    
    # Read the size of the lists
    N = int(input())
    
    # Read N values for list A, tag each as a 0 (identifier for type A)
    A = []
    for i in range(N):
        a = int(input())
        A.append((a, 0))

    # Read N values for list B, tag each as a 1 (identifier for type B)
    B = []
    for i in range(N):
        b = int(input())
        B.append((b, 1))

    # Merge both lists and sort by their integer values (ignoring the identifier in sort)
    X = A + B
    X.sort()  # sorts by tuple's first element by default

    ans = 1   # To keep track of the total number of valid arrangements
    Ar = 0    # Unpaired elements from A
    Br = 0    # Unpaired elements from B

    # Iterate through each element in the sorted merged list X
    for value, kind in X:
        if kind == 0:  # Element is from A
            if Br > 0:
                # There are unmatched B elements; match current A with a B
                ans *= Br
                ans %= mod
                Br -= 1  # Used one unmatched B
            else:
                # No B to match, add A to the unmatched pool
                Ar += 1
        else:          # Element is from B
            if Ar > 0:
                # There are unmatched A elements; match current B with an A
                ans *= Ar
                ans %= mod
                Ar -= 1  # Used one unmatched A
            else:
                # No A to match, add B to the unmatched pool
                Br += 1

    # Output the final answer
    print(ans)

if __name__ == "__main__":
    main()