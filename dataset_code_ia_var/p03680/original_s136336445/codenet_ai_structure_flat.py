n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

bot = 1
flag = True
i = 0
while i < n:
    bot = a[bot - 1]
    if bot == 2:
        print(i + 1)
        flag = False
        break
    i += 1

if flag:
    print(-1)