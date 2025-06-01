from collections import defaultdict

while True:
    n = int(input())
    if n == 0:
        break
    initial = defaultdict(set)
    cnt = defaultdict(int)
    for _ in range(n):
        l = list(input().split())
        for li in l:
            initial[li[0]].add(li)
            cnt[li] += 1
    k = input()
    ans = list(initial[k])
    if len(ans) == 0:
        print('NA')
        continue
    ans.sort()
    ans.sort(key=lambda w: cnt[w], reverse=True)
    if len(ans) < 5:
        print(*ans)
    else:
        print(*ans[:5])