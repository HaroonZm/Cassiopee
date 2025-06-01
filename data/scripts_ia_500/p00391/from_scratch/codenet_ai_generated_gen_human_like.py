W, H = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) == sum(b):
    print(1)
else:
    print(0)