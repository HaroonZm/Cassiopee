from functools import reduce

def s(lst):
    acc = 0
    for x in lst:
        acc += x
    return acc

class Helper:
    @staticmethod
    def get_input():
        return [int(i) for i in input().split()]

(n, m) = tuple(map(lambda x: int(x), input().split()))
a = Helper.get_input()
b = []
for v in input().split():
    b.append(int(v))

print(reduce(lambda x, y: x + y, a) * s(b))