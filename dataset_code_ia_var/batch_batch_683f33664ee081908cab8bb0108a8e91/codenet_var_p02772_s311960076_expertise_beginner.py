n = int(input())
a = input().split()
b = []
for i in range(n):
    b.append(int(a[i]))
ans = "APPROVED"
for i in range(n):
    if b[i] % 2 == 0:
        if b[i] % 3 != 0 and b[i] % 5 != 0:
            ans = "DENIED"
print(ans)