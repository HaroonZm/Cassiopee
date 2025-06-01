N, K, L = map(int, input().split())  # Utilisation de la fonction map pour convertir les entrées en int et les assigner aux variables N, K, et L
A = list(map(int, input().split()))  # Conversion de la chaîne d'entrée en liste d'entiers A

# Définition d'une fonction nommée is_ok qui vérifie si on peut prendre au moins L éléments 
# inférieurs ou égaux à X en respectant certaines contraintes basées sur K
def is_ok(X):
    r = 0  # Initialisation de l'indice droit de la fenêtre glissante à 0
    cnt1 = 0  # Initialisation d'un compteur accumulant le nombre total d'éléments valides trouvés
    cnt2 = 0  # Compteur pour le nombre actuel d'éléments valides entre i et r
    for i in range(N):  # Parcours de tous les indices i de 0 à N-1 inclus
        for j in range(r, N):  # Parcours de j à partir de r jusqu'à la fin de la liste A
            if cnt2 == K - 1 and A[j] <= X:  
                # Si on a atteint K-1 éléments valides et A[j] est validé par la condition <= X
                r = j  # Met à jour r à la position j (nouvelle borne droite de la fenêtre)
                cnt1 += N - j  # Ajoute le nombre d'éléments restants à partir de j à cnt1
                if A[i] <= X:  # Si l'élément courant i est <= X
                    cnt2 -= 1  # Réduit le compteur cnt2 car on va "bouger" la fenêtre
                break  # Sort de la boucle interne for j
            elif A[j] <= X:  # Sinon, si A[j] est <= X, on incrémente cnt2
                cnt2 += 1  
        else:
            # Ce else correspond au for j; il s'exécute si on a parcouru toute la boucle sans break
            break  # Dans ce cas, on sort de la boucle for i car aucune autre fenêtre valide n'a été trouvée
    # Après avoir parcouru toutes les fenêtres possibles et comptabilisé les éléments,
    # on compare cnt1 avec L pour décider si la condition est satisfaite
    if cnt1 >= L:
        return True  # On peut prendre au moins L éléments valides
    else:
        return False  # On ne peut pas en prendre autant

# Fonction de recherche binaire qui cherche la valeur minimale X pour laquelle is_ok(X) est True
def bisearch(high, low):
    while high - low > 1:  # Tant que l'intervalle de recherche contient plus d'un élément
        mid = (high + low) // 2  # Calcule la valeur moyenne entière entre high et low
        if is_ok(mid):  # On teste si on peut prendre L éléments avec la limite X = mid
            high = mid  # Si oui, on essaye une valeur plus petite, donc on met à jour high
        else:
            low = mid  # Sinon, on essaye une valeur plus grande, donc on met à jour low
    return high  # La valeur minimale pour laquelle la condition est remplie est retournée

print(bisearch(200000, -1))  # Appelle la fonction bisearch avec un intervalle initial et affiche le résultat final