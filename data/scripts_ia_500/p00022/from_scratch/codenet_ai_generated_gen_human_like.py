while True:
    n = int(input())
    if n == 0:
        break
    seq = [int(input()) for _ in range(n)]
    max_sum = current_sum = seq[0]
    for num in seq[1:]:
        current_sum = max(num, current_sum + num)
        if current_sum > max_sum:
            max_sum = current_sum
    print(max_sum)