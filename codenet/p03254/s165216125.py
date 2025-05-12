n, x = map(int, input().split())
A = sorted(list(map(int, input().split())))
for i in range(n):
    if sum(A[:i + 1]) > x:
        print(i)
        exit()
    if sum(A[:i + 1]) == x:
        print(i + 1)
        exit()
print(i)