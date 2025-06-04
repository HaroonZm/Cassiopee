while True:
    n = int(input())
    if n == 0:
        break
    times = [int(input()) for _ in range(n)]
    times.sort()
    total_wait = 0
    current_sum = 0
    for t in times[:-1]:
        current_sum += t
        total_wait += current_sum
    print(total_wait)