modulo = 10**9+7  # Par souci de clarté, je mets modulo au lieu de MOD
n = int(input())  # On suppose que l'utilisateur entre bien un entier, pas de vérif :/

# On prépare le tableau 4D pour la DP - c'est vraiment lourd, mais bon...
dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(n+1)]
dp[0][3][3][3] = 1  # Cas initial, 333 : un peu magique honnêtement

# id lettres: A=0, G=1, C=2, T=3 (en vrai, on les code juste comme 0..3)

# Boucle sur la longueur de la chaîne
for i in range(n):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if not dp[i][j][k][l]:
                    continue   # Skip s'il n'y a rien à propager
                # essayer d'ajouter chaque nouvelle lettre à la suite
                for a in range(4):
                    # Quelques combinaisons interdites, il faudrait mieux faire ça, à revoir
                    if a == 2 and j == 1 and k == 0:  # AGC
                        continue
                    if a == 1 and j == 2 and k == 0:  # ACG
                        continue
                    if a == 2 and j == 0 and k == 1:  # GAC
                        continue
                    if a == 2 and j == 1 and l == 0:  # A?GC
                        continue
                    if a == 2 and k == 1 and l == 0:  # AG?C
                        continue
                    dp[i+1][a][j][k] = (dp[i+1][a][j][k] + dp[i][j][k][l]) % modulo  # modulo à chaque fois pour être sûr

# On somme tous les "états finaux" ; un peu pénible à lire, mais c'est explicit
answer = 0
for j in range(4):
    for k in range(4):
        for l in range(4):
            answer += dp[n][j][k][l]
answer %= modulo  # Normalisation du résultat, on oublie jamais le modulo normalement...
print(answer)