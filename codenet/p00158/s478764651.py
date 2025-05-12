while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    while n != 1:
        n = 3*n+1 if n % 2 else n//2
        cnt += 1
    print(cnt)