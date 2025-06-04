from bisect import bisect_left

def main():
    """
    This is the main function that solves the problem.
    It reads the number of items N, and two integer sequences A and B.
    The function computes the minimum number of elements to "improve" in A such that
    A[i] >= B[i] for every i, possibly using surplus in other positions of A.

    Input:
        N (int): The length of arrays A and B.
        A (Tuple[int]): The first integer sequence.
        B (Tuple[int]): The second integer sequence.

    Output:
        Prints the minimum required operations (int), or -1 if not possible.
    """

    # Read the size of the arrays/sequences
    N = int(input())
    # Read the first sequence A as a tuple of integers
    A = tuple(map(int, input().split()))
    # Read the second sequence B as a tuple of integers
    B = tuple(map(int, input().split()))

    surplus = []  # List to store surplus values where A[i] >= B[i]
    need = 0      # Total amount needed to balance deficits (where A[i] < B[i])
    ans = 0       # Counter for the number of deficit corrections required

    # Iterate over corresponding pairs in A and B
    for a, b in zip(A, B):
        diff = a - b  # Calculate difference at current index
        if diff >= 0:
            # Surplus case: store the surplus amount
            surplus.append(diff)
        else:
            # Deficit case: sum up the needed amount and increment ans
            need += -diff
            ans += 1

    # Sort surpluses in decreasing order to use larger surpluses first
    surplus.sort(reverse=True)

    # Compute cumulative sums of the sorted surpluses for efficient queries
    # cusum[i] stores the total of the largest i surplus elements
    cusum = [0] * (len(surplus) + 1)
    for i, sur in enumerate(surplus):
        cusum[i+1] = cusum[i] + sur

    # Find the smallest number of surplus items needed to meet or exceed the 'need'
    # Use bisect_left to find the minimal index such that cusum[index] >= need
    ans += bisect_left(cusum, need)

    # If more elements would have to be "improved" than available positions, print -1
    if ans > N:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()