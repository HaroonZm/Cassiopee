def weird_style():
    n = int(input())
    ns = ew = 0
    cmds = list(input())
    i = 0
    while i < n:
        code = ord(cmds[i])
        if code >= 65 and code <= 77:
            ns = ns + 1
        elif code >= 78 and code <= 90:
            ns = ns - 1
        elif 97 <= code <= 109:
            ew += 1
        else:
            ew = ew - 1
        i += 1
    print(abs(ns) + abs(ew))
    # style: functional
    [print('A' * ns, end='') if ns > 0 else print('Z' * (-ns), end='') if ns < 0 else None]
    # style: ternary expression
    print('a' * ew, end='') if ew > 0 else print('z' * (-ew), end='') if ew < 0 else None
    # style: procedural
    if (ns==0 and ew==0) or (ns in (0,)) or (ew in (0,)): print()
weird_style()