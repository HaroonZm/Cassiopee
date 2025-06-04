n = int(input())
a = input().split()
b = []
for i in range(n):
    b.append(int(a[i]))
total = 0
for i in range(n):
    total = total + b[i]
diviseur = n * (n + 1) // 2
if total % diviseur != 0:
    print("NO")
    exit()
steps = total // diviseur
compte = 0
for i in range(n):
    if i == n - 1:
        diff = b[i] - b[0]
    else:
        diff = b[i] - b[i+1]
    val = diff + steps
    if val < 0:
        print("NO")
        exit()
    if val % n != 0:
        print("NO")
        exit()
    compte = compte + (val // n)
if compte == steps:
    print("YES")
else:
    print("NO")