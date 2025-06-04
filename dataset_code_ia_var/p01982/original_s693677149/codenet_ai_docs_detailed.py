def main():
    """
    Main loop of the program: processes multiple test cases.  
    For each test case, reads integers n, l, r, and a list of n integer divisors.
    For all integers x in the range [l, r], checks divisibility by elements of a and increases a counter according to specific conditions.
    The loop stops when a triple of zeros is entered.
    """

    while True:
        # Read n, l, r from input and convert them to integers
        n, l, r = map(int, input().split())
        
        # Terminate the loop if all three inputs are zero
        if n == 0 and l == 0 and r == 0:
            break
        
        # Initialize an array a to store the list of n divisors, each set to 0 initially
        a = [0] * n
        
        # Initialize counter to count numbers satisfying the conditions
        cnt = 0
        
        # Read n integers from input and store into array a
        for i in range(n):
            a[i] = int(input())
            # Completion of list a
        
        # Iterate over every integer x in the range [l, r] (inclusive)
        for x in range(l, r + 1):
            for i in range(1, n + 1):
                if x % a[i - 1] == 0:
                    # If x is divisible by a[i-1], and it's the ith divisor
                    # If i is odd (i%2==1), increment the counter
                    if i % 2 == 1:
                        cnt += 1
                    # Once divisible, stop checking further divisors for this x
                    break
                # If reached the last check and n is even, increment the counter
                if i == n and n % 2 == 0:
                    cnt += 1
        # Output the total count for this test case
        print(cnt)

if __name__ == "__main__":
    main()