# Définition de la fonction principale solve qui contient toute la résolution du problème
def solve():
    # On lit une ligne de l'entrée standard avec input()
    # .split() permet de séparer la chaine saisie en fonction des espaces, créant ainsi une liste de chaînes de caractères
    # map(int, ...) va convertir chaque élément de cette liste de chaînes en entier
    # Les deux résultats sont assignés aux variables A et B, de gauche à droite
    A, B = map(int, input().split())

    # On lit une autre ligne de l'entrée standard, supposée contenir A entiers séparés par des espaces
    # Ensuite, on convertit chaque élément en entier comme ci-dessus
    # tuple(...) transforme la séquence ainsi créée en tuple (structure de données immuable, comme une liste mais non modifiable)
    s1 = tuple(map(int, input().split()))

    # On répète le processus pour une nouvelle ligne, cette fois pour remplir le tuple s2 avec B entiers
    s2 = tuple(map(int, input().split()))

    # On initialise la variable result à 0.
    # Cette variable stocke le plus grand nombre de correspondances trouvées entre s2 et s1 selon un algorithme donné
    result = 0

    # On commence une boucle for sur une plage d'entiers de 0 à B-1 inclus
    # range(B) produit une séquence de valeurs 0, 1, 2, ..., B-1
    # La variable i prend successivement chacune de ces valeurs
    for i in range(B):
        # On initialise une variable k à 0 pour chaque nouvelle valeur de i
        # k sera utilisé comme index pour avancer dans s1
        k = 0
        # On initialise aussi une variable cnt à 0, pour compter le nombre de correspondances trouvées pour ce i
        cnt = 0

        # On utilise enumerate pour itérer dans une partie de s2, celle allant de l'indice i à la fin
        # enumerate(s2[i:]) va donc donner pour chaque élément restant de s2 à partir de i :
        #    - un index j (valeur commençant à 0)
        #    - une valeur n (l'élément courant de la séquence)
        for j, n in enumerate(s2[i:]):
            # On commence une boucle for imbriquée sur tous les éléments de s1 à partir de l'indice k
            # s1[k:] crée une vue (un sous-tuple) démarrant à l'indice k et allant jusqu'à la fin
            # Cette boucle va donc examiner successivement tous les éléments restants de s1
            for m in s1[k:]:
                # On incrémente k manuellement de 1 à chaque itération de la boucle
                # Cela permet de s'assurer qu'on ne considère chaque élément dans s1 qu'une seule fois
                k += 1
                # On vérifie si le nombre courant n de s2 est égal au nombre courant m de s1
                if n == m:
                    # Si c'est le cas, on a trouvé une correspondance
                    # On incrémente alors cnt pour garder trace de cette correspondance
                    cnt += 1
                    # On arrête la boucle for sur s1 puisqu'on a trouvé la correspondance pour n
                    break
            # À ce stade, soit on a trouvé n dans s1[k:] (et fait un break), soit non (donc on passe à l'itération suivante de n)

        # Après avoir terminé l'examen des éléments de s2[i:], on vérifie si cnt (nombre de correspondances pour cet i donné)
        # est strictement supérieur à la valeur actuelle de result (le meilleur score trouvé jusque là)
        if cnt > result:
            # Si oui, alors on met à jour le résultat maximal trouvé
            result = cnt
        # Encore une condition d'optimisation :
        # Si result est déjà supérieur ou égal au nombre d'éléments restants à traiter dans s2,
        # c'est-à-dire B-i, alors il est inutile de continuer la boucle sur i car il n'est plus possible d'améliorer le résultat
        if result >= B - i:
            # On quitte prématurément la boucle for sur i
            break
    # Enfin, quand toutes les comparaisons sont faites, on affiche la valeur finale de result
    print(result)

# Ce bloc sert à ne lancer solve() que si le script est exécuté directement (pas importé en tant que module)
if __name__ == "__main__":
    solve()