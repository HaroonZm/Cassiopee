N = int(input())
a = list(map(int, input().split()))
x = (min(a) + max(a)) // 2
b = []
for i in range(N):
    b.append(abs(x - a[i]))
print("{:.0f}".format(max(b)))