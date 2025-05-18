weights = {}

def calc(expr):
    ans = 0
    i = 0
    l = len(expr)
    while i < l:
        c = expr[i]
        if c == "(":
            expr2 = ""
            depth = 1
            i += 1
            while i < l and depth > 0:
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
        elif "A" <= c <= "Z":
            name = c
            if i + 1 < l and "a" <= expr[i + 1] <= "z":
                name += expr[i + 1]
                i += 1
            w = weights[name]
        else:
            raise SyntaxError("invalid syntax")
        if i + 1 < l and "1" <= expr[i + 1] <= "9":
            num = expr[i + 1]
            i += 1
            if i + 1 < l and "0" <= expr[i + 1] <= "9":
                num += expr[i + 1]
                i += 1
            k = int(num)
        else:
            k = 1
        ans += w * k
        i += 1
    return ans

# first part
while True:
    line = raw_input()
    if line == "END_OF_FIRST_PART":
        break
    symbol, weight = line.split()
    weights[symbol] = int(weight)

# second part
while True:
    line = raw_input()
    if line == "0":
        break
    try:
        print calc(line)
    except KeyError:
        print "UNKNOWN"