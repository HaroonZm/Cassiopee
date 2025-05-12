def solve():
    n = int(input())
    li = [int(_) for _ in input().split()]
    for i in range(n):
        for j in range(i+1, n):
            if abs(li[i]-li[j]) % (n-1) == 0:
                print(str(li[i]) + " " + str(li[j]))
                return

solve()