while True:
    K = int(input())
    if K == 0:
        break
    numbers = list(map(int, input().split()))
    total = sum(numbers)
    result = total // (K - 1)
    print(result)