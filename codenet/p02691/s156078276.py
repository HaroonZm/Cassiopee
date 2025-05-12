from collections import defaultdict

def solve(*args: str) -> str:
    n = int(args[0])
    A = list(map(int, args[1].split()))

    ret = 0
    X = defaultdict(int)
    for i, a in enumerate(A):
        X[a+i] += 1

        if 0 <= i-a:
            ret += X[i-a]

    return str(ret)

if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))