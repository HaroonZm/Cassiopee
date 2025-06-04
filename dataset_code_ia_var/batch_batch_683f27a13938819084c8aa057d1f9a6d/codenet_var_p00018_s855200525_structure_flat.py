a = list(map(int, input().split()))
a.sort(reverse=True)
x = 0
while x < len(a):
    if x == len(a) - 1:
        print(a[x])
    else:
        print(a[x], end=" ")
    x += 1