# Cette ligne récupère une entrée de l'utilisateur sous forme de chaîne de caractères,
# puis la convertit en un entier (int) et la stocke dans la variable n.
# La fonction input() attend que l'utilisateur entre une donnée puis appuie sur Entrée.
n = int(input())

# De même, cette ligne prend une autre entrée utilisateur, convertit en entier,
# et la stocke dans la variable m.
m = int(input())

# Ici, on crée une liste à deux dimensions (une matrice) nommée K.
# Cette matrice a 32 lignes et 32 colonnes.
# Chaque élément de cette matrice est initialisé avec la valeur 10^9 (un grand nombre).
# Cette valeur sert souvent comme "infini" dans des algorithmes de graphe
# pour indiquer qu'il n'y a pas encore de chemin connu entre deux points.
# La compréhension de liste imbriquée agit ainsi :
# - La boucle intérieure crée une liste de 32 éléments à 10^9.
# - La boucle extérieure crée 32 de ces listes, formant une matrice 32x32.
K = [[10**9 for one in range(32)] for two in range(32)]

# Cette boucle s'exécute m fois, c'est-à-dire autant de fois qu'il y a de données à lire.
# La variable three est un compteur allant de 0 à m-1.
for three in range(m):
    # On attend une entrée utilisateur d'une ligne contenant quatre entiers séparés par des virgules.
    # La fonction input() récupère cette ligne sous forme de chaîne.
    # La méthode split(",") divise la chaîne à chaque virgule, produisant une liste de chaînes de chiffres.
    # La fonction map(int, ...) convertit chaque élément de cette liste en entier.
    # Les quatre entiers ainsi obtenus sont assignés aux variables a, b, c, d.
    a,b,c,d = map(int,input().split(","))
    
    # Ici on met à jour la matrice K aux positions [a][b] et [b][a].
    # Ces positions correspondent aux poids des arêtes dans un graphe orienté ou non orienté.
    # K[a][b] = c signifie que le poids du chemin allant de a à b est c.
    K[a][b] = c
    # K[b][a] = d signifie que le poids du chemin allant de b à a est d.
    # Cela peut représenter un graphe avec des poids différents dans chaque direction.
    K[b][a] = d

# On commence ici l'algorithme de Floyd-Warshall,
# un algorithme permettant de calculer les plus courts chemins entre toutes paires de sommets dans un graphe.
# La variable k représente le "sommet intermédiaire" actuellement considéré.
for k in range(1,n+1):
    # La variable j parcourt les sommets cibles possibles.
    for j in range(1,n+1):
        # La variable i parcourt les sommets sources possibles.
        for i in range(1,n+1):
            # La condition vérifie si le chemin passant par le sommet intermédiaire k
            # est plus court que le chemin direct actuel entre i et j.
            # K[i][k] est la distance la plus courte connue entre i et k.
            # K[k][j] est la distance la plus courte connue entre k et j.
            # Si la somme de ces deux chemins est inférieure à K[i][j],
            # alors on peut améliorer le chemin entre i et j en passant par k.
            if K[i][j] > K[i][k] + K[k][j]:
                # Mise à jour du chemin le plus court entre i et j.
                K[i][j] = K[i][k] + K[k][j]

# On lit ici quatre entiers à partir d'une entrée utilisateur.
# Ces valeurs sont séparées par des virgules dans la saisie.
# s, g, V, P vont donc contenir ces quatre entiers respectivement.
s,g,V,P = map(int,input().split(","))

# Enfin, on calcule une expression et on l'affiche.
# Cette expression est : V - P - K[s][g] - K[g][s]
# En supposant que K[s][g] est la distance la plus courte entre s et g,
# et K[g][s] celle entre g et s,
# on soustrait ces deux distances ainsi que P de la valeur V.
# La fonction print() affiche le résultat à l'écran.
print(V-P-K[s][g]-K[g][s])