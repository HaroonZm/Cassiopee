def main():
    while True:
        line = input()
        if line == "":
            break
        n, m, k = map(int, line.split())
        if n == 0 and m == 0 and k == 0:
            break

        # Initialize list for counts of sums, index from n to n*m
        # counts[s] = number of ways to get sum s
        counts = [0]*(n*m+1)

        # Base case for one die
        for i in range(1, m+1):
            counts[i] = 1

        # For more than 1 die, calculate counts iteratively
        for dice in range(2, n+1):
            new_counts = [0]*(n*m+1)
            for s in range(dice-1, (dice-1)*m+1):
                if counts[s] != 0:
                    for face in range(1, m+1):
                        new_counts[s+face] += counts[s]
            counts = new_counts

        total = m**n
        expected = 0.0
        # sum of spots s runs from n to n*m
        for s in range(n, n*m+1):
            val = s - k
            if val < 1:
                val = 1
            prob = counts[s]/total
            expected += val*prob

        print(expected)

if __name__ == "__main__":
    main()