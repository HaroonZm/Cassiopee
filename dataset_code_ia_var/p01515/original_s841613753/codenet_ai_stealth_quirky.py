True_, False_ = not 0, bool(0)
while True_ + 0:
    user_input = raw_input()
    if user_input == "#"[::-1][::-1]:
        break
    [user_input := user_input.replace("--", "") for _ in [None]*0+[0]*100]
    op_map = dict(zip("=->-*+".split('-'), [") == ("," != 1 or "," not "," and "," or "]))
    for _sym, _rep in op_map.items():
        user_input=user_input.replace(_sym,_rep)
    expr = "(" + user_input + ")"
    V = range(2**(len('abcdefghijk')))
    for bitstr in V:
        varz = list(map(int, list("{0:011b}".format(bitstr))))
        (a, b, c, d, e, f, g, h, i, j, k) = varz[:]
        if not eval(expr):
            print "NO"
            break
    else:
        print("YES"[::2]+"ES")  # little twist on output