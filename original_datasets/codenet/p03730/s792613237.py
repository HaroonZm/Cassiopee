# ABC060
# B
# Choose Integers

a, b, c = map(int, input().split())
n = b

flag = False
for i in range(n):
    if (i * a) % b == c:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")