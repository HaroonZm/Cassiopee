while 1:
    n=int(input())
    if n==0:
        break
    print(sum([int(input()) for _ in range(n//4)]))