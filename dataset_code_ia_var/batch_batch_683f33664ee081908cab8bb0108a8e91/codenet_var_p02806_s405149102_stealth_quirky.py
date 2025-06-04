collect = lambda n: [input().split() for _ in range(n)]
getnum = lambda: int(input())
res = [0]
found = [0]
n = getnum()
data = collect(n)
marker = input()

def process():
    for pair in data:
        k, v = pair
        if found[0]:
            res[0] += int(v)
        if k == marker:
            found[0] = 1

process()
print(res[0])