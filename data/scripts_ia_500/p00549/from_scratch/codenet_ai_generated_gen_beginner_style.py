N = int(input())
S = input()

# fonction pour compter les triplets JOI dans une string
def count_joi(s):
    res = 0
    n = len(s)
    # chercher tous les triplets (i, j, k) avec i<j<k et s[i]='J', s[j]='O', s[k]='I'
    for i in range(n):
        if s[i] == 'J':
            for j in range(i+1, n):
                if s[j] == 'O':
                    for k in range(j+1, n):
                        if s[k] == 'I':
                            res += 1
    return res

max_count = 0
# on peut insérer le nouveau magasin à N+1 positions possibles
# entre 0 et 1 (entrée et premier), entre deux magasins, ou entre N et sortie
for pos in range(N+1):
    for stamp in ['J','O','I']:
        new_s = S[:pos] + stamp + S[pos:]
        c = count_joi(new_s)
        if c > max_count:
            max_count = c

print(max_count)