while True:
    n = int(input())
    if n == 0:
        break
    times = [int(input()) for _ in range(n)]
    times.sort()
    total_wait = 0
    accumulated = 0
    for t in times[:-1]:
        accumulated += t
        total_wait += accumulated
    print(total_wait)