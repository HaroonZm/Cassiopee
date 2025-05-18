import re

def main():
    s = input()
    d = {}
    n = len(re.findall(r'\w', s))
    for i in range(n):
        a, v = input().split()
        v = int(v)
        d[a] = v

    prog = re.compile(r'\[(\w)-(\w)\]')
    m = prog.search(s)
    while m is not None:
        c1, c2 = m.group(1, 2)
        if d[c1] == d[c2]:
            print('No')
            return 0

        if d[c1] < d[c2]:
            d[c2] -= 1
            s = prog.sub(c2, s, 1)
            if d[c1] != 0:
                print('No')
                return 0
        else:
            d[c1] -= 1
            s = prog.sub(c1, s, 1)
            if d[c2] != 0:
                print('No')
                return 0

        m = prog.search(s)

    if len(s) != 1:
        print('No')
    elif [0 for k, v in d.items() if v]:
        print('No')
    else:
        print('Yes')
    return 0

if __name__ == '__main__':
    main()