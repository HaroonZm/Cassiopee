# Vérifie si ce script Python est exécuté directement, et non importé comme un module. 
# Cela est utile pour contrôler l'exécution du code principal du programme.
if __name__ == "__main__":
    # Demande à l'utilisateur d'entrer deux valeurs séparées par un espace sur une même ligne.
    # La fonction input() lit une ligne comme une chaîne. 
    # split() divise cette chaîne en une liste de sous-chaînes en utilisant l’espace comme séparateur.
    # map(lambda x: int(x), ...) convertit chaque sous-chaîne (qui représente un nombre) en entier.
    # L'unpacking avec N, K stocke les deux valeurs obtenues respectivement dans N et K.
    N, K = map(lambda x: int(x), input().split())
    
    # Demande ensuite à l'utilisateur d'entrer N valeurs (ou plus), formant la liste.
    # input().split() lit la ligne d'entrée et la divise en morceaux (str) selon les espaces.
    # map(lambda x: int(x), ...) convertit chaque morceau en entier.
    # list(...) transforme directement le résultat d'un objet map en liste Python classique.
    a = list(map(lambda x: int(x), input().split()))
    
    # Initialise la variable ans avec N + 1, une valeur plus grande que n'importe quelle possible sous-séquence
    # Cela permet de toujours garder le minimum recherché.
    ans = N + 1

    # idx représente un index secondaire pour parcourir la liste, initialisé à 0.
    idx = 0

    # num compte, à tout moment, combien de différentes valeurs entre 1 et K sont actuellement
    # présentes au moins une fois dans la "fenêtre" (sous-séquence considérée).
    num = 0

    # values est une liste de taille K, initialisée avec des zéros.
    # Chaque case correspond au nombre d'occurrences du nombre (i+1) dans la fenêtre courante.
    values = [0] * K

    # La boucle for s'incrémente sur s variant de 0 à N-1: s est l'index du début de la fenêtre considérée.
    for s in range(N):
        # Boucle while interne permet d'élargir la fenêtre vers la droite (idx) aussi longtemps que :
        # - l'index droit ne dépasse pas la taille du tableau (idx < N)
        # - le nombre total de valeurs différentes présentes num reste inférieur à K
        while (idx < N and num < K):
            # Récupère la valeur à l'index idx dans a.
            v = a[idx]
            # Vérifie si la valeur v est dans la plage 1 à K (v <= K)
            if (v <= K):
                # Accroît le compteur pour v dans la fenêtre.
                values[v - 1] += 1
                # Si c'est la première apparition de v (le compteur est passé de 0 à 1)
                # alors on a trouvé une nouvelle valeur distincte.
                if (1 == values[v - 1]):
                    num += 1
            # On déplace l'index droit de la fenêtre d'une case
            idx += 1
        
        # Si tous les nombres de 1 à K sont présents au moins une fois dans la fenêtre courante,
        # c'est-à-dire si num == K, alors on peut comparer la longueur de cette fenêtre à la
        # meilleure (plus petite) trouvée jusque-là et conserver la plus courte.
        if (K == num):
            ans = min(ans, idx - s)
        
        # On va maintenant "rétrécir" la fenêtre du côté gauche en retirant l'élément a[s]
        v = a[s]
        # Encore une fois, ne considérer que les valeurs v de 1 à K
        if (v <= K):
            # Diminue le compteur de v car on la retire de la fenêtre.
            values[v - 1] -= 1
            # Si maintenant le compteur pour v tombe à zéro, cela signifie qu'il ne
            # reste plus de v dans la fenêtre, donc num diminue aussi.
            if (0 == values[v - 1]):
                num -= 1
    
    # A la fin, si aucune sous-séquence n’a été trouvée (ans reste à sa valeur initiale)
    # on affiche 0, sinon la longueur minimale trouvée (ans).
    ans = ans if ans < N + 1 else 0
    print(ans)