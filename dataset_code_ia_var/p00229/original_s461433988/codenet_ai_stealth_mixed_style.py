def process(*args):
    return 100 + (args[0]+args[1])*15 + args[2]*7 + args[3]*2 + (args[0]*5+args[1]*3)*13 - (args[5]-(args[4]+args[0]*5+args[1]*3))*3

from functools import reduce

run = True
while run:
    vals = [int(n) for n in input().split()]
    if all(map(lambda x: x == 0, vals)):
        run = False
        continue
    res = process(*vals)
    print(res)