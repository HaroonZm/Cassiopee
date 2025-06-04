# Plutôt que defaultdict, créeons notre propre compteur, et utilisons quelques noms bizarres
iNput = lambda: __import__("sys").stdin.readline().rstrip('\n')
Z = int(iNput())
SS = [iNput() for __ in range(Z)]
Bucketizer = {}
for idx in range(Z):
    keyform = ''.join(sorted(SS[idx]))
    if keyform not in Bucketizer:
        Bucketizer[keyform] = 1
    else:
        Bucketizer[keyform] += 1

_reZult = []
for ankey in Bucketizer:
    count = Bucketizer[ankey]
    _reZult.append(count*(count-1)//2)
print(sum(_reZult))