def main():
    """
    Main function to read input, generate and print matrices based on the given parameters.
    The program continues to process until a case with k == 0 is encountered.
    """
    while True:
        # Read input values n and k from the user
        n, k = map(int, raw_input().split())

        # If k is zero, exit the loop and terminate the program
        if k == 0:
            break

        # Initialize an n x n matrix filled with '.'
        A = [['.' for _ in range(n)] for _ in range(n)]

        # Convert (k-1) to its binary representation, 
        # padded with zeros to length n/2 for further processing
        k_bin = bin(k - 1)[2:].zfill(n // 2)

        # If n is odd or the binary length exceeds n/2, 
        # it's not possible to construct a valid configuration
        if n % 2 == 1 or len(k_bin) > n // 2:
            print "No\n"
            continue

        # Fill specific positions in the first row of A with 'E' based on k_bin
        for i in range(n // 2):
            if k_bin[i] == '1':
                A[0][i * 2] = 'E'
                A[0][i * 2 + 1] = 'E'

        # Print the first row of the matrix as a string
        print ''.join(A[0])

        # Process the rest of the matrix row by row
        for i in range(n - 1):
            for j in range(n):
                cnt = 0
                # Check if current cell matches the one above
                if i > 0 and A[i][j] == A[i - 1][j]:
                    cnt += 1
                # Check if current cell matches the one to the left
                if j > 0 and A[i][j] == A[i][j - 1]:
                    cnt += 1
                # Check if current cell matches the one to the right
                if j < n - 1 and A[i][j] == A[i][j + 1]:
                    cnt += 1

                # Decide the value of the cell below based on the count
                if cnt == 1:
                    A[i + 1][j] = A[i][j]
                elif A[i][j] == '.':
                    A[i + 1][j] = 'E'
                else:
                    A[i + 1][j] = '.'
            # Print each newly completed row as a string
            print ''.join(A[i + 1])
        # Print an empty line after each matrix for separation
        print

if __name__ == "__main__":
    main()