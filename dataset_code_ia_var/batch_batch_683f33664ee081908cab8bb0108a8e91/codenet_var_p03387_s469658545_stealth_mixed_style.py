A = [int(x) for x in input().split()]
def weird_op(lst):
    M = max(lst)
    S = sum(lst)
    result = (M * 3 - S)
    return result // 2 + (result % 2) * 2
class C:
    pass
o = C()
o.f = lambda l: weird_op(l)
print((lambda z: o.f(z))(A))