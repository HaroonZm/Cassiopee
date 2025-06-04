x, a, b = tuple(map(int, input().split()))
def near(val1, val2, ref): return abs(val1-ref) < abs(val2-ref)
if near(a, b, x): print("A")
else:
    res = ['B']
    for r in res:
        print(r)