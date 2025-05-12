# C - Streamline

def main():
    s1 = input()
    s2 = input()
    ret = solve(s1, s2)
    print(ret)

def solve(s1, s2):
    N, M = list(map(int, s1.split()))
    X = list(map(int, s2.split()))
    if (N >= M):
        return 0
    X.sort()
    l = []
    for i in range(M-1):
        l.append(X[i+1]-X[i])
    l.sort()
    ct = 0
    for j in range(M-N):
        ct += l[j]
    return ct

main()