# AOJ 1036: Monster Factory
# Python3 2018.7.6 bal4u
# Code entièrement réécrit, avec des commentaires détaillés pour chaque partie, concept, et tâche.

# Boucle infinie pour traiter plusieurs jeux de données jusqu'à la condition d'arrêt
while True:
    # On lit la première chaîne de caractères depuis l'entrée standard
    # 'input()' lit une ligne de texte que l'utilisateur saisit, sous forme de chaîne
    # 'list()' convertit cette chaîne en liste de caractères, pour pouvoir manipuler chaque lettre individuellement (car les chaînes sont immuables en Python)
    in1 = list(input())  # in1 représente la première chaîne de caractères
    
    # On vérifie si la première lettre de in1 est un tiret '-', ce qui est le signal d'arrêt donné par l'énoncé
    if in1[0] == '-':
        # Si le signal d'arrêt est détecté, on quitte la boucle avec 'break'
        break

    # On lit une deuxième chaîne de caractères et on la convertit entièrement en liste de caractères
    in2 = list(input())  # in2 est la deuxième chaîne de caractères

    # Même opération pour la troisième chaîne
    out = list(input())  # out est la chaîne de sortie souhaitée (liste de caractères)

    # On initialise la variable 'k' avec le premier caractère de la liste in2
    # 'pop(0)' retire et retourne le premier élément de la liste (opération destructrice)
    k = in2.pop(0)

    # On initialise 'ans' à une chaîne vide ; elle stockera la réponse au problème
    ans = ''
    # On initialise un indicateur booléen 'f' à True ; il servira à noter si une condition d'échec survient
    f = True

    # On entre dans une boucle qui s'exécutera tant que l'une ou l'autre des listes 'in1' ou 'in2' n'est pas vide
    # 'len(liste)' retourne le nombre d'éléments dans la liste ; 'or' signifie que la boucle tourne si au moins une des deux n'est pas vide
    while len(in1) or len(in2):
        # On vérifie d'abord si la liste 'out' n'est pas vide ET si le premier caractère de 'out' est égal à 'k'
        if len(out) and out[0] == k:
            # Si c'est le cas, on change la lettre courante 'k' pour la suivante dans in1
            # On retire aussi la première lettre de 'out' car on considère qu'elle est utilisée
            k = in1.pop(0)
            del out[0]  # on retire ce caractère traité de 'out'
        else:
            # Si ce n'est PAS le cas, cela signifie que l'on cherche à construire 'k' dans la réponse
            # Donc, on ajoute le caractère 'k' à la variable 'ans' (concaténation de chaînes)
            ans += k

            # On regarde s'il reste des caractères dans 'in2'
            if len(in2):
                # S'il en reste, on met à jour 'k' avec le prochain caractère de 'in2'
                k = in2.pop(0)
            else:
                # S'il n'y a plus de caractères, on signale l'échec via 'f' et on sort de la boucle prématurément avec 'break'
                f = False
                break  # on arrête la boucle while

    # Une fois la boucle while terminée, on vérifie si 'f' est True (aucun échec)
    if f:
        # Si oui, on ajoute le dernier caractère 'k' à la réponse 'ans'
        ans += k

    # On affiche enfin la réponse à l'utilisateur
    print(ans)  # Affichage du résultat pour ce jeu de données

# Fin du programme. S'il lit un '-' en entrée, il s'arrête proprement