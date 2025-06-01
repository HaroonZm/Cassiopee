while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    a = [int(input()) for _ in range(n)]
    current_sum = sum(a[:k])
    max_sum = current_sum
    for i in range(k, n):
        current_sum += a[i] - a[i - k]
        if current_sum > max_sum:
            max_sum = current_sum
    print(max_sum)