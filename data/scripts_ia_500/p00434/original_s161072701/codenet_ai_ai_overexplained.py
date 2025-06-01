# Création d'une liste appelée 'n' qui contiendra des nombres entiers
# Ici, on utilise une compréhension de liste pour remplir 'n' avec des valeurs allant de 1 à 30 inclus
# 'range(30)' génère une séquence de nombres de 0 à 29 (30 nombres en tout)
# 'i+1' décale cette séquence pour que les nombres commencent à 1 au lieu de 0
n = [i + 1 for i in range(30)]

# Boucle 'for' qui va s'exécuter 28 fois
# 'range(28)' produit les entiers de 0 à 27, donc la boucle se répète 28 fois
for i in range(28):
    # Appel de la fonction 'input()' qui attend que l'utilisateur entre une valeur au clavier
    # Cette valeur est récupérée sous forme de chaîne de caractères
    # 'int(input())' convertit cette chaîne en un entier pour manipulation numérique
    valeur = int(input())
    
    # La méthode 'index' est utilisée sur la liste 'n' pour trouver l'indice (position) 
    # où l'entier 'valeur' apparaît pour la première fois dans la liste
    indice_valeur = n.index(valeur)
    
    # 'pop' supprime (retire) l'élément de la liste 'n' situé à l'indice 'indice_valeur'
    # Cela signifie que l'entier fourni par l'utilisateur sera retiré de la liste 'n'
    n.pop(indice_valeur)

# Après la boucle, il restera exactement 2 éléments dans la liste 'n' 
# puisque 28 éléments ont été retirés d'une liste initialement de 30 éléments

# 'print(*n, sep='\n')' affiche chaque élément de la liste 'n' sur une ligne différente
# L'opérateur '*' dépaquète (découpe) la liste pour passer chaque élément en argument séparé à la fonction 'print'
# Le paramètre 'sep' avec la valeur '\n' indique que les éléments doivent être séparés par des sauts de ligne
print(*n, sep='\n')