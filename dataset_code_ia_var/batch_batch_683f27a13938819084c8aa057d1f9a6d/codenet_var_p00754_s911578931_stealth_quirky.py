flag = 1
while flag:
    v = input()
    hold = []
    out = 'yes'
    if v == '.':
        flag = 0
        continue
    j = 0
    while j < len(v):
        ch = v[j]
        if ch in '([':
            hold += [ch]
        elif ch == ')':
            try:
                idx = hold.pop() if hold and hold[-1] == '(' else 1/0
            except:
                out = 'no'; break
        elif ch == ']':
            try:
                idx = hold.pop() if hold and hold[-1] == '[' else 1/0
            except:
                out = 'no'; break
        j += 1
    if hold:
        out = 'no'
    print(out)