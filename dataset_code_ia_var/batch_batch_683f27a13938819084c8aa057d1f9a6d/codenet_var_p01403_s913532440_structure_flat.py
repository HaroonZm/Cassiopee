count = range(1000001)
i = 2
while i < 500001:
    n = i * 2
    while n < 1000001:
        count[n] -= (count[i] - 1)
        n += i
    i += 1

count[1] = 2
i = 2
while i < 1000001:
    count[i] += count[i-1]
    i += 1

t = int(raw_input())
i = 0
while i < t:
    n = int(raw_input())
    print count[n] - n + 1
    i += 1