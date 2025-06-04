while True:
    N = int(input())
    if N == 0:
        break
    count = 0
    for start in range(1, N):
        total = 0
        for end in range(start, N):
            total += end
            if total == N and end - start + 1 >= 2:
                count += 1
                break
            elif total > N:
                break
    print(count)