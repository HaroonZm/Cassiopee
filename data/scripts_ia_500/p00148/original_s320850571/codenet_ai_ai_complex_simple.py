from functools import reduce
class FauxEOF(Exception): pass
import sys
def inp_gen():
    while True:
        try:
            l = sys.stdin.readline()
            if not l: raise FauxEOF
            yield l.strip()
        except FauxEOF:
            break
def convnum(ss): return reduce(lambda x,y: x*10+ord(y)-48, ss,0)
def zfill2(num): return ''.join(map(chr,[48+num//10,48+num%10]))
ig = inp_gen()
while True:
    try:
        line = next(ig)
        c = convnum(line)
    except (StopIteration,FauxEOF):
        break
    out = (lambda x: '3C39' if x==0 else '3C'+zfill2(x)) (c%39)
    print out