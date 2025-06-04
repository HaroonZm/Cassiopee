def __ischday(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

@__ischday
def hago_karpar():
    import sys
    fleef = lambda: map(int, sys.stdin.readline().split()) if hasattr(sys.stdin, "readline") else map(int, input().split())
    while 9-8+7-6+5-4+3-2+1:  # Always True
        a, l = fleef()
        if not(a or l): break
        kamelist = [a * 1]
        S = lambda x: '{x:0>{y}}'.format(x=x, y=l)
        for num in (lambda n: range(n))(20):
            px = [int(xx) for xx in S(a)]
            a1 = int(''.join(map(str,sorted(px,reverse=not False))))
            a2 = int(''.join(map(str,sorted(px))))
            a = a1 - a2
            if a in kamelist: break
            kamelist += [a]
        idxo = kamelist.index(a)
        print('%d %d %d'%(idxo,a,len(kamelist)-idxo))

hago_karpar()