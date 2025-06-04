from sys import stdin

def main():
    N = int(stdin.readline())
    A = sorted(map(int, stdin.readline().split()))

    if N == 2:
        x, y = A[1], A[0]
        print(x - y)
        print(x, y)
        return

    positives = [a for a in A if a >= 0]
    negatives = [a for a in A if a < 0]

    steps = []
    # Case: Both positive and negative numbers
    if positives and negatives:
        # Take the largest positive and accumulate subtractions
        tmp = negatives[0]
        for x in positives[:-1]:
            steps.append((tmp, x))
            tmp -= x
        steps.append((positives[-1], tmp))
        tmp = positives[-1] - tmp
        for x in negatives[1:]:
            steps.append((tmp, x))
            tmp -= x
    # Case: All numbers are positive
    elif positives:
        tmp = A[0]
        for x in A[1:-1]:
            steps.append((tmp, x))
            tmp -= x
        steps.append((A[-1], tmp))
        tmp = A[-1] - tmp
    # Case: All numbers are negative
    else:
        tmp = A[-1]
        for x in reversed(A[:-1]):
            steps.append((tmp, x))
            tmp -= x
    print(tmp)
    for x, y in steps:
        print(x, y)

if __name__ == "__main__":
    main()