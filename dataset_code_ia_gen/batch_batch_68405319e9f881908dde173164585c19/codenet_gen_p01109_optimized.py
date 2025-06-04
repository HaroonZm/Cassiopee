import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    incomes = list(map(int, input().split()))
    total = sum(incomes)
    count = sum(1 for x in incomes if x * n <= total)
    print(count)