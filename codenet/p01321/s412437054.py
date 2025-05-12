while 1:
    n = int(input())
    if n == 0:
        break
    total = []
    for i in range(n):
        score = input().split()
        sum = 0
        for s in score:
            sum += int(s)
        total.append(sum)
    print(max(total), min(total))