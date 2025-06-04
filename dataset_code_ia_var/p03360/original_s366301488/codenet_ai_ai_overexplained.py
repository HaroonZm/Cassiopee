# Importer la fonction map pour appliquer une fonction à tous les éléments d'un itérable
# Ici, nous demandons à l'utilisateur de saisir trois entiers séparés par des espaces.
# La fonction input() récupère la saisie de l'utilisateur sous forme de chaîne de caractères.
# La méthode split() divise cette chaîne en une liste de sous-chaînes, chacune correspondant à un nombre isolé par des espaces.
# La fonction map(int, ...) convertit chaque sous-chaîne en entier.
# Enfin, l'opérateur de déballage (*) affecte les trois entiers respectivement à A, B et C.
A, B, C = map(int, input().split())

# Nous demandons à nouveau à l'utilisateur un entier, cette fois pour K.
# input() récupère la saisie utilisateur et int() la convertit en entier.
K = int(input())

# Définition d'une fonction appelée dfs (recherche en profondeur).
# Cette fonction prend en argument 4 paramètres :
#   i  : le niveau actuel de récursion ou le nombre d'opérations déjà effectuées
#   a  : un compteur indiquant combien de fois A a été doublé
#   b  : un compteur indiquant combien de fois B a été doublé
#   c  : un compteur indiquant combien de fois C a été doublé
def dfs(i, a, b, c):
    # Condition d'arrêt de la récursion :
    # Si le nombre d'opérations effectuées atteint le maximum K
    if i == K:
        # Calculer la somme pondérée de A, B et C, chacun multiplié par 2 puissance le nombre de doublages respectif.
        # 2**a signifie "2 à la puissance a" (le nombre de fois où A a été doublé)
        # Idem pour B et C
        return A * (2 ** a) + B * (2 ** b) + C * (2 ** c)
    
    # Sinon, on explore les trois possibilités pour l'opération suivante :
    #   - Doubler A en incrémentant a de 1
    #   - Doubler B en incrémentant b de 1
    #   - Doubler C en incrémentant c de 1
    # Pour chacune, on fait un appel récursif après avoir incrémenté le paramètre correspondant.
    
    # Cas 1 : on choisit de doubler A, donc a devient a+1
    res1 = dfs(i + 1, a + 1, b, c)
    # Cas 2 : on choisit de doubler B, donc b devient b+1
    res2 = dfs(i + 1, a, b + 1, c)
    # Cas 3 : on choisit de doubler C, donc c devient c+1
    res3 = dfs(i + 1, a, b, c + 1)
    
    # On prend le maximum parmi les trois résultats possibles pour ce niveau de récursion,
    # car on veut maximiser la somme totale finale.
    return max(res1, res2, res3)

# Appel initial de la fonction dfs :
# On commence à l'opération 0 (i=0),
# Aucun des entiers n'a encore été doublé (a=0, b=0, c=0)
# On affiche le résultat avec print pour montrer le maximum possible à la fin des K opérations.
print(dfs(0, 0, 0, 0))