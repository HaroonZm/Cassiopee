# Importation du module 'product' depuis 'itertools' pour générer toutes les combinaisons possibles 
# de produits cartésiens d'éléments provenant d'un ou de plusieurs iterables.
from itertools import product

# On lit 10 lignes depuis l'entrée standard.
# Pour chaque ligne, on sépare la ligne en parties en utilisant split(), 
# puis on convertit chaque élément en entier avec map(int, ...), 
# enfin, on transforme l'itérable map en une liste.
# Le résultat est une liste de 10 listes de 10 entiers chacune, représentée par la variable T.
T = [list(map(int, input().split())) for i in range(10)]

# Définition d'une fonction nommée 'calc' qui prend en argument 'v', généralement une liste d'entiers.
def calc(v):
    # 'val' est initialisée à 0. Elle sert d'indice de départ pour naviguer dans la table T
    val = 0
    # On parcourt chaque élément 'e' de la liste 'v'.
    for e in v:
        # La ligne d'indice 'val' de la table T est sélectionnée, puis on prend la colonne d'indice 'e'.
        val = T[val][e]
    # A la fin de la boucle, 'val' contient la valeur atteinte après avoir suivi les étapes dictées par v.
    return val

# Initialisation du compteur de solutions ne satisfaisant pas un certain critère à 0.
ans = 0

# On utilise product(range(10), repeat=4) pour générer toutes les combinaisons possibles de 4 chiffres
# (pouvant aller de 0 à 9 pour chacun) ; il y a 10^4 = 10000 combinaisons possibles.
for code in product(range(10), repeat=4):
    # On calcule l'entier 'e' en passant la combinaison 'code' comme argument à la fonction 'calc'.
    e = calc(code)
    # On considère qu'initialement la combinaison 'code', augmentée de 'e', est "valide".
    ok = 1
    # On transforme le tuple 'code' en une liste, puis on ajoute 'e' à la fin pour former une liste de longueur 5.
    code = list(code) + [e]
    
    # Pour chaque position i dans la liste 'code' (de 0 à 4 inclus : 5 éléments) :
    for i in range(5):
        # On crée une copie indépendante de la liste 'code' et on la stocke dans 'd'.
        d = code[:]
        # Pour chaque chiffre possible 'j' de 0 à 9 :
        for j in range(10):
            # Si la valeur à la position i de 'code' est déjà égale à j, on saute cette itération.
            if code[i] == j:
                continue
            # Sinon, on modifie la position i dans la copie 'd' pour qu'elle soit 'j'.
            d[i] = j
            # On applique la fonction calc à la liste modifiée 'd'. 
            # Si le résultat est 0, on considère que la combinaison modifiée échoue à un test.
            if calc(d) == 0:
                ok = 0   # On marque la combinaison comme non "robuste".
    
    # Pour chaque index i de 0 à 3 inclus (il s'agit des 4 premiers indices des 5 éléments du code) :
    for i in range(4):
        # On copie la liste 'code' dans une nouvelle variable 'd' pour ne pas modifier l'original.
        d = code[:]
        # On vérifie si les éléments consécutifs d[i] et d[i+1] sont identiques. 
        # Si oui, échanger n'aurait aucun effet, donc on passe à l'itération suivante.
        if d[i] == d[i+1]:
            continue
        # Sinon, on échange les éléments consécutifs d[i] et d[i+1].
        d[i], d[i+1] = d[i+1], d[i]
        # On applique 'calc' à cette nouvelle liste.
        # Si le résultat vaut 0, cela signifie que le code modifié n'est pas "robuste".
        if calc(d) == 0:
            ok = 0
    
    # Après tous ces tests, si 'ok' est passé à 0, cela veut dire que la combinaison 'code' 
    # (formée de 4 chiffres plus leur résultat e) n'est pas "robuste". 
    # Dans ce cas, on incrémente le compteur 'ans' de 1.
    if ok == 0:
        ans += 1

# Affichage du nombre total de combinaisons ayant échoué aux tests ci-dessus.
print(ans)