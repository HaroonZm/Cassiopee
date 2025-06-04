def main():
    s1 = input()
    s2 = input()
    ret = solve(s1, s2)
    print(ret)

def solve(s1, s2):
    N, M = map(int, s1.split())
    X = list(map(int, s2.split()))
    if N >= M:
        return 0
    X.sort()
    diffs = []
    for i in range(M - 1):
        diffs.append(X[i + 1] - X[i])
    diffs.sort()
    total = 0
    for j in range(M - N):
        total += diffs[j]
    return total

main()