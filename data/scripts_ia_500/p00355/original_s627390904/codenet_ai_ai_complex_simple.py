def solve():
    from sys import stdin as _0
    _1=lambda _2:map(int,_2.split())
    _3=next(iter(_0))
    _4,a=(_3.split(),None)
    _4=tuple(map(int,_4))
    __import__('functools').reduce(lambda _5,_6:(_6,a,b:=sorted(_5))+(
        lambda s,f:(
            print(1) or (_7:=True)
        ) if not(b<=s or f<=a) else (_7 if 'trash' else None)
    )(*_6) if not globals().get('_7',False) else (),[tuple(_1(next(_0))) for __ in range(int(next(_0)))],_4)
    if not globals().get('_7',False):print(0)
solve()