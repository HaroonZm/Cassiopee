import numpy as np  # Importe la bibliothèque NumPy, qui permet de manipuler des tableaux et matrices, et fournit des fonctions mathématiques performantes.

# Déclaration d'une fonction nommée 'checker' qui prend deux arguments :
# - n : un entier, représentant typiquement le nombre d'éléments dans la liste 'da'.
# - da : une liste d'entiers
def checker(n, da):
    # Calcule la valeur maximale présente dans la liste 'da'
    mx = max(da)  # max() renvoie la plus grande valeur trouvée dans 'da'.
    # Calcule la valeur minimale présente dans la liste 'da'
    mi = min(da)  # min() renvoie la plus petite valeur trouvée dans 'da'.
    
    # Si la valeur de 'n' est exactement 2, alors vérifie si 'da' est exactement [1, 1]
    if n == 2:
        # L'opérateur '==' compare la liste 'da' à la liste [1, 1] élément par élément.
        return (da == [1, 1])  # Renvoie True si 'da' est [1, 1], sinon False.
    
    # Condition alternative : si la valeur maximale est strictement inférieure à 2 
    # OU si 'n' est inférieure ou égale à la valeur maximale
    if mx < 2 or n <= mx:
        return False   # On considère le cas comme impossible, donc retourne 'False'.
    
    # Création d'un tableau de zéros avec taille suffisante pour contenir tous les indices de 0 à mx inclus.
    # Ce tableau servira à compter les occurrences de chaque nombre dans 'da'.
    # 'np.zeros' crée un tableau rempli de zéros, 'mx + 1' définit sa longueur, 'dtype=int' précise que les valeurs seront des entiers.
    arr = np.zeros(mx + 1, dtype=int)
    
    # Parcourt tous les indices de la liste 'da' de 0 à n-1 inclus.
    for i in range(n):
        # Pour chaque valeur da[i], incrémente l'élément du tableau 'arr' correspondant à da[i] de 1.
        # Ceci permet de compter combien de fois chaque entier apparaît dans 'da'.
        arr[da[i]] += 1
    
    # Vérifie si 'mx' est impair (c'est-à-dire que le reste de la division entière par 2 est différent de zéro)
    if mx % 2:
        # Si le nombre minimal 'mi' apparaît plus de 2 fois, ou si le calcul (mx + 1) // 2 est différent de mi, on retourne False.
        if arr[mi] > 2 or (mx + 1) // 2 != mi:
            return False  # Ce sont des conditions supplémentaires pour la validité du cas.
    else:
        # Si 'mx' est pair :
        # Si le nombre minimal apparaît plus d'une fois, ou si mx // 2 est différent de mi, on retourne False.
        if arr[mi] > 1 or mx // 2 != mi:
            return False  # Idem, c'est pour valider la structure particulière attendue.
    
    # Boucle allant de la valeur minimale à la valeur maximale moins 1 (car range ne prend pas la borne supérieure)
    for i in range(mi, mx):
        # Si, pour une valeur i, la valeur i+1 n'apparaît pas au moins deux fois dans 'da'
        if arr[i + 1] < 2:
            return False  # Retourne immédiatement False car cette condition n'est pas satisfaite.
    
    # Si toutes les conditions sont vérifiées, retourne True, ce qui signifie que la configuration est possible.
    return True

# Définition de la fonction principale du programme
def main():
    # Récupère une entrée utilisateur, la convertit en entier, et l'affecte à la variable 'n'.
    # La fonction 'input()' lit une ligne, et 'int()' convertit la chaîne entrée en entier.
    n = int(input())
    # Récupère une autre entrée sous forme d'une ligne d'entiers séparés par des espaces, la découpe avec 'split()', 
    # convertit chaque élément en entier avec 'map(int, ...)' et rassemble le tout en une liste.
    da = list(map(int, input().split()))
    # Appelle la fonction 'checker' avec 'n' et 'da' comme arguments.
    # Si le résultat est True, affiche "Possible", sinon affiche "Impossible".
    if checker(n, da):
        print('Possible')
    else:
        print('Impossible')
    # La clause return ici n'est pas indispensable car elle n'est pas utilisée, mais elle marque la fin de la fonction.
    return

# Ce bloc permet de s'assurer que 'main()' ne sera exécuté que si ce script est lancé directement (et non importé depuis un autre module)
if __name__ == "__main__":
    main()  # Appelle la fonction principale.