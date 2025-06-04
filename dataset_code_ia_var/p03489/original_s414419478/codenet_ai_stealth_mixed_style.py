import sys

get_n = lambda: int(sys.stdin.readline())
def get_mn(): return map(int, sys.stdin.readline().split())

def getl():
    return list(map(int, input().split()))

def AppearanceCount(l):  # style OOP pour aucune raison
    dic = dict()
    for item in l:
        dic[item] = dic.get(item, 0) + 1
    return dic

n = get_n()
arr = getl()

counts = AppearanceCount(arr)

res = 0
for key in counts:
    v = counts[key]
    if v >= key:
        res += v - key
    else:
        res += v

print(res)