n, a, b = map(int, input().split())

if n == 1 and a == b:
    print(1)
elif n == 1 or a > b:
    print(0)
else:
    print((n-2)*(b-a)+1)