# AOJ Volume4 0411
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0411

# On commence par lire deux entiers depuis l'entrée standard.
# La fonction input() lit une ligne sous forme de chaîne de caractères.
# La méthode split() coupe cette chaîne en liste de sous-chaînes sur les espaces.
# map(int, ...) convertit chaque sous-chaîne en entier.
# list() transforme le map en liste concrète.
# Ainsi, N est le nombre d'éléments, et L une limite ou longueur donnée.
N, L = list(map(int, input().split()))

# On initialise une liste vide c pour stocker des paires de données.
c = []

# Cette boucle itère N fois, de 0 à N-1.
# Le _ est une convention pour indiquer qu'on ne se sert pas de la variable de boucle.
for _ in range(0, N):
    # On lit une ligne, la décompose en deux entiers, p et d.
    # p et d sont probablement les coordonnées et une direction ou état associé.
    p, d = list(map(int, input().split()))
    # On ajoute la paire (p, d) à la liste c.
    # L'opérateur += avec une liste ajoute les éléments d'une autre liste.
    # Ici [(p,d)] est une liste contenant un tuple, donc on ajoute ce tuple à c.
    c += [(p, d)]

# Une fois toutes les données chargées, on trie la liste c.
# Le tri s'effectue par défaut selon le premier élément de chaque tuple, ici p.
c.sort()

# On extrait la première composante p de chaque tuple dans une nouvelle liste masu.
# Cette liste contiendra les positions des éléments, ordre désormais trié par p.
masu = [p for p, d in c]

# On extrait la deuxième composante d de chaque tuple dans une autre liste dir.
# Cette liste contient donc la direction associée à chaque position.
dir  = [d for p, d in c]

# variable result initialisée à 0, elle sera utilisée pour stocker le résultat final.
result = 0

# variable score initialisée à 0, elle servira à calculer un score intermédiaire.
score = 0

# boucle de 0 à N-1 sur les indices des éléments.
for j in range(0, N):
    # Si la direction de l'élément j vaut 0,
    if dir[j] == 0:
        # On ajoute à score la différence entre la position p et (j+1) moins 1.
        # Cela semble mesurer un décalage ou un score partiel relatif à l'indice.
        score += masu[j] - j - 1
    # Sinon si la direction vaut 1,
    elif dir[j] == 1:
        # On soustrait ce même décalage à score.
        score -= masu[j] - j - 1
    # On met à jour la position masu[j] pour qu'elle soit l'indice 1-based j+1.
    masu[j] = j + 1
# Après avoir traité tous les éléments, on affecte score à result.
result = score

# Boucle inversée sur les indices de N-1 à 0 inclu.
for i in range(N - 1, -1, -1):
    # Si la direction à i vaut 1,
    if dir[i] == 1:
        # On ajoute à score calcul basé sur L, N, i, et masu[i].
        # L - (N - i) calcule une sorte de décalage à partir de la fin,
        # on retranche masu[i] puis ajoute 1.
        score += L - (N - i) - masu[i] + 1
    # Sinon, si direction vaut 0,
    elif dir[i] == 0:
        # On soustrait ce même terme de score.
        score -= L - (N - i) - masu[i] + 1
    # masu[i] est alors mise à une nouvelle valeur calculée en fonction de L, N, i.
    masu[i] = L - (N - i) + 1
    
    # On met à jour result avec la valeur maximale entre result et score.
    result = max(result, score)

# On affiche la valeur finale de result qui représente le score maximum calculé.
print(result)