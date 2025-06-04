# Importation de la classe Counter depuis le module collections.
# Counter sert à compter le nombre d'occurrences de chaque élément dans une séquence.
from collections import Counter

# Définition d'une constante MOD dont la valeur est 998244353.
# Cette constante est utilisée pour effectuer des calculs de modulo afin d'éviter les dépassements d'entiers.
MOD = 998244353

# Lecture d'une valeur entière depuis l'entrée standard, correspondant au nombre d'éléments du tableau D.
# La fonction input() lit une ligne de texte, int() la convertit en entier.
N = int(input())

# Lecture d'une ligne contenant N entiers séparés par des espaces.
# input() lit la ligne, split() la découpe en une liste de chaînes, map(int, ...) convertit chaque chaîne en entier.
# list(...) crée une liste à partir du résultat.
D = list(map(int, input().split()))

# Création d'un objet Counter "C" à partir de la liste D.
# Cela va associer à chaque valeur de D le nombre de fois où elle apparaît.
C = Counter(D)

# Vérification que la première valeur de la liste D est 0.
# Cela s'écrit D[0] != 0, ce qui teste si le premier élément de D n'est pas 0.
# Vérification que le nombre d'occurrences de 0 dans la liste D est strictement égal à 1.
# Cela s'écrit C[0] != 1.
if D[0] != 0 or C[0] != 1:
    # Si au moins une des conditions précédentes n'est pas respectée,
    # alors la sortie doit être 0 selon l'énoncé du problème.
    print(0)
    # exit() arrête immédiatement l'exécution du script.
    exit()

# Initialisation de la variable ans à 1. Cette variable contiendra la réponse finale.
ans = 1

# La boucle for va parcourir tous les entiers i allant de 1 jusqu'à la valeur maximale de D incluse.
# range(1, max(D)+1) génère cette séquence.
for i in range(1, max(D)+1):
    # Si la valeur "i" n'est pas présente dans la liste D (c'est-à-dire si son compte est 0 dans Counter),
    # alors cela signifie que la structure demandée n'est pas correcte.
    if C[i] == 0:
        # On affecte 0 à la réponse finale pour indiquer un cas impossible.
        ans = 0
        # On sort prématurément de la boucle car le calcul ne sert plus à rien.
        break
    else:
        # Si la valeur "i" est bien présente, on effectue le calcul suivant :
        # On multiplie la réponse courante "ans" par C[i-1] élevé à la puissance C[i], modulo MOD.
        # pow(a, b, c) calcule (a**b) % c de façon efficace, même pour de grandes valeurs.
        ans *= pow(C[i-1], C[i], MOD)
        # On applique le modulo à la variable ans après chaque multiplication pour éviter toute surcharge mémoire.
        ans %= MOD

# Une fois la boucle terminée, on affiche la réponse finale.
print(ans)