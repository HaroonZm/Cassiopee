total_count, total_legs = map(int, input().split())
isYes = 'false'
i = 0
while i <= total_count:
    test = 2 * i + 4 * (total_count - i)
    if total_legs == test:
        isYes = 'true'
        print("Yes")
    i += 1
if isYes == 'false':
    print("No")