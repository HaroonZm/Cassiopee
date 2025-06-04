import sys  # Importe le module système, utilisé ici pour l'entrée standard

# Redéfinit la fonction input afin d'utiliser sys.stdin.readline, 
# qui lit une ligne depuis l'entrée standard et est généralement plus rapide
input = sys.stdin.readline

def Solve():
    # Initialise la variable 'ans' à 0. Cette variable va servir à accumuler le résultat final de la fonction.
    ans = 0
    # On parcourt tous les indices de 0 à n-1 grâce à la fonction range.
    for i in range(n):
        # Si la case V[i] vaut True, cela signifie que l'indice 'i' a déjà été visité.
        if V[i]:
            # On passe au tour suivant de la boucle sans rien faire pour cet 'i' déjà traité.
            continue
        # On initialise 'cur' à 'i'. 'cur' va représenter l'indice courant du parcours.
        cur = i
        # On initialise 'S' à 0 : il servira à additionner certaines valeurs du tableau 'A'.
        # On initialise 'an' à 0, compteur du nombre d'éléments dans le cycle (ou la séquence que l'on parcourt).
        S, an = 0, 0
        # On initialise 'm' à la valeur maximale possible (VMAX), ce qui facilitera la recherche du minimum.
        m = VMAX
        # On entre dans une boucle infinie qui ne se cassera que via 'break'.
        while True:
            # Marque le sommet 'cur' comme visité pour éviter de le traiter plusieurs fois.
            V[cur] = True
            # Incrémente le compteur d’éléments du cycle.
            an += 1
            # Récupère la valeur associée au sommet courant.
            v = A[cur]
            # Met à jour le minimum rencontré dans le cycle jusque-là.
            m = min(m, v)
            # Ajoute la valeur courante à la somme totale S pour ce cycle.
            S += v
            # Se déplace vers le prochain indice dans la permutation, déterminé par le tableau T.
            cur = T[v]
            # Si le prochain indice est déjà visité, on a bouclé le cycle et on peut sortir.
            if V[cur]:
                break
        # Calcule le coût pour ce cycle en prenant le minimum entre deux stratégies et ajoute à l'accumulateur général.
        # (S + (an-2)*m) est une stratégie, (m + S + (an+1)*s) en est une autre; on choisit la moins chère.
        ans += min(S + (an - 2) * m, m + S + (an + 1) * s)
    # Après avoir traité tous les cycles, on retourne la valeur globale accumulée.
    return ans

# Définit la constante MAX à 1000, qui servira pour la taille du tableau V.
MAX = 1000
# Définit la constante VMAX à 10000. Cela représente un maximum utilisé pour la taille du tableau T et la valeur initiale de m.
VMAX = 10000

# Lit un entier depuis l'entrée standard, qui sera le nombre total d'éléments dans la liste A.
n = int(input())
# Lit une ligne, la découpe en éléments (split()), les convertit tous en int, puis les place dans la liste A.
A = [int(x) for x in input().split()]
# Calcule le plus petit élément de la liste A, et le stocke dans la variable 's'.
s = min(A)
# Trie la liste A et stocke le résultat dans B. 'sorted' retourne une nouvelle liste.
B = sorted(A)
# Initialise la liste T avec une taille de VMAX+1 éléments, remplie de 0.
# T servira à déterminer, pour chaque valeur, son nouvel indice dans la séquence triée.
T = [0] * (VMAX + 1)
# Boucle sur tous les indices et valeurs du tableau trié B pour remplir T.
for i, b in enumerate(B):
    # Pour chaque valeur b, T[b] est mis à jour à l'indice i dans la liste triée.
    # Ce tableau permet de savoir à quelle position chaque valeur se trouve une fois le tableau trié.
    T[b] = i
# Initialise la liste V de taille MAX à False; chaque case indique si l'indice en question a été traité.
V = [False] * MAX
# Appelle la fonction Solve() et stocke le résultat dans la variable 'ans'.
ans = Solve()
# Affiche la variable ans, qui contient le résultat final calculé par Solve().
print(ans)