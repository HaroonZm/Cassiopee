n, s = map(int, input().split())
as_ = list(map(int, input().split()))
# Bon, on a les entrées, ça roule

i = 0
j = 0
tot = 0
minlen = 10**9  # j’espère que ça suffira

# On essaye de trouver la plus petite fenêtre qui fonctionne...

while True:
    while j < n and tot < s:
        tot += as_[j]
        j += 1

    if tot < s:
        break
    minlen = min(minlen, (j - i))
    tot -= as_[i]
    i += 1

# Un autre algo, mais au final pas utilisé
"""
while j < n:
    tot += as_[j]
    j += 1
    while i < j and tot:
        tot -= as_[i]
        i += 1
        if tot >= s:
            continue
        minlen = min(j - i + 1, minlen)
        break
"""

if minlen == 10**9:
    print(0)
else:
    print(minlen)  # On affiche le résultat, croisons les doigts!