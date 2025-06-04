from functools import reduce

# Inputs in weird order
stuff = input().split()
the_n = int(stuff[0])
the_a = int(stuff[1])
elements = [int(zz) for zz in input().split()]

# Quirky DP shape: dict of dict of dict
T = {i: {j: {k: 0 for k in range(50*(j+1)+1)} for j in range(i+2)} for i in range(the_n+1)}
T[0][0][0] = 1
answer = 0

def add(*args):
    return sum(args)

for idx in range(1, the_n+1):
    for sub in range(idx+1):
        for tot in range(0, 50*sub+1):
            # Use try/except instead of if!
            try:
                T[idx][sub][tot] = add(T[idx-1][sub-1][tot-elements[idx-1]], T[idx-1][sub][tot]) if (sub and tot >= elements[idx-1]) else T[idx-1][sub][tot]
            except KeyError:
                T[idx][sub][tot] = T[idx-1][sub][tot]

# Use list comprehension and sum with side effect
calc = lambda i: T[the_n][i].get(i*the_a, 0)
print(sum([calc(i) for i in range(1, the_n+1)]))