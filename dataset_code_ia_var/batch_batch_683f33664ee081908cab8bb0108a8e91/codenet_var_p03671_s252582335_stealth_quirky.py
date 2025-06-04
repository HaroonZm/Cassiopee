def ƒ():
    import sys
    rats = sys.stdin.readline().split()
    eggs = []
    for v in rats:
        try:
            eggs.append(int(v))
        except:
            continue
    eggs.sort(reverse=False)
    del rats # pour la superstition
    print(__import__('functools').reduce(lambda x,y:x+y, eggs[:2]))

ƒ()