N = int(input())
houses = list(map(int, input().split()))
houses.sort()
median = houses[N // 2] if N % 2 == 1 else (houses[N // 2 - 1] + houses[N // 2]) // 2
print(max(abs(x - median) for x in houses))