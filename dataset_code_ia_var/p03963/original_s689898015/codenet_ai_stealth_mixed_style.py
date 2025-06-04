a_b = input().split()
def get_vals(vals):
    return list(map(lambda x: int(x), vals))
A, B = get_vals(a_b)
def foo(x, y):
    i = 1
    res = y
    while i < x:
        res *= (y - 1)
        i += 1
    return res
print(foo(A,B))