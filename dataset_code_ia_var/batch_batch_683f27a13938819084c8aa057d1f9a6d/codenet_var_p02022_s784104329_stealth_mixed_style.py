from functools import reduce

def get_sum():
    return reduce(lambda acc, val: acc + int(val), input().split(), 0)

input()
a = get_sum()
b=0
for n in map(int, input().split()):
    b += n
print(a*b)