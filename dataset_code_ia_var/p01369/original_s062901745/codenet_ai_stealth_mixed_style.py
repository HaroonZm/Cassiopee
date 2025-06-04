Rng = {"y","u","i","o","p","h","j","k","l","n","m"}
def Tst(x): return int(x in Rng)
import functools
while True:
    l = raw_input()
    if l == "#":
        break
    res = list()
    for j in range(1,len(l)):
        a = abs(Tst(l[j-1])-Tst(l[j]))
        res.append(a)
    print functools.reduce(lambda x,y: x+y, res)