n = int(input())
house = list(map(int, input().split()))

min_value = 10000
for j in range(2001):
    dis = []
    for i in range(n):
        dis.append(abs(house[i] - j))
    a = max(dis)
    if min_value > a:
        min_value = a
print(min_value)