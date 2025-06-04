# Demander à l'utilisateur d'entrer un nombre entier et l'enregistrer dans la variable n.
# Cela définira la longueur de la séquence d'animaux à traiter.
n = int(input())

# Demander à l'utilisateur d'entrer une chaîne de caractères et l'enregistrer dans la variable s.
# Cette chaîne représente la séquence d'observations ('o' ou 'x') sur chaque position d'animal.
s = input()

# Créer une liste ans de taille n remplie initialement de 'S' (supposons que cela représente un mouton).
# Cette liste va représenter l'état actuel supposé des animaux autour du cercle.
ans = ['S'] * n  # * signifie que la liste est dupliquée n fois avec la valeur 'S'

# Initialisations de séquences possibles pour les premiers éléments (et dernier).
# ani0 : états potentiels pour le premier animal.
# ani1 : états potentiels pour le deuxième animal.
# anim1 : états potentiels pour le dernier animal (le n-ème car c’est un cercle).
ani0 = ['S', 'S', 'W', 'W']
ani1 = ['S', 'W', 'S', 'W']
anim1 = ['S', 'W', 'W', 'S']

# Boucle sur les 4 configurations possibles d'initialisation (pour couvrir tous les cas de base).
for i in range(4):
    # Définir le premier animal selon la configuration ani0.
    ans[0] = ani0[i]
    # Si la première observation s[0] est 'o', régler le deuxième et le dernier animal suivant le cas de base.
    if s[0] == 'o':
        # L’observation 'o' influence la configuration attendue suivant des règles logiques propres à l’énoncé.
        # On assigne alors le (dernier) et le (deuxième) animal respectivement à anim1[i] et ani1[i].
        ans[-1] = anim1[i]
        ans[1] = ani1[i]
    else:
        # Si l’observation n’est pas 'o', on utilise la configuration inverse (indice retourné 3-i).
        ans[-1] = anim1[3 - i]
        ans[1] = ani1[3 - i]

    # On commence à itérer sur chaque position de la séquence des observations.
    for j in range(1, n):
        # On gère les deux dernières itérations explicitement à cause du comportement circulaire.
        if j >= n - 2:
            # Si l'observation à la position j est 'o'
            if s[j] == 'o':
                # Plusieurs cas sont gérés en fonction des valeurs actuelles d'ans (animal supposé)
                if ans[j] == 'S':
                    if ans[j - 1] == 'S':
                        if ans[(j + 1) % n] == 'S':
                            if j == n - 1:
                                # Si tous les cas sont validés, on affiche la configuration trouvée et on quitte le programme.
                                print(*ans, sep='')
                                exit()
                        else:
                            # Si la condition n’est pas satisfaite, on sort de la boucle.
                            break
                    else:
                        if ans[(j + 1) % n] == 'W':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
                else:
                    if ans[j - 1] == 'S':
                        if ans[(j + 1) % n] == 'W':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
                    else:
                        if ans[(j + 1) % n] == 'S':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
            else:  # Si l'observation n'est pas 'o' donc elle est 'x'
                if ans[j] == 'S':
                    if ans[j - 1] == 'S':
                        if ans[(j + 1) % n] == 'W':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
                    else:
                        if ans[(j + 1) % n] == 'S':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
                else:
                    if ans[j - 1] == 'S':
                        if ans[(j + 1) % n] == 'S':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
                    else:
                        if ans[(j + 1) % n] == 'W':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
        # Si on est sur la dernière case, on arrête la boucle, car la dernière case a été vérifiée.
        if j == n - 1:
            break

        # Mise à jour de l'animal à la prochaine position en fonction de l'observation s[j] et des états précédents.
        # On respecte ici la relation entre observation et types possibles pour l'animal suivant.
        if s[j] == 'o':
            if ans[j] == 'S':
                if ans[j - 1] == 'S':
                    ans[j + 1] = 'S'
                else:
                    ans[j + 1] = 'W'
            else:  # ans[j] == 'W':
                if ans[j - 1] == 'S':
                    ans[j + 1] = 'W'
                else:
                    ans[j + 1] = 'S'
        else:  # s[j] == 'x'
            if ans[j] == 'S':
                if ans[j - 1] == 'S':
                    ans[j + 1] = 'W'
                else:
                    ans[j + 1] = 'S'
            else:  # ans[j] == 'W':
                if ans[j - 1] == 'S':
                    ans[j + 1] = 'S'
                else:
                    ans[j + 1] = 'W'

# Si aucune des configurations testées n'a permis de trouver une séquence valide, on affiche -1.
print(-1)