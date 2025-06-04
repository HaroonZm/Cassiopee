from sys import stdin
from itertools import accumulate

def main():
    n, d = map(int, stdin.readline().split())
    D = list(map(int, stdin.readline().split()))
    A = [0] * (n + 2)
    P = [0] * (n + 2)

    pos = d
    P[0] = pos
    for i, x in enumerate(D):
        pos = abs(pos - x) if x <= 2 * pos else pos
        P[i + 1] = pos
        if pos == 0:
            P[i + 2:] = [0] * (n - i - 1)
            break

    for i in range(n - 1, -1, -1):
        A[i] = (A[i + 1] + D[i]) if D[i] <= 2 * A[i + 1] + 1 else A[i + 1]

    q = int(stdin.readline())
    Q = map(int, stdin.readline().split())
    for i in Q:
        idx = i
        if P[idx - 1] <= A[idx] and pos == 0:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    main()