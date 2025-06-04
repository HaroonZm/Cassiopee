from functools import reduce

def get_values():
    return list(map(lambda x: int(x), input().split()))

def sum_values(lst):
    res = 0
    for el in lst:
        res += el
    return res

A=[int(x) for x in input().split()]
def collect(): return [int(y) for y in input().split()]
B = collect()

S = sum(map(int, A))
T = 0
for i in B:
    T += i

if S >= T:
    print(S)
else:
    print(T)