# Demande à l'utilisateur d'entrer un nombre entier, puis convertit ce texte en un int (nombre entier).
# La fonction input() récupère une chaîne de caractères depuis l'entrée standard (clavier).
# int() convertit cette chaîne en un nombre entier, ce qui est nécessaire pour pouvoir utiliser cette valeur dans des calculs ou pour des boucles.
N = int(input())

# Demande à l'utilisateur d'entrer une chaîne de caractères et la stocke dans la variable s.
# input() renvoie toujours une chaîne de caractères, alors on n'a pas besoin de conversion ici.
s = input()

# De même, récupère une autre chaîne de caractères saisie par l'utilisateur et la stocke dans la variable t.
t = input()

# Création d'un dictionnaire nommé D.
# Un dictionnaire en Python est une structure de données qui stocke des paires clé-valeur.
# Ici, on initialise le dictionnaire avec une clé qui est le dernier caractère de la chaîne t (t[-1]).
# t[-1] signifie "le dernier élément de la chaîne t", car les indices négatifs commencent à la fin.
# La valeur associée à cette clé est 1.
# Ce dictionnaire va être utilisé pour stocker des fréquences ou des comptes associés aux caractères.
D = {t[-1]: 1}

# Démarrage d'une boucle for.
# range(N-2, 0, -1) génère une séquence de nombres commençant à N-2, s'arrêtant avant 0, en décrémentant de 1 à chaque itération.
# Cela signifie que la boucle va parcourir les indices dans l'ordre décroissant de N-2 jusqu'à 1 (inclus).
# Par exemple, si N=5, la boucle i prendra les valeurs 3, 2, 1.
for i in range(N-2, 0, -1):

    # Récupération du caractère i-ème dans la chaîne s et le stocke dans la variable si.
    # Cela permet d'accéder directement à un caractère spécifique dans la chaîne via son indice.
    si = s[i]

    # De la même manière, récupère le caractère i-ème dans la chaîne t et le stocke dans ti.
    ti = t[i]

    # Recherche dans le dictionnaire D de la valeur associée à la clé 'si'.
    # La méthode get() permet de récupérer la valeur correspondant à une clé.
    # Si la clé 'si' n'existe pas, get() retourne 0 par défaut grâce à l'argument 0.
    v = D.get(si, 0)

    # Dans le dictionnaire D, associe à la clé 'ti' la somme de l'ancienne valeur associée à 'ti' (ou 0 si elle n'existe pas)
    # plus la valeur v calculée précédemment.
    # Le résultat est pris modulo 10**9+7, ce qui est un grand nombre premier souvent utilisé pour éviter les débordements et pour des calculs modulo en informatique.
    # Cela revient à mettre à jour une valeur comptable dans D liée au caractère ti.
    D[ti] = (D.get(ti, 0) + v) % (10**9+7)

# Enfin, affiche le résultat final en récupérant dans D la valeur associée au premier caractère de la chaîne s (s[0]).
# Si cette clé n'existe pas dans D, on retourne 0 par défaut.
# print() affiche la valeur sur la sortie standard, généralement l'écran.
print(D.get(s[0], 0))