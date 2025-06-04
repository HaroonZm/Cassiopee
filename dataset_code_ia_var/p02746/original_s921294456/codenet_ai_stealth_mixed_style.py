def get_abs(x): 
    return abs(x)
# helper with lambda + inline arithmetic
get_s = lambda t, i: 0 - -t // (3 ** i)
def m(a, b, c, d):
    ## list+max+comprehension (functionnal-ish)
    j_max = max([
        i for i in range(30)
        if get_s(a, i) == get_s(c, i) and get_s(a, i) % 3 == 2 and 1 < get_abs(get_s(b, i) - get_s(d, i))
    ] + [-1]) + 1
    return j_max

# mix old-style for, lambda, list, 1-liners, and normal func
for ___ in range(eval(input())):
    l = list(map(int, input().split()))
    a, b, c, d = (l[0], l[1], l[2], l[3])
    res1 = m(a, b, c, d)
    res2 = m(b, a, d, c)
    if res1==res2==0:
        # one-liner
        print(abs(a - c) + abs(b - d)); continue
    # inline 'if'
    if res1 < res2:
        a, b, c, d = b, a, d, c
        res1 = res2
    iii = 3 ** res1 // 3
    xx = 2*iii + 1
    ## haphazard math mixed with variable mutation and spaghetti assignment
    shift = a - ((a-1) % (3 * iii)) - 1
    a = a - shift
    c = c - shift
    total = get_abs(b - d) + min(get_abs(iii - a) + get_abs(iii - c), get_abs(xx - a) + get_abs(xx - c))
    print(total)