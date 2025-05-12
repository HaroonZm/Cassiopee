def main():
    n, m = map(int, input().split())
    p = [False] * n
    q = p[:]
    for i in range(m):
        j, k = map(int, input().split())
        if j == 1:
            p[k] = True
        if j == n:
            q[k] = True
        elif k == n:
            q[j] = True
    for i in range(n):
        if p[i] and q[i]:
            print("POSSIBLE")
            return
    print("IMPOSSIBLE")

main()