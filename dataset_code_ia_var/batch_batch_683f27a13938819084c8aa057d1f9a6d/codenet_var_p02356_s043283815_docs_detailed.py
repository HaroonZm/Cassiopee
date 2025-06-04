import sys

def main():
    """
    Main entry point of the program.
    Reads input, prepares prefix sums, and outputs results for each query.
    """
    readline = sys.stdin.readline
    write = sys.stdout.write

    # Read number of elements N and number of queries Q
    N, Q = map(int, readline().split())
    # Read the sequence of N integers
    A = list(map(int, readline().split()))
    # Read Q queries
    X = list(map(int, readline().split()))

    # Prepare prefix sum arrays
    ss = [0]      # ss[i]: prefix sum of first i elements (0-based, ss[0]=0)
    tt = []       # tt[i]: prefix sum up to ith element (same as ss[1:])
    v = 0
    for a in A:
        v += a
        ss.append(v)
        tt.append(v)
    # Remove last element from ss (to keep it length N)
    ss.pop()
    # Add a large value at the end of tt to act as a sentinel
    tt.append(10**15)

    def solve(x):
        """
        For a given integer x, yields for each prefix sum ss[s] (in order),
        how many complete blocks of sum ≥ x have been passed up to that point.

        Args:
            x (int): The threshold value per 'block'.

        Yields:
            int: The number of completed blocks up to each prefix sum.
        """
        t = 0              # Counter for full blocks
        # Create an iterator for the extended prefix sums array
        it = iter(tt).__next__  # Equivalent to next(it)
        nxt = it() - x          # The next threshold at which one additional block is filled
        # Enumerate through each prefix sum in ss
        for s, c in enumerate(ss):
            # For each prefix sum, check if next block boundary is below/equal
            while nxt <= c:
                nxt = it() - x
                t += 1
            # Yield number of blocks completed up to position s
            yield t - s

    # For each query x in X, call solve(x), sum the result (total blocks for all prefixes), format as str
    results = (str(sum(solve(x))) for x in X)
    # Print results: one per line
    write("\n".join(results))
    write("\n")

if __name__ == "__main__":
    main()