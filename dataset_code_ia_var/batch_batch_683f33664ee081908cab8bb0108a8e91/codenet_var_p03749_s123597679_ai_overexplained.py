import sys  # Importe le module sys qui fournit l'accès à certaines variables et fonctions utilisées ou maintenues par l'interpréteur Python

# sys.stdin.buffer.read, readline, readlines permettent de lire l'entrée standard (stdin) en mode binaire (octets)
# Cela permet une lecture rapide et sans gestion automatique des encodages, ce qui est utile en compétition
read = sys.stdin.buffer.read  # Alias vers la fonction read() sur le buffer d'entrée standard. Lit tout jusqu'à EOF
readline = sys.stdin.buffer.readline  # Alias pour lire une ligne complète depuis le buffer d'entrée standard
readlines = sys.stdin.buffer.readlines  # Alias pour lire toutes les lignes sous forme de liste d'octets depuis stdin

# Ici, on lit toute l'entrée, puis on la découpe selon les espaces, puis on convertit chaque morceau en entier grâce à map(int, ...)
N, M, *X = map(int, read().split())  # N = entier, M = entier, X = liste d'entiers représentant des positions découpées

MOD = 10 ** 9 + 7  # Définition de la constante du modulo, souvent utilisée pour éviter les dépassements d'entier

def mult(a, b, c, d, e, f):
    # Fonction qui multiplie deux polynômes de degré au plus 2 (représentés par leurs coefficients)
    # a, b, c sont les coefficients du premier polynôme (a + b*x + c*x^2)
    # d, e, f sont les coefficients du second polynôme (d + e*x + f*x^2)
    # On réalise la multiplication des deux polynômes, puis on réduit modulo le polynôme caractéristique 1 - 4x + 2x^2 - x^3
    # On effectue toutes les étapes du développement puis une réduction par rapport au polynôme caractéristique, étape par étape

    # Multiplication : on calcule tous les termes (on ignore x^3 et au-delà en réduisant après)
    a, b, c, d, e = a * d, a * e + b * d, a * f + b * e + c * d, b * f + c * e, c * f  # On instancie d, e comme variables temporaires
    # Ici, a, b, c représentent les coefficients pour x^0, x^1, x^2 jusqu'ici, d = coef de x^3, e = coef de x^4

    # Réduction modulo le polynôme caractéristique. Chaque fois qu'il y a du x^3, on remplace x^3 = 4x - 2x^2 + x^3 = 0 => x^3 = 4x - 2x^2
    b += e          # x^4 devient x* (x^3), donc on reporte e (x^4) sur b (x^1)
    c -= 4 * e      # x^4 = (x^3) * x = (4x - 2x^2) * x, ce qui donne des corrections sur c
    d += 2 * e      # x^4 impacte d (qui va être réduit encore après)
    e = 0           # On met e à zéro (plus de x^4)

    a += d          # x^3 est réduit comme x^0
    b -= 4 * d      # x^3 : -4x sur b
    c += 2 * d      # x^3 : +2x^2 sur c
    d = 0           # Plus de x^3

    # On applique le modulo sur chaque coefficient pour éviter les débordements et s'assurer que tout reste dans [0, MOD)
    a %= MOD
    b %= MOD
    c %= MOD

    # On renvoie les trois premiers coefficients réduits
    return a, b, c


# On prépare maintenant la table des puissances de l'inverse de x, modulo le polynôme caractéristique (1-4x+2x^2-x^3)
M = 10 ** 5  # Valeur maximale pour le pré-calcul

A1 = [0] * (M + 1)  # Liste pour mémoriser les puissances successives de (1/x) modulo le polynôme, taille M+1
a, b, c = 1, 0, 0   # Initialisation pour (1/x)^0 = 1

for i in range(M + 1):  # Pour chaque exposant de 0 à M inclus
    A1[i] = (a, b, c)  # On stocke le triplet de coefficients, i.e. la représentation polynomiale
    # Pour passer à (1/x)^(i+1), on multiplie le polynôme courant par (1/x) modulo le polynôme caractéristique
    # (1/x) * (a + b*x + c*x^2) = (b + 4*a) + (c - 2*a)*x + a*x^2
    a, b, c = b + 4 * a, c - 2 * a, a  # Mise à jour via la relation de récurrence
    a %= MOD  # On réduit chaque coefficient modulo MOD
    b %= MOD
    c %= MOD

# On prépare maintenant les puissances entières de (1/x) pour des multiples de M
A2 = [0] * (M + 1)  # Liste des puissances (1/x)^(M*i)
a, b, c = 1, 0, 0   # Initialisation pour la puissance 0
d, e, f = A1[M]     # (1/x)^M modulo polynôme caractéristique
for i in range(M + 1):  # Pour i de 0 à M
    A2[i] = (a, b, c)
    a, b, c = mult(a, b, c, d, e, f)  # On multiplie par (1/x)^M à chaque étape pour cumuler la puissance

def power(n):
    # Calcule la puissance (1/x)^n modulo le polynôme caractéristique
    # Utilise la décomposition n = q*M + r pour économiser du calcul avec la table (A1 et A2)
    q, r = divmod(n, M)  # Division entière pour obtenir quotient (q) et reste (r)
    a, b, c = A1[r]      # (1/x)^r
    d, e, f = A2[q]      # (1/x)^(M*q)
    return mult(a, b, c, d, e, f)  # Le résultat est le produit des deux puissances

# Ajout de N à la liste X. Cela simplifie la logique suivante car la boucle traite tous les points de coupure.
X.append(N)

# Initialisation des coefficients polynomiaux
# a, b, c représentent le polynôme courant, initialisé à x + x^2 (i.e. 0 + 1*x + 1*x^2)
a, b, c = 0, 1, 1

prev_x = 0  # Position de départ pour la première coupe/cas

for x in X:  # On parcourt tous les points de la liste X (y compris N qui vient d'être ajouté)
    # Pour chaque intervalle [prev_x, x], on élève le polynôme à la puissance (x - prev_x) via power()
    a, b, c = mult(a, b, c, *power(x - prev_x))  # On multiplie le polynôme courant par la puissance idoine
    b -= a  # Mise à jour selon la particularité du problème (soustraction du coefficient constant à b)
    c -= a  # Idem pour le terme de degré 2
    prev_x = x  # On avance à la prochaine position

# Le résultat final est le coefficient constant (degré 0) du polynôme après toutes les transitions
answer = a  # On stocke la réponse souhaitée dans "answer"

print(answer)  # Affiche la réponse finale calculée