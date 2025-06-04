while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    avg = sum(a)/n
    print(sum(avg >= i for i in a))