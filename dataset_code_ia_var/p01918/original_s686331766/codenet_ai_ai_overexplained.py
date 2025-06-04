# Demander à l'utilisateur d'entrer un nombre et convertir la saisie en entier.
# Ici, input() lit un texte que int() transforme en nombre entier.
n = int(input())

# Si la valeur de n est exactement 1 :
if n == 1:
    # Afficher '! 1' pour signaler un résultat final, suivi de la valeur 1.
    print('! 1')
    # Arrêter immédiatement l'exécution du programme, car il n'y a rien d'autre à faire.
    exit()
# Si la valeur de n est exactement 2 :
elif n == 2:
    # Afficher '! 1 2' comme résultat final, qui est l'ordre des deux éléments.
    print('! 1 2')
    # Quitter le programme, car ce cas est traité.
    exit()

# Si n est supérieur à 2 :
# Afficher une requête commençant par '? 1 2', ce qui interroge une information basée sur 1 et 2.
print('? 1 2')
# Lire une réponse utilisateur et la transformer en entier ; c'est la valeur 'm'
m = int(input())

# Créer une liste vide pour stocker des informations concernant chaque élément à partir de 3 jusqu'à n.
d = []

# Boucler sur les entiers de 3 à n inclusivement.
for i in range(3, n + 1):
    # Afficher une requête '? 1 i', ce qui interroge une information basée sur 1 et i.
    print('? 1', i)
    # Lire la réponse, la convertir en entier et la stocker dans p (valeur associée à (1, i))
    p = int(input())
    # Afficher une requête '? 2 i', pour obtenir une autre information avec 2 et i.
    print('? 2', i)
    # Lire la réponse, la convertir en entier et la stocker dans q (valeur associée à (2, i))
    q = int(input())
    # Ajouter à la liste 'd' un tuple contenant la somme (p+q), p, q, et la valeur de i elle-même.
    # Cela permettra plus tard de trier et d'utiliser toutes ces valeurs pour prendre des décisions.
    d.append((p + q, p, q, i))

# Trier la liste 'd' par ordre croissant (c'est le comportement par défaut de sorted).
# Ensuite, inverser la liste pour obtenir un ordre décroissant de la somme p+q (élément d[i][0]).
d = sorted(d)[::-1]

# Créer deux listes vides pour stocker respectivement des indices à 'gauche' et à 'droite'.
left = []
right = []

# Initialiser une variable de boucle 'i' à 0, même si elle sera aussi utilisée dans la boucle for après.
i = 0

# Flag (drapeau) booléen servant de marqueur pour savoir si le chiffre 2 a déjà été placé dans la liste 'right'.
flag = True

# Boucler sur tous les éléments d'indice dans la liste d (len(d) éléments).
for i in range(len(d)):
    # Récupérer les valeurs p et q à partir du tuple courant dans la liste.
    p = d[i][1] # correspond à la distance/relation entre le noeud 1 et i
    q = d[i][2] # correspond à la distance/relation entre le noeud 2 et i
    # j est la valeur de l'élément du sommet courant (compris entre 3 et n)
    j = d[i][3]
    # Si la somme (p+q = d[i][0]) est inférieure ou égale à m (valeur obtenue initialement entre 1 et 2)
    if d[i][0] <= m:
        # Si le drapeau est encore à True, il faut placer 2 dans la liste 'right' une seule fois.
        if flag:
            right.append(2)
            flag = False
        # Ajouter j à la liste 'right'
        right.append(j)
        # Continuer à l'itération suivante sans exécuter le reste du code de la boucle pour cette itération.
        continue
    # Si q > p (donc la relation avec 2 est plus grande qu’avec 1), placer j à gauche.
    if q > p:
        left.append(j)
    # Sinon placer j à droite.
    else:
        right.append(j)

# Si le drapeau flag est toujours à True après la boucle, il signifie que l’élément 2 n’a pas encore été mis dans 'right',
# donc il faut l'y ajouter (on ne doit jamais oublier ce nœud important).
if flag:
    right.append(2)

# Construire la réponse finale : concaténer la liste 'left', ensuite [1], puis la liste 'right' inversée (right[::-1]).
# Cela donne l’ordre souhaité des sommets/éléments/nœuds, en fonction de la logique appliquée précédemment.
ans = left + [1] + right[::-1]

# Afficher la réponse finale sous la forme requise :
# '!' suivi de chaque entier de la liste 'ans', séparés par des espaces.
print('!', ' '.join([str(u) for u in ans]))