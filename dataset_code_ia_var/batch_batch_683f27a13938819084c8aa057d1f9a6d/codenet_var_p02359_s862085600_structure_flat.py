n, t = map(int, input().split(" "))
num = []
for i in range(t):
    num.append(0)
for i in range(n):
    l, r = map(int, input().split(" "))
    num[l] = num[l] + 1
    if r < t:
        num[r] = num[r] - 1
i = 1
while i < t:
    num[i] = num[i] + num[i - 1]
    i = i + 1
mx = num[0]
for v in num:
    if v > mx:
        mx = v
print(mx)