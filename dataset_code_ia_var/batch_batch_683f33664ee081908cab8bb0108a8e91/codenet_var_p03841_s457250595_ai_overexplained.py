# Début de la définition de la fonction 'solve'
def solve():
    # Lire un entier 'n' depuis l'entrée utilisateur.
    # Ceci définit la taille du tableau qui sera traité.
    n = int(input())
    
    # Lire une ligne de nombres séparés par des espaces depuis l'entrée utilisateur,
    # appliquer la fonction 'int' à chaque élément via 'map', puis convertir le résultat en liste.
    # Cela crée une liste d'entiers appelée 'x' de taille n.
    x = list(map(int, input().split()))
    
    # Initialiser une liste vide appelée 'list1'. Cette liste stockera des paires de valeurs.
    # Les paires vont contenir le nombre de la liste 'x' et son indice (avec un décalage de +1).
    list1 = []
    
    # Définir une fonction 'ap1' pour ajouter un élément à 'list1'.
    # 'num' est ici un paramètre générique qui sera une paire [valeur, position].
    def ap1(num):
        list1.append(num)
    
    # Pour chaque indice de 0 à n-1 (car range(n) donne 0 inclus jusqu'à n exclus),
    # ajouter à 'list1' la paire [x[i], i+1].
    # 'i+1' est utilisé pour donner des indices commençant à 1, pas 0.
    for i in range(n):
        ap1([x[i], i+1])

    # Définir une fonction lambda appelée 'str1', qui prend une valeur 'val'
    # (qui sera une paire [valeur, position]) et retourne le premier élément de la paire.
    # Cette lambda sera utilisée comme fonction de tri.
    str1 = lambda val: val[0]
    
    # Trier la liste 'list1' selon la valeur du premier élément de chaque paire.
    # Cela trie la liste selon les valeurs initialement lues dans 'x'.
    list1.sort(key=str1)
    
    # Déclarer deux listes vides : 'numa' et 'numb'.
    # Elles serviront à stocker des séquences spécifiques de valeurs pour l'algorithme.
    numa = []
    numb = []
    
    # Pour chaque indice de 0 à n-1,
    # prendre le deuxième élément de la paire dans 'list1[i]' (qui est la position original +1),
    # puis ajouter à 'numa' ce numéro répété 'num3-1' fois,
    # et à 'numb' ce numéro répété 'n-num3' fois.
    # Cela traite chaque case possible du carré.
    for i in range(n):
        num3 = list1[i][1]
        numa += [num3] * (num3 - 1)  # Étendre la liste avec 'num3-1' fois le numéro 'num3'.
        numb += [num3] * (n - num3)  # Étendre avec 'n-num3' fois le numéro 'num3'.
    
    # Initialiser plusieurs compteurs à zéro :
    count1 = 0  # Compte le nombre d'insertions principales terminées.
    count2 = 0  # Indique la position actuelle dans 'numa'.
    count3 = 0  # Indique la position actuelle dans 'numb'.
    count3 = 0
    
    # Initialiser une liste vide appelée 'ans' qui va contenir la réponse finale.
    ans = []
    
    # Initialiser une variable 'ansnum' à zéro. Elle servira comme indicateur d'échec.
    ansnum = 0
    
    # Définir une fonction 'countnum' qui compte combien de fois 'num' apparaît dans 'ans'
    def countnum(num):
        return ans.count(num)
    
    # Définir une fonction 'apans' qui ajoute 'num' à la liste 'ans'.
    def apans(num):
        ans.append(num)
    
    # Faire une boucle de 0 à n*n-1 (donc au total n^2 tours, pour chaque case du carré de taille n*n)
    for i in range(n * n):
        yn = 0  # Cette variable servira à déterminer si l'on a effectué une insertion principale ou non.
        
        # Si on n'a pas encore traité tous les éléments principaux,
        # vérifier si l'indice actuel 'i' correspond à la position (convertie à partir de la valeur) du prochain nombre à placer dans 'list1'.
        if count1 != n:
            # Vérifier si l'indice 'i' est égal à (valeur dans la paire de list1[count1] - 1).
            # Cela vérifie la position à laquelle il faut placer un certain numéro.
            if i == list1[count1][0] - 1:
                # Vérifier si le nombre d'occurrences du numéro (list1[count1][1]) dans 'ans'
                # est différent de ce qui est attendu (list1[count1][1] - 1).
                if countnum(list1[count1][1]) != list1[count1][1] - 1:
                    # Si c'est le cas, il y a une incohérence : placer ce numéro ici n'est pas valable.
                    ansnum = 1  # Indiquer une erreur.
                    break  # Sortir de la boucle car ce n'est pas possible.
                # Ajouter le numéro à la réponse finale 'ans'.
                apans(list1[count1][1])
                count1 += 1  # Passer à l'élément suivant dans 'list1'.
                yn = 1  # Marquer qu'on a fait une insertion principale.
        
        # Si on n'a pas fait d'insertion principale,
        # alors on va remplir à partir des listes auxiliaires 'numa' ou 'numb'.
        if yn == 0:
            # Si on n'a pas encore utilisé tous les éléments dans 'numa'
            if count2 != len(numa):
                apans(numa[count2])  # Ajouter l'élément courant de 'numa' à 'ans'.
                count2 += 1  # Passer à l'élément suivant.
            # Sinon, si on n'a pas encore utilisé tous les éléments de 'numb'
            elif count3 != len(numb):
                apans(numb[count3])  # Ajouter l'élément courant de 'numb' à 'ans'.
                count3 += 1
            else:
                # Si on a épuisé les deux listes auxiliaires mais qu'on est pas arrivé à la fin ('i' n'est pas n^2-1),
                # cela signifie qu'on ne peut pas compléter 'ans' correctement.
                if i != n * n - 1:
                    ansnum = 1  # Indiquer une erreur.
                    break  # Sortir de la boucle.
    
    # Après la boucle, vérifier si on a rencontré une erreur.
    if ansnum == 1:
        print("No")  # Si oui, il n'est pas possible de satisfaire les conditions. Afficher 'No'.
    else:
        print("Yes")  # Sinon, il est possible. Afficher 'Yes'.
        print(*ans)   # Afficher le contenu de la liste 'ans', séparé par des espaces.

# Appeler la fonction 'solve' pour lancer le traitement.
solve()