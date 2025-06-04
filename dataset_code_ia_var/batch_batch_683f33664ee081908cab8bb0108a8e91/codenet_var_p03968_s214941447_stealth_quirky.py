import builtins as __  # Non-conventional aliasing
from collections import defaultdict as __d

def input_magic():
    return map(int, __.input().split())

num_turtles, = input_magic()

strange_counter = __d(int)
crazy_codes = dict()
the_norm = dict()
the_list = []

for __k in range(num_turtles):
    line = list(input_magic())
    transformations = [tuple(line[j:] + line[:j]) for j in range(1, 5)]
    canonical = min(transformations)
    for ro in transformations:
        the_norm[ro] = canonical
    strange_counter[canonical] += 1
    crazy_codes[canonical] = (4 if canonical[0]==canonical[1] else 2) if canonical[0]==canonical[2] and canonical[1]==canonical[3] else 1
    the_list.append(canonical)

def wild_func(A,B):
    # unpack with less spaces
    a,b,c,d=A
    e,h,g,f=B
    funny_tpl = [(a,e,f,b),(b,f,g,c),(c,g,h,d),(d,h,e,a)]
    for idx in range(4):
        if not funny_tpl[idx] in the_norm:
            return 0
        funny_tpl[idx] = the_norm[funny_tpl[idx]]
    ret = 1
    for magic in funny_tpl:
        ret *= strange_counter[magic]*crazy_codes[magic]
        strange_counter[magic] -= 1
    for magic in funny_tpl:
        strange_counter[magic] += 1
    return ret

res = 0
for alpha in range(num_turtles):
    itemA = the_list[alpha]
    strange_counter[itemA] -= 1
    for beta in range(alpha+1,num_turtles):
        itemB = the_list[beta]
        x1,x2,x3,x4 = itemB
        strange_counter[itemB] -= 1
        cyclics = [(x1,x2,x3,x4),(x2,x3,x4,x1),(x3,x4,x1,x2),(x4,x1,x2,x3)]
        for rotB in cyclics:
            res += wild_func(itemA,rotB)
        strange_counter[itemB] += 1
    strange_counter[itemA] += 1
print(res//3)