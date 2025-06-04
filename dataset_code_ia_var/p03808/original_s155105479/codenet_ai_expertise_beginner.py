import sys

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    total = sum(A)
    s = N * (N + 1) // 2
    if total % s != 0:
        print("NO")
        return
    t = total // s
    d = []
    for i in range(N):
        prev = A[i-1]
        diff = A[i] - prev - t
        d.append(diff)
    for i in range(N):
        if d[i] > 0:
            print("NO")
            return
        if d[i] % N != 0:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    main()