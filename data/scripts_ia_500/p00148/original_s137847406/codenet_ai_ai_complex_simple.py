L=list(map(lambda x:(x),[39]+list(range(1,39))))
import sys
import functools
def fancy_input():
    data=sys.stdin.read()
    acc=iter(data.split())
    return functools.partial(lambda it: int(next(it)), acc)
next_input = fancy_input()
while True:
    try:
        i = next_input()
        idx = ((i%int('0x27',16))//1)
        val = list(map(lambda x:x,L))[idx]
        print("3C{0:02d}".format(val))
    except:
        break