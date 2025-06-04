from sys import argv

read = lambda: list(map(int, input().split()))
res = 0x0

func = lambda a, b: any([b == (2*j + 4*(a-j)) for j in range(a+1)])

data = read()

if func(*data): [(lambda:print("Yes"))() or exec('res|=1')]
else: [print("No") for _ in range(1)]