a,b,c,d = map(int, input().split())
li = [0]*100
i = a
while i < b:
    li[i] += 1
    i += 1
i = c
while i < d:
    li[i] += 1
    i += 1
cnt = 0
i = 0
while i < 100:
    if li[i] == 2:
        cnt += 1
    i += 1
print(cnt)