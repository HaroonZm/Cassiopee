def run():
  # Lire deux entiers D et N depuis l'entrée standard.
  # map(int, input().split()) applique la fonction int à chaque élément produit par input().split()
  # input() lit une ligne de texte, split() divise cette ligne en mots (séparés par des espaces).
  # Résultat: D = nombre de jours, N = nombre de vêtements possibles.
  D, N = map(int, input().split())

  # Lire D entiers, un par ligne, représentant la température de chaque jour.
  # Utilisation de la compréhension de liste: 
  # pour chaque indice d allant de 0 à D-1, on exécute int(input()) et on ajoute le résultat à la liste d_li.
  d_li = [int(input()) for d in range(D)]

  # Lire N lignes, chacune contenant 3 entiers séparés par des espaces.
  # Chaque ligne représente les caractéristiques d'un vêtement: a (température minimale), b (température maximale), c (niveau de confort).
  # map(int, input().split()) convertit chaque ligne en une liste de 3 entiers.
  # list(map(...)) transforme l'objet map en liste.
  clothe_li = [list(map(int, input().split())) for n in range(N)]

  # Initialiser une matrice dp (programming dynamique) de dimensions D x N remplie de zéros.
  # Chaque élément dp[d][n] correspondra à la valeur maximale accumulée du confort jusqu'au jour d en portant le vêtement n ce jour-là.
  # [[0]*N for d in range(D)] crée une liste de D listes, chacune contenant N zéros.
  dp = [[0]*N for d in range(D)]

  # Initialisation pour le premier jour (index 0).
  d = d_li[0]  # Temperature du premier jour.
  # Parcourir tous les vêtements pour vérifier si chacun peut être porté ce jour-là.
  for n, (a, b, c) in enumerate(clothe_li):
    # Vérifier que la température du jour est dans l'intervalle acceptable [a, b] du vêtement.
    if (a <= d) and (d <= b):
      # Si le vêtement est portable ce jour-là, mettre dp[0][n] à 1.
      # Cela signifie qu'on peut commencer avec ce vêtement avec un confort initial de 1.
      dp[0][n] = 1

  # Boucle principale pour les jours suivants, allant du deuxième jour (index 1) au dernier (index D-1).
  for i in range(1, D):
    d = d_li[i]  # Température du jour actuel.
    # Pour chaque vêtement porté la veille (précédent jour i-1), vérifier les options pour aujourd'hui.
    for pre_n in range(N):
      # Si aucun chemin valide jusqu'au vêtement pré_n la veille, on ignore.
      if dp[i-1][pre_n] == 0: 
        continue  # Passer au vêtement suivant.
      # Parcourir tous les vêtements possibles pour le jour actuel.
      for n, (a, b, c) in enumerate(clothe_li):
        # Vérifier si le vêtement n est portable aujourd'hui selon la température d.
        if (a <= d) and (d <= b):
          # Calculer la valeur maximale possible pour dp[i][n].
          # On regarde la meilleure valeur actuelle pour dp[i][n], et on la compare au chemin passant par pre_n la veille plus le "coût"
          # du changement de vêtement, calculé ici comme la valeur précédente dp[i-1][pre_n] plus l'absolu de la différence de confort entre le vêtement de la veille (pre_n) et celui d'aujourd'hui (n).
          dp[i][n] = max(dp[i][n], 
                         dp[i-1][pre_n] + abs(clothe_li[pre_n][2] - c))
          # Ici, clothe_li[pre_n][2] donne le confort du vêtement porté la veille, c est le confort du vêtement actuel.
          # abs() calcule la valeur absolue de la différence, représentant une sorte de "variation de confort".

  # À la fin, on cherche la valeur maximale dans la dernière ligne de dp, 
  # ce qui représente le meilleur score total après le dernier jour.
  # Puis on soustrait 1 car l'initialisation des premiers vêtements a été faite avec 1 pour faciliter les calculs.
  print(max(dp[-1])-1)
    
# Condition pour exécuter run() seulement si ce fichier est le programme principal exécuté,
# évitant d'exécuter la fonction si le module est importé ailleurs.
if __name__ == '__main__':
  run()