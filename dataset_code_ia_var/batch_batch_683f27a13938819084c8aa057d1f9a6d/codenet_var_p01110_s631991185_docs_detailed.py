import sys
input = sys.stdin.readline

def main():
    """
    Contrôle la boucle principale du programme. Pour chaque jeu de paramètres, construit et met à jour une table dynamique
    permettant de calculer des valeurs selon des opérations de découpe successives, puis répond à des requêtes.
    Termine l'exécution si tous les paramètres d'entrée sont nuls.
    """
    while True:
        # Lecture du cas de test : n, m, t, p
        n, m, t, p = map(int, input().split())
        
        # Condition d'arrêt : si tous les paramètres sont 0, quitter le programme
        if [n, m, t, p] == [0, 0, 0, 0]:
            exit()
        
        # Initialisation de la table DP (programmation dynamique)
        # La taille allouée est suffisamment grande pour stocker tous les sous-rectangles créés après découpes
        dp = [[0] * (m * m + 1) for _ in range(n * n + 1)]
        
        # Définition des coordonnées courantes du rectangle considéré (coin supérieur gauche et coin inférieur droit exclus)
        sx = 0  # décalage en ligne (x)
        sy = 0  # décalage en colonne (y)
        ex = n  # nb de lignes considérées
        ey = m  # nb de colonnes considérées
        
        # Initialiser la zone de dp correspondant au rectangle d'origine avec 1 (point de départ pour la DP)
        for i in range(n):
            for j in range(m):
                dp[sx + i][sy + j] = 1
        
        # Traiter les t opérations de découpe successives
        for i in range(t):
            d, c = map(int, input().split())
            if d == 1:
                # Découpe horizontale : additionner la partie du haut sur celle du bas
                for k in range(c):
                    for j in range(sy, ey):
                        # Propager la valeur du rectangle du dessus vers celui du dessous
                        dp[sx + c + k][j] += dp[sx + c - k - 1][j]
                # Décalage du coin supérieur
                sx += c
                # Mise à jour de la borne inférieure droite si nécessaire
                ex = max(ex, sx + c)
            else:
                # Découpe verticale : additionner la partie de gauche sur celle de droite
                for k in range(c):
                    for j in range(sx, ex):
                        # Propager la valeur du rectangle de gauche vers la droite
                        dp[j][sy + c + k] += dp[j][sy + c - k - 1]
                # Décalage du coin gauche
                sy += c
                # Mise à jour de la borne inférieure droite si nécessaire
                ey = max(ey, sy + c)
        
        # Pour chaque requête, on affiche la valeur calculée dans la table dp à la position décalée correspondante
        for i in range(p):
            x, y = map(int, input().split())
            # Accès à la valeur à la position (sx + x, sy + y)
            res = dp[sx + x][sy + y]
            print(res)
            
main()