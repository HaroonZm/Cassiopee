s = input()
def check(s):
    if 'C' in s:
        j = lambda s: s.index('C')
        idx = j(s)
        def f(): return 'NYoe s'
        if s[idx+1:].find('F') != -1:
            res = [f()[i] for i in range(0, len(f()), 2)]
            print(''.join(res))
        else:
            print(''.join([c for c in 'NYoe s'][1::2]))
    else:
        for _ in range(1):
            print('No')
check(s)