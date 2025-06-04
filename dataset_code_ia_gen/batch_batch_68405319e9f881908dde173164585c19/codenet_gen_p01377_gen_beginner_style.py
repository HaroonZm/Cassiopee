s = input()

def is_palindrome_candidate(c1, c2):
    # Retourne vrai si c1 et c2 peuvent former un couple symétrique sans substitution
    pairs = [('i','i'), ('w','w'), ('(',')'), (')','(')]
    return (c1, c2) in pairs

def cost_to_match(c1, c2):
    # Calcule le coût minimal pour rendre c1 et c2 symétriques par substitution
    pairs = [('i','i'), ('w','w'), ('(',')'), (')','(')]
    if c1 == c2 and (c1 == 'i' or c1 == 'w'):
        return 0
    if (c1, c2) in pairs:
        return 0
    # Sinon, il faut au moins une substitution. On essaie toutes combinaisons possibles.
    chars = ['i','w','(',')']
    min_cost = 2  # On peut changer les deux caractères au max
    for a in chars:
        for b in chars:
            if (a,b) in pairs or (a==b and (a=='i' or a=='w')):
                cost = 0
                if c1 != a:
                    cost +=1
                if c2 != b:
                    cost +=1
                if cost < min_cost:
                    min_cost = cost
    return min_cost

n = len(s)
res = 0
for i in range(n // 2):
    res += cost_to_match(s[i], s[n-1 - i])

# Si la longueur est impaire, vérifier que le milieu est i ou w, sinon 1 substitution
if n %2 ==1:
    mid = s[n//2]
    if mid != 'i' and mid != 'w':
        res +=1

print(res)