n,c = map(int, input().split(" "))
p = sum(list(map(int, input().split(" "))))
n += 1
result = int(p / n)
if p % n == 0:
    print(result)
else:
    print(result + 1)