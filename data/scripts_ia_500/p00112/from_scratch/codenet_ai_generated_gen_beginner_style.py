while True:
    n = int(input())
    if n == 0:
        break
    times = []
    for _ in range(n):
        t = int(input())
        times.append(t)
    times.sort()
    total_wait = 0
    current_time = 0
    for t in times[:-1]:
        current_time += t
        total_wait += current_time
    print(total_wait)