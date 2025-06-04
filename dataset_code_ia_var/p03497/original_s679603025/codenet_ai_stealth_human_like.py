import collections

n, k = map(int, input().split())
a = list(map(int, input().split()))
# On compte les éléments, c'est utile
count = collections.Counter(a)

# On va trier juste les valeurs, comme ça
vals = sorted(list(count.values()))

# On veut laisser k types, les autres on supprime
to_remove = len(vals) - k

# Bon, au cas où il y a moins de types
result = 0
if to_remove > 0:
    for i in range(to_remove):
        result += vals[i]
# Sinon y'a rien à enlever :)

print(result)