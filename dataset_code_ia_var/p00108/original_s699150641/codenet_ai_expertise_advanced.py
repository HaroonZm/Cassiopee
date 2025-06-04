from collections import Counter

while True:
    n = int(input())
    if n == 0:
        break
    seq = list(map(int, input().split()))
    prev = seq[:]
    cnt = 0
    while True:
        freq = Counter(prev)
        curr = [freq[x] for x in prev]
        if curr == prev:
            break
        prev = curr
        cnt += 1
    print(cnt)
    print(*prev)