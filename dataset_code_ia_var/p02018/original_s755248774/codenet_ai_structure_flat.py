n = int(input())
li = list(map(int, input().split()))
cnt = 0
i = 0
while i < len(li):
    if li[i] % 2 == 0:
        cnt += 1
    i += 1
print(cnt)