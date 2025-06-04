from bisect import bisect_left, bisect_right, insort_left  # Importation des fonctions du module bisect utilisées pour manipuler des listes triées

n = int(input())  # Lecture d'une ligne de l'entrée, conversion en entier. Cette variable 'n' représente le nombre total d'instructions à traiter.

dic = {}  # Création d'un dictionnaire vide nommé 'dic'. Il sera utilisé pour stocker des clés (de type string) associées à des listes d'entiers.
dic2 = {}  # Création d'un second dictionnaire vide nommé 'dic2'. Dans ce code, il n'est pas utilisé, il pourrait être un vestige d'une version précédente ou prévu pour une utilisation future.
box = []  # Initialisation d'une liste vide nommée 'box', qui servira à stocker les valeurs 'b' de manière triée, afin de faciliter la recherche binaire.

# Boucle principale qui itère 'n' fois (c'est-à-dire pour chaque commande à traiter)
for i in range(n):
    a, b, *c = input().split()  # Lecture d'une ligne de l'entrée, séparation en différentes variables. 'a' est le premier élément, 'b' le second, et le reste est stocké dans la liste 'c'.
    
    if a == '0':  # Si la commande est '0'
        # On utilise 'insort_left' pour insérer 'b' dans la liste 'box', en gardant la liste triée.
        # 'insort_left' insère l'élément à la position appropriée selon l'ordre croissant sans perturber l'ordre.
        insort_left(box, b)
        
        # Vérification si la clé 'b' existe déjà dans le dictionnaire 'dic'.
        if b in dic:
            temp = dic[b]  # On récupère la liste associée à la clé 'b' dans 'dic'.
            # On ajoute à cette liste l'entier obtenu à partir du premier élément de la liste 'c'.
            dic[b] = temp + [int(c[0])]
        else:
            # Si la clé 'b' n'existe pas encore, on crée une nouvelle liste contenant seulement cet entier.
            dic[b] = [int(c[0])]
    
    elif a == '1':  # Si la commande est '1'
        # Vérification si la clé 'b' est présente dans 'dic'.
        if b in dic:
            pri = []  # Création d'une liste vide servant à stocker les représentations sous forme de chaînes de caractères des entiers associés à 'b'.
            for i in dic[b]:
                pri.append(str(i))  # Conversion de chaque entier en chaîne de caractères et ajout à la liste 'pri'.
            # Affichage de chaque élément de la liste 'pri' (c'est-à-dire les entiers associés à 'b'), séparés par des retours à la ligne.
            print("\n".join(pri))
    
    elif a == '2':  # Si la commande est '2'
        # Vérification si 'b' est une clé dans 'dic'.
        if b in dic:
            # Suppression de la clé 'b' du dictionnaire 'dic' ainsi que de sa liste associée.
            del dic[b]
    
    else:  # Pour toute autre valeur de 'a' différente de '0', '1' ou '2'
        # On effectue une recherche binaire dans la liste triée 'box' pour trouver l'intervalle d'indices correspondant aux valeurs entre 'b' et 'c[0]' inclusivement.
        L = bisect_left(box, b)  # Trouve l'indice du premier élément dans 'box' qui est n'est pas inférieur à 'b'.
        R = bisect_right(box, c[0])  # Trouve l'indice du premier élément dans 'box' qui est strictement supérieur à 'c[0]'.
        
        # Boucle tant que L est strictement inférieur à R (parcours de l'intervalle trouvé dans 'box')
        while L < R:
            # Vérifie si la valeur 'box[L]' existe comme clé dans le dictionnaire 'dic'.
            if box[L] in dic:
                for i in dic[box[L]]:  # Pour chaque entier associé à cette clé
                    # Affiche la clé (qui est une chaîne) suivie de l'entier associé.
                    print(box[L], i)
            # Passe à l'indice suivant correspondant à une nouvelle clé dans la liste triée (on saute les doublons de 'box[L]').
            # 'bisect_right(box, box[L])' donne l'indice du prochain élément strictement supérieur à 'box[L]'.
            L = bisect_right(box, box[L])