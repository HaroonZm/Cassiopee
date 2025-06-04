# Définition de la fonction Q, qui sert à effectuer une requête interactive auprès de l'utilisateur ou du système
def Q(x):
    # Utilisation de la fonction print pour afficher le caractère "?" suivi de la variable x
    # L'argument flush=True force l'affichage immédiat de la sortie, ce qui est important pour les systèmes interactifs
    print("?", x, flush=True)
    # Lecture d'une entrée utilisateur avec input(), puis conversion en entier avec int()
    # La fonction retourne cette valeur entière
    return int(input())

# On effectue une première requête avec pour argument la chaîne de caractères "A"
x = Q("A")  # Cette variable x va stocker la valeur retournée par la fonction Q("A")

# On vérifie si la valeur obtenue est égale à 128
if x == 128:
    # Si c'est le cas, on attribue la valeur 128 à la variable L
    L = 128
else:
    # Sinon, on continue avec des requêtes supplémentaires pour déterminer la valeur de L
    # On effectue une seconde requête dont l'argument est une chaîne composée de x fois le caractère "A"
    y = Q("A" * x)  # y va prendre la valeur retournée par Q sur "A" répété x fois
    # On effectue une troisième requête avec une chaîne qui est "A" répété x+1 fois
    z = Q("A" * (x + 1))  # z reçoit la valeur retournée par Q sur "A" répété x+1 fois

    # On compare les résultats obtenus pour y et z
    if z == y:
        # Si z et y sont égaux, cela signifie qu'ajouter un caractère n'a pas changé la réponse,
        # donc la longueur L est x + 1
        L = x + 1
    else:
        # Sinon, si la réponse a changé, la valeur de L est simplement x
        L = x

# Construction d'une liste S contenant tous les caractères possibles pour les indices d'un alphabet spécial
# chr(i) convertit un entier i en son caractère ASCII correspondant
# On construit d'abord les chiffres de 0 à 9 (codes ASCII 48 à 57 inclus)
S = [chr(i) for i in range(48, 58)]
# On ajoute ensuite les lettres majuscules A à Z (codes ASCII 65 à 90 inclus)
S += [chr(i) for i in range(65, 91)]
# Puis enfin les lettres minuscules a à z (codes ASCII 97 à 122 inclus)
S += [chr(i) for i in range(97, 123)]
# On obtient ainsi une liste de 62 caractères (10 chiffres + 26 majuscules + 26 minuscules)

# Initialisation d'une liste K de taille 62 contenant uniquement la valeur -1
K = [-1] * 62

# Remplissage de la liste K à l'aide d'une boucle for qui parcourt tous les indices de 0 à 61 inclus
for i in range(62):
    # Pour chaque i, on calcule une valeur en soustrayant à L la valeur retournée par Q sur la chaîne S[i] répétée L fois
    # Le résultat représente le nombre d'occurrences manquantes pour S[i] dans le mot recherché (codé subtilement)
    K[i] = L - Q(S[i] * L)

# Importation du module heapq permettant de gérer des files de priorité (min-heaps) efficacement
import heapq
# Création d'une liste de tuples pour la structure de heap
# Chaque tuple contient en première valeur l'élément K[i] (priorité), et en deuxième valeur la chaîne S[i] répétée K[i] fois
# Cela permet de manipuler et de fusionner par la suite les différentes parties du mot recherché
A = [(K[i], S[i] * K[i]) for i in range(62)]
# Transformation de la liste A en min-heap pour permettre des extractions efficaces du plus petit élément
heapq.heapify(A)

# La boucle principale s'exécute tant qu'il reste plus d'un élément dans le heap A
while len(A) > 1:
    # Extraction du tuple avec la plus petite priorité (le plus petit K[i]) du heap A
    x, y = heapq.heappop(A)
    # Si la priorité extraite x vaut 0, cela veut dire qu'il n'y a pas d'occurrence à traiter pour cette chaîne,
    # donc on passe à l'itération suivante
    if x == 0:
        continue
    # Extraction du deuxième tuple ayant la petite priorité suivante
    z, w = heapq.heappop(A)

    # Initialisation d'un indice ind qui servira à placer les caractères de w dans y
    ind = 0
    # La boucle parcourt chaque caractère de la chaîne w à insérer un par un
    for i in range(len(w)):
        # Boucle pour déterminer la bonne position d'insertion du caractère w[i] dans la chaîne y
        # On fait subtilement des requêtes en insérant w[i] à la position ind dans y 
        # et on compare la réponse à L-x-i pour savoir si on doit l'insérer plus loin ou non
        while Q(y[:ind] + w[i] + y[ind:]) >= L - x - i:
            ind += 1 # On avance l'indice de position
        # Après avoir trouvé la bonne position, on insère w[i] dans y à l'indice ind
        y = y[:ind] + w[i] + y[ind:]
        # On incrémente ensuite ind d'une unité pour traiter le prochain caractère
        ind += 1
    # Après avoir fusionné w dans y, on remet le résultat dans le heap avec la nouvelle priorité (x + z)
    heapq.heappush(A, (x + z, y))
    
# Lorsque la boucle s'arrête, il ne reste plus qu'un seul élément dans le heap,
# qui est supposé être la chaîne recherchée
# On affiche la réponse finale en préfixant par le caractère "!" puis la chaîne, suivi d'un flush pour garantir l'affichage
print("!", A[0][1], flush=True)