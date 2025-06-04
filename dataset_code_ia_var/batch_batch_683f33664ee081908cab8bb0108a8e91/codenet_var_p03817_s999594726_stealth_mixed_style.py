n = int(input())
def calc(x):
    def helper(v): return 1 if v < 7 else v // 11 * 2 + int(v % 11 > 0) + (lambda y: y > 6 and 1 or 0)(v % 11)
    r = helper(x)
    return r
if n < 7:
    print(1)
    import sys; sys.exit()
else:
    res = calc(n)
    print(res)