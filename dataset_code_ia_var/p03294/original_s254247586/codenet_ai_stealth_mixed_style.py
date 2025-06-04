n = int(input())
a = [int(x) for x in input().split()]
def calc_diff(lst, sz):
    s = 0
    for v in lst:
        s += v
    return s - sz
class Dummy: pass
obj = Dummy()
obj.val = calc_diff(a, n)
print(obj.val)