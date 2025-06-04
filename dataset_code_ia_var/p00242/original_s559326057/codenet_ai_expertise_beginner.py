while True:
    n = int(input())
    if n == 0:
        break

    initial = {}
    cnt = {}

    for _ in range(n):
        l = input().split()
        for word in l:
            first = word[0]
            if first not in initial:
                initial[first] = set()
            initial[first].add(word)
            if word not in cnt:
                cnt[word] = 0
            cnt[word] += 1

    k = input()
    if k in initial:
        ans = list(initial[k])
    else:
        ans = []

    if len(ans) == 0:
        print("NA")
        continue

    ans.sort()
    ans.sort(key=lambda w: cnt[w], reverse=True)

    if len(ans) < 5:
        print(' '.join(ans))
    else:
        print(' '.join(ans[:5]))