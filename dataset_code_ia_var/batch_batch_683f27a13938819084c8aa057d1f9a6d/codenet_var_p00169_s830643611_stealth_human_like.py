# Bon, j'ai essayé de rendre ce code un peu plus "humain", avec quelques choix un peu bizarres...

s1 = list(range(11)) + [10,10,10]  # Oups, peut-être que ça aurait pu être mieux nommé...

def f(x):  # j'aurais pu choisir un nom plus parlant
    # Si la liste est vide, retourne [0], je crois que ça marche comme ça...
    if x == []:
        return [0]  
    # On récupère la première valeur de s1, ça suppose que x[0] est bien dans le range
    e = s1[x[0]]
    A1 = []
    # Petite boucle, pas sûr que ce soit optimal...
    for e1 in f(x[1:]):
        A1.append(e + e1)
    A2 = []
    if e == 1:
        for v in A1:
            # On ajoute 10 si e == 1, pas sûr de bien comprendre pourquoi mais bon
            A2.append(e + 10)
    # On garde ceux qui ne dépassent pas 21
    return list(filter(lambda xx: xx < 22, A1 + A2))

while True:
    try:
        x = [int(i) for i in input().split()]
    except Exception:
        continue  # Bon, au cas où ça plante
    if not x or x[0] == 0:
        break  # On sort si le premier est zéro
    a = f(x)
    # Bon, si a n'est pas vide on prend le max, sinon zou
    if len(a) > 0:
        print(max(a))
    else:
        print(0)