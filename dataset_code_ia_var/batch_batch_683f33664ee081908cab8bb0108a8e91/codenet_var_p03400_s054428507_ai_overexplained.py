# Demande à l'utilisateur de saisir une valeur entière et l'assigne à la variable N.
# Cette valeur N représente le nombre d'éléments ou le nombre de participants.
N = int(input())

# Demande à l'utilisateur de saisir deux entiers séparés par un espace.
# Utilise la compréhension de liste pour parcourir chaque élément issu du split de la chaîne saisie.
# Convertit chaque élément (chaîne de caractères) en entier.
# Le premier entier est assigné à la variable D, et le second à X.
D, X = [int(x) for x in input().split()]

# Utilise une compréhension de liste pour répéter N fois la saisie d'un entier par l'utilisateur.
# input() prend la saisie, int() la convertit en entier, puis la liste finale A contient ces N entiers.
A = [int(input()) for _ in range(N)]

# Initialise la variable ans avec la valeur de X.
# Cette variable stocke le résultat final, initialisé avec la valeur de X.
ans = X

# Démarre une boucle for pour itérer sur une séquence de nombres de 0 à N-1 inclus.
# i représente l'indice courant dans la liste A.
for i in range(N):
    # Initialise une variable a à 1.
    # Cette variable représente le prochain jour de participation d'un participant.
    a = 1
    # Initialise une variable l à 1.
    # Cette variable représente le nombre d'intervalles ajoutés dans la formule du jour.
    l = 1
    # Utilise une boucle while pour répéter les instructions tant que a est inférieur ou égal à D.
    while a <= D:
        # Incrémente la variable ans de 1, en ajoutant une participation pour ce jour précis.
        ans += 1
        # Calcule la prochaine valeur de a, qui représente le prochain jour où le participant fera l'action.
        # La formule utilise l'élément courant de la liste A, multiplié par l, et ajouté à 1.
        a = l * A[i] + 1
        # Incrémente la variable l de 1 pour le passage au prochain intervalle.
        l += 1

# Affiche la valeur finale de ans, qui contient le résultat total attendu.
print(ans)