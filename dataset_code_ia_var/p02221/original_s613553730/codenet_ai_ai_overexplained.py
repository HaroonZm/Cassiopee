import sys  # Importe le module système, qui contient des fonctions et des variables utilisées pour manipuler différentes parties de l'environnement d'exécution Python

# On crée un alias 'read' pour la méthode de lecture brute du flux d'entrée standard (stdin) sous forme de bytes
read = sys.stdin.buffer.read

# On crée un alias 'readline' pour la méthode de lecture d'une seule ligne brute à partir du flux d'entrée standard
readline = sys.stdin.buffer.readline

# On crée un alias 'readlines' pour la méthode de lecture de toutes les lignes restantes depuis stdin, chacun étant un bytes object
readlines = sys.stdin.buffer.readlines

# On lit un entier N à partir d'une ligne d'entrée :
#   - readline() lit une seule ligne comme bytes
#   - int() convertit cette valeur bytes en un entier directement (l'entrée doit donc être sous la forme d'une chaîne d'entiers, ex : '5\n')
N = int(readline())

# On prépare une liste S représentant la chaîne binaire en entrée, à partir d'une deuxième ligne lue :
#   - readline() lit la ligne, rstrip retire les caractères de fin comme '\n'
#   - pour chaque caractère (byte) x dans cette ligne :
#       - int(x) donne le code ASCII du caractère (puisque x est aussi un byte)
#       - ord('0') est le code ASCII du caractère '0' (c'est-à-dire 48)
#       - donc int(x) - ord('0') convertit le caractère chiffré ('0' ou '1') en nombre entier (0 ou 1)
#   - [0] + ... : on ajoute le zéro au début pour garder l'indice 0 inutilisé (1-based indexing), probablement pour simplifier les calculs de décalage plus tard
S = [0] + [int(x) - ord('0') for x in readline().rstrip()]

# On lit maintenant la troisième entrée, qui consiste en une séquence de nombres séparés par des espaces
# - read() lit tous les bytes restants du flux, split() les découpe selon les espaces et les retours à la ligne
# - [int(x) for x in ...] convertit chaque bytes en integer
P = [int(x) for x in read().split()]

# On double la liste P. Ceci permet que pour un décalage (offset) dx, on puisse toujours prendre P[i+dx] sans se soucier du débordement d'indice (circular buffer)
P += P

# On crée une liste dp (pour "programmation dynamique"), qui contiendra successivement plusieurs listes générées étape par étape
# Elle commence par la liste doublée P.
dp = [P]

# On exécute une boucle sur i allant de 0 à N inclus (range(N+1) car le stop n'est pas inclusif)
for i in range(N+1):
    # On récupère la i-ème liste de la mémoire dynamique, à partir de laquelle on va générer la suivante
    P = dp[i]
    # On prépare une nouvelle liste vide qui va contenir la prochaine génération de valeurs
    newP = []
    # On calcule le décalage dx comme étant une puissance de 2 : 1 << i signifie 2^i
    dx = 1 << i
    # On avance dans P deux à deux : on considère chaque a à l'indice j et b à l'indice j+dx
    for a, b in zip(P, P[dx:]):
        # Ordre croissant : si a > b, on échange a et b
        if a > b:
            a, b = b, a
        # On utilise l'information binaire dans S pour faire un choix :
        #   - S[b-a] est censé être un 0 ou un 1 (prend la position b-a dans la chaîne binaire fournie)
        #   - Si S[b-a] vaut 1, on prend b ; sinon on prend a et on ajoute la valeur choisie à la nouvelle liste
        if S[b - a]:
            newP.append(b)
        else:
            newP.append(a)
    # On ajoute la nouvelle génération à la liste dynamique
    dp.append(newP)

# On génère la séquence finale de réponses : P[:-1] sont tous les éléments sauf le dernier (on ignore le dernier, raison à déterminer selon le problème source)
# - On utilise un générateur pour produire chaque valeur x de la liste finale
answers = (x for x in P[:-1])

# On imprime les réponses, chacune sur une ligne
# - map(str, answers) convertit chaque entier en chaîne de caractères
# - '\n'.join(...) joint les chaînes avec un saut de ligne
# - print imprime le résultat final d'un seul coup
print('\n'.join(map(str, answers)))