def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    res = "YES"
    for i in range(N - 1):
        if A[i] == A[i + 1]:
            res = "NO"
    print(res)

if __name__ == "__main__":
    main()