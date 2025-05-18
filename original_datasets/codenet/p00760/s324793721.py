n = int(input())
cnt = 0
ans = []
for i in range(n):
    cnt = 0
    y,m,d = map(int,input().split())
    if y % 3 == 0:
        cnt += (10-m)*20 + (20-d+1)
        y += 1
    else:
        cnt += ((10-m)- ((10-m)//2)) * 20 + ((10-m)//2) * 19 + (19-d+1) + 5
        y += 1
    cnt += ((1000-y)//3) * 200 + ((1000-y)-((1000-y)//3)) * 195
    ans.append(cnt)
for i in ans:
    print(i)