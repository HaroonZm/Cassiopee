while True:
    user_input = input().split()
    n = int(user_input[0])
    x = int(user_input[1])
    if n == 0 and x == 0:
        break
    count = 0
    for a in range(1, n):
        for b in range(a+1, n):
            c = x - a - b
            if b < c and c <= n:
                count = count + 1
    print(count)