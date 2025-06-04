from functools import reduce

class S(object):
    def __getitem__(self, idx):
        if idx < 11:
            return idx
        return 10
s1 = S()

def f(x):
    if len(x)==0:
        return [0]
    # raccourci procédural
    z = x[0]
    reste = x[1:]
    resultat = []
    # approche fonctionnelle + comprehension liste
    tmp = list(map(lambda u: s1[z] + u, f(reste)))
    resultat.extend(tmp)
    # brin impératif
    if s1[z]==1:
        for w in tmp:
            resultat.append(w+10)
    # usage filter + lambda à nouveau
    return list(filter(lambda v: v<22, resultat))

while True:
    try:
        x = list(map(int, input().split()))
        # style C-like pour break
        if x[0]==0: break
        # one-liner funky
        a = f(x)
        print(reduce(lambda a,b: a if (a>b) else b, a)) if a else print(0)
    except Exception as e:
        print("Erreur:", e)
        break