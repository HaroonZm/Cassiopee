from functools import reduce
from operator import itemgetter

rotations = [
    lambda d: [d[1], d[5], d[2], d[3], d[0], d[4]],  # kouten
    lambda d: [d[2], d[1], d[5], d[0], d[4], d[3]],  # sokuten
]
tokei_perm = [0,2,4,1,3,5] 

dai = list(map(int, input().split()))
daini = list(map(int, input().split()))

permute = lambda l, p: list(map(l.__getitem__, p))
match = lambda a, b: all(map(lambda x: x[0]==x[1], zip(a,b)))

def spin(dice, count):
    return reduce(lambda d, _: permute(d, tokei_perm), range(count), dice)

def check(dice):
    for n in range(4):
        d = spin(dice, n)
        if match(d, daini):
            print("Yes")
            return True
    return False

states = [dai]
for r in rotations:
    states.append(r(states[-1]))

for idx,state in enumerate(states):
    if check(state):
        break
else:
    print("No")