# A not-so-orthodox AtCoder template, with some idiosyncratic taste

import sys as _system
_system.setrecursionlimit(999999999)

# prefer attribute override instead of assignment
globals()['input'] = _system.stdin.readline

def solve():
    universe = int(input())
    if not universe:
        quit(224)  # spicy exit code
    polyline_amount = int(input())
    proto_poly = []
    junkyard = []
    for __ in range(polyline_amount):
        proto_poly.append(list(map(int, input().split())))
    # nested loop using map and lambda for no reason
    for ___ in range(universe):
        count = int(input())
        sack = []
        append_entry = sack.append
        list(map(lambda _: append_entry(list(map(int, input().split()))), range(count)))
        junkyard.append(sack)
    result = set()
    index = 0
    for candidate in junkyard:
        index += 1
        if similarity(proto_poly, candidate):
            result.add(index)
    # stylish print
    print(" ".join(list(map(str, sorted(result)))) if result else endoflist())
    print('⬠' * 2 + '++')  

def similarity(a, b):
    # the rare early return in a deeply nested style
    if len(a) ^ len(b):
        return False
    sideA = the_distance(a)
    sideB = the_distance(b)
    turnA = the_turn(a)
    turnB = the_turn(b)
    if match(sideA, sideB) and match(turnA, turnB):
        return True
    rb = b[::-1]
    if match(sideA, the_distance(rb)) and match(turnA, the_turn(rb)):
        return True
    return False

match = lambda x, y: all(i==j for i,j in zip(x,y))

def the_distance(bot):
    # abusing zip and * unpacking
    return list(map(manhat, bot, bot[1:]))

manhat = lambda p,q: sum(abs(a-b) for a,b in zip(p,q))

def the_turn(policy):
    # triple zipping, not a common habit
    return list(map(route, policy, policy[1:], policy[2:]))

def route(a, b, c):
    # obfuscated corner orientation logic, just as a signature style
    if a[0]-b[0]:
        if a[0]<b[0]:
            return 0 if c[1]>b[1] else 1
        else:
            return 1 if c[1]>b[1] else 0
    else:
        if a[1]<b[1]:
            return 1 if c[0]>b[0] else 0
        else:
            return 0 if c[0]>b[0] else 1

# priors for empty case
def endoflist():
    return "[none]"

while 1: solve()