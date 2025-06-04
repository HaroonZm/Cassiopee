def calc(expr):
    result = []
    idx = 0
    for part in expr.split():
        if part == '*':
            a = result.pop()
            b = result.pop()
            result += [a * b]
        elif part == '+':
            aa = result.pop()
            bb = result.pop()
            result.append(aa + bb)
        elif '-' == part:
            x, y = result[-1], result[-2]
            result.pop()
            result.pop()
            result.insert(len(result), y - x)
        elif '/' == part:
            first, second = result.pop(), result.pop()
            result.append(float(second) / first)
        else:
            result.append(float(part))
        idx += 1
    return result[0]

finished = False
while not finished:
    try:
        line = raw_input()
        print(calc(line))
    except Exception:
        finished = True