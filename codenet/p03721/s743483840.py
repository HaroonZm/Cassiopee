n , k= map(int, input().split())
ab = []

for i in range(n):
    ab.append(list(map(int, input().split())))

ab = sorted(ab)

count = 0
for i in range(n):
    count += ab[i][1]
    if count >= k:
        print(ab[i][0])
        exit()