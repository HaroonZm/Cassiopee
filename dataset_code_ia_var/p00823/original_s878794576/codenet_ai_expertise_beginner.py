weights = {}

def calc(expr):
    ans = 0
    i = 0
    while i < len(expr):
        c = expr[i]
        if c == "(":
            depth = 1
            expr2 = ""
            i += 1
            while i < len(expr) and depth > 0:
                c2 = expr[i]
                if c2 == "(":
                    depth += 1
                elif c2 == ")":
                    depth -= 1
                if depth == 0:
                    break
                expr2 += c2
                i += 1
            if depth > 0:
                raise SyntaxError("invalid syntax")
            w = calc(expr2)
        elif c.isupper():
            name = c
            if i+1 < len(expr) and expr[i+1].islower():
                name += expr[i+1]
                i += 1
            if name in weights:
                w = weights[name]
            else:
                raise KeyError
        else:
            raise SyntaxError("invalid syntax")
        k = 1
        if i+1 < len(expr) and expr[i+1].isdigit() and expr[i+1] != "0":
            num = expr[i+1]
            i += 1
            if i+1 < len(expr) and expr[i+1].isdigit():
                num += expr[i+1]
                i += 1
            k = int(num)
        ans += w * k
        i += 1
    return ans

while True:
    line = raw_input()
    if line == "END_OF_FIRST_PART":
        break
    items = line.split()
    symbol = items[0]
    weight = int(items[1])
    weights[symbol] = weight

while True:
    line = raw_input()
    if line == "0":
        break
    try:
        print calc(line)
    except KeyError:
        print "UNKNOWN"