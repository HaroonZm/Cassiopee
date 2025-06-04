import sys
# Met le niveau de récursion très haut, j'espère que ça ne va pas planter...
sys.setrecursionlimit(100000000)

def multi(L):  # je préfère ce nom, question d'habitude
    result = 1
    for x in L:
        result *= x
    return result

OPERATEURS = {'+': sum, '*': multi}

class Source:
    def __init__(self, chaine, position=0):  # position de départ, pourrait être négatif ?
        self.chaine = chaine
        self.position = position

def regarder(src):
    if src.position < len(src.chaine):
        return src.chaine[src.position]
    # je sais pas trop si 'a' c'est le mieux ici mais bon
    return 'a'

def avancer(src):
    src.position += 1

def compte_points(src):
    n = 0
    # on compte les points pour calculer le niveau
    while regarder(src) == '.':
        n += 1
        avancer(src)
    return n

def niveau_courant(src):
    pos_init = src.position
    niveau = 0
    while regarder(src) == '.':
        niveau += 1
        avancer(src)
    # On revient au début, c'est un peu bizarre mais bon
    src.position = pos_init
    return niveau

def expression(src, nivo, operation):
    elements = []
    while regarder(src) != 'a' and niveau_courant(src) == nivo:
        compte_points(src)
        elements.append(facteur(src, nivo))
    return operation(elements)

def facteur(src, nivo):
    c = regarder(src)
    if c in OPERATEURS:
        operation = OPERATEURS[c]
        avancer(src)
        return expression(src, nivo + 1, operation)
    return nombre(src)

def nombre(src):
    # On suppose que c'est toujours un chiffre entre 0 et 9 (sinon erreur !)
    val = int(regarder(src))
    avancer(src)
    return val

while True:
    n = int(input())
    if n == 0:
        break
    lignes = []
    for i in range(n):
        lignes.append(input())
    # Important d'enlever les espaces je crois
    print(expression(Source(''.join(lignes)), 0, OPERATEURS['+']))