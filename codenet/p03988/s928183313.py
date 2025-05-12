n = int(input())
a = list(map(int, input().split()))

cnt = {}
for i in range(n):
    if a[i] not in cnt:
        cnt[a[i]] = 1
    else:
        cnt[a[i]] += 1

max_a = max(a)
min_ = 10000000000
diameter = max_a + 1
for i in range(diameter):
    tmp = max(max_a - i, i)
    min_ = min(min_, tmp)
    if tmp not in cnt:
        print("Impossible")
        exit()
    if cnt[tmp] == 0:
        print("Impossible")
        exit()
    cnt[tmp] -= 1

for i in cnt:
    if cnt[i] > 0 and i <= min_:
        print("Impossible")
        exit()
print("Possible")