#!python3

iim = lambda: map(int, input().rstrip().split())

def resolve():
    N = int(input())
    X = list(iim())

    av = (2 * sum(X) + N) // N // 2
    ans = 0
    for x in X:
        ans += (x - av)**2
    print(ans)

if __name__ == "__main__":
    resolve()