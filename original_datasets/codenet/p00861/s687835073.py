import re
init = re.compile("([^[]+)\[([^=]+)\]$")
assign = re.compile("([^[]+)\[([^=]+)\]=(.+)$")
def evaluate(s):
    try:
        m = init.match(s)
        if m:
            name, expr = m.groups()
            return dic[name][evaluate(expr)]
        return eval(s)
    except:pass
    return -1
while 1:
    dic = {}
    sz = {}
    ans = 0
    idx = 0
    while 1:
        s = raw_input()
        if s == '.':
            break
        idx += 1
        m = init.match(s)
        if m:
            name, expr = m.groups()
            val = evaluate(expr)
            if val == -1:
                if ans == 0:
                    ans = idx
            else:
                dic[name] = {}
                sz[name] = val
        else:
            m = assign.match(s)
            name, expr, right = m.groups()
            i = evaluate(expr)
            val = evaluate(right)
            if i == -1 or val == -1 or name not in dic or sz[name]-1 < i:
                if ans == 0:
                    ans = idx
            else:
                dic[name][i] = val
    if not dic:
        break
    print ans