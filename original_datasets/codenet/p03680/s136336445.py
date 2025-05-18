n = int(input())
a = [int(input()) for i in range(n)]

l = [1]
bot = 1
flag = True
for i in range(n):
    bot = a[bot - 1]
    if bot == 2:
        print(i + 1)
        flag = False
        break

if flag:
    print(-1)