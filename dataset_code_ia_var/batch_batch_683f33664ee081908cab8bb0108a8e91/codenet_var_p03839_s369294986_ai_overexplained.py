# Lecture de deux entiers n et k à partir de l'entrée standard
# La fonction input() lit une ligne, split() la divise en mots, et map(int, ...) convertit chaque mot en entier
# Enfin, les deux entiers sont affectés à n et k grâce à l'affectation multiple
n, k = map(int, input().split())

# Lecture de la liste des entiers a_1 à a_n
# input() lit une ligne de texte contenant les nombres
# split() les sépare
# map(int, ...) les transforme en entiers
# list() crée la liste correspondante
# [0] + ... ajoute un zéro au début de la liste (décalage pour faciliter l'indexation à partir de 1)
a = [0] + list(map(int, input().split()))

# Initialisation d'une liste 's' contenant un seul élément 0
# Cette liste contiendra les sommes préfixées du tableau 'a'
s = [0]

# Initialisation d'une liste 'p' avec un seul élément 0
# Cette liste contiendra les sommes préfixées du maximum entre 0 et chaque élément de 'a'
# Autrement dit, la somme des éléments positifs du tableau jusqu'à un certain index
p = [0]

# Boucle allant de 1 à n inclus avec 'i' comme variable d'itération
# Cette boucle va construire les listes de préfixes 's' et 'p'
for i in range(1, n + 1):
    # Calcul et ajout de la somme préfixée courante au tableau 's'
    # s[i] = s[i-1] + a[i]
    s.append(s[i - 1] + a[i])
    
    # Calcul de la somme préfixée des valeurs positives uniquement
    # max(0, a[i]) permet de ne prendre que les valeurs positives (ou zéro) de 'a'
    # p[i] = p[i-1] + max(0, a[i])
    p.append(p[i - 1] + max(0, a[i]))

# Initialisation de la variable 'ans' à 0
# Cette variable gardera en mémoire le maximum trouvé selon le critère du problème
ans = 0

# Boucle pour examiner toutes les sous-séquences contiguës de longueur k dans le tableau 'a'
# La boucle va de i = 1 jusqu'à i = n - k + 1 inclus (d'où le +2 car range s'arrête avant le dernier)
for i in range(1, n - k + 2):
    # Calcul de la somme des éléments du sous-tableau de longueur k commençant à l'indice i
    # s[i+k-1] - s[i-1] donne la somme des éléments de a[i] à a[i+k-1]
    # max(0, ...) prend la valeur maximale entre zéro et cette somme
    t = max(0, s[i + k - 1] - s[i - 1])
    
    # On ajoute à 't' la somme de toutes les valeurs positives en dehors de la fenêtre courante
    # p[i-1] est la somme des positifs avant l'intervalle (avant l'indice i)
    # p[n] est le total de tous les positifs dans 'a'
    # p[i+k-1] est la somme des positifs jusqu'à la fin de la fenêtre, donc p[n] - p[i+k-1] donne ceux après la fenêtre
    # On fait donc p[i-1] + (p[n] - p[i+k-1]) pour obtenir la somme des positifs hors de la fenêtre
    t += p[i - 1] + p[n] - p[i + k - 1]
    
    # Mise à jour de la valeur maximale obtenue jusque-là
    # max(ans, t) donne le maximum entre la valeur actuelle d'ans et la nouvelle valeur t
    # On affecte ce maximum à 'ans'
    ans = max(ans, t)

# Affichage de la réponse finale qui consiste en la meilleure somme possible suivant le calcul spécifique
print(ans)