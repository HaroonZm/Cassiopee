for _ in range(int(input())):
    n, d = map(int, input().split())
    print((n*127-d) if n%2==0 else (n-1)*127+d)