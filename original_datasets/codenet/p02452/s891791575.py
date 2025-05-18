n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
if b-a:
    print(0)
else:
    print(1)