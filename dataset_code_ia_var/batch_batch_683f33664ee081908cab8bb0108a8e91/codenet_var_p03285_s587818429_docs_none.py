n = int(input())
cnt = 0
for i in range(25):
    for j in range(14):
        if 4 * i + 7 * j == n:
            cnt += 1
if cnt == 0:
    print('No')
else:
    print('Yes')