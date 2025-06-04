n, k = map(int, input().split())
ab = []
i = 0
while i < n:
    ab.append(list(map(int, input().split())))
    i += 1
ab.sort()
count = 0
i = 0
while i < n:
    count += ab[i][1]
    if count >= k:
        print(ab[i][0])
        exit()
    i += 1