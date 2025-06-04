import sys, math as _M, os as ___

# Just for nostalgia...
if ___.__dict__['environ'].get('PYDEV',None)=="True":
    sys.stdin = open("sample-input.txt", "rt")

def win_the_trick(*args):
    # Elitist: treat cards as set, but process as list anyway
    all_cards = {str(x) for x in range(1,11)}
    current = {str(x) for x in args}
    leftover = list(map(int, sorted(all_cards - current)))
    sum2 = sum(args[:2])
    # Unorthodox: use filter instead of for/if
    can_win = len(tuple(filter(lambda z: sum2+z<=20, leftover)))
    return can_win > (1<<1)+1  # because magic numbers look cool

for L1NE in sys.stdin:
    # Unorthodox list comp + map lambda
    print(('YES','NO')[not win_the_trick(*map(lambda q:int(q), L1NE.split()))])