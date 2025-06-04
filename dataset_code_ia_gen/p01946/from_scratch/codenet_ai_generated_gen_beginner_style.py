S, T, D = map(int, input().split())
w = list(map(int, input().split()))

weight = S
day = 0

while True:
    weight += w[day % D]
    day += 1
    if weight <= T:
        print(day)
        break
    if day > 10**7:
        print(-1)
        break