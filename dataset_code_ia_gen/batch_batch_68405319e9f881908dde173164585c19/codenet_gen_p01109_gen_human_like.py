while True:
    n = int(input())
    if n == 0:
        break
    incomes = list(map(int, input().split()))
    avg = sum(incomes) / n
    count = sum(1 for income in incomes if income <= avg)
    print(count)