N = int(input())
friends = [tuple(map(int, input().split())) for _ in range(N)]

max_friends = 0
for x in range(1, N+2):  # 親も含めた人数なので最大はN+1
    count = 0
    for a, b in friends:
        if a <= x <= b:
            count += 1
    if count >= x - 1:  # 友だちの人数 = 総人数 - 1(親)
        if x - 1 > max_friends:
            max_friends = x - 1

print(max_friends)