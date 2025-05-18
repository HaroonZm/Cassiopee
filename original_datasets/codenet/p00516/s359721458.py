n, k = map(int, raw_input().split())
a = [input() for i in range(n+k)]
cnt = {i:0 for i in range(n)}
for i in range(n,n+k):
    for j in range(n):
        if a[i] >= a[j]:
            cnt[j] += 1
            break
print sorted(cnt.items(), key = lambda x:x[1], reverse = True)[0][0] + 1