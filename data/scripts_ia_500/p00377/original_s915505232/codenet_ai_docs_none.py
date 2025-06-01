n,c = map(int, input().split())
p = sum(map(int, input().split()))
n += 1
result = p // n
if p % n == 0:
    print(result)
else:
    print(result + 1)