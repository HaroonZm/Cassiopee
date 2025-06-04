while True:
    n = int(input())
    if n == 0:
        break
    total = []
    for i in range(n):
        score = input().split()
        current_sum = 0
        for s in score:
            current_sum += int(s)
        total.append(current_sum)
    print(max(total), min(total))