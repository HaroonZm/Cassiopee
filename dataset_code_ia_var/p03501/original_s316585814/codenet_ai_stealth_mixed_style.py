def get_values():
    return list(map(int, input().split()))
class C:
    calc = staticmethod(lambda t, a, b: print((lambda x, y: y if x>y else x)(a*t, b)))
for _ in [0]:
    t, a, b = get_values()
    C.calc(t, a, b)