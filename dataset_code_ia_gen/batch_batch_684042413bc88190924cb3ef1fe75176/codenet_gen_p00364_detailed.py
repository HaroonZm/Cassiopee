# Solution au problème "Bange Hills Tower"
# L'objectif est de déterminer la hauteur minimale de la tour pour que la ligne de vue depuis le sommet de la tour jusqu'au bas du donjon (au sol, position 0 hauteur 0)
# ne soit obstruée par aucun bâtiment.

# Approche :
# - Le donjon est à la position 0, et la tour est à la position t sur l'axe horizontal.
# - On cherche la hauteur H de la tour pour que la droite entre (t, H) et (0, 0) ne coupe aucun bâtiment.
# 
# Modélisation :
# - Pour chaque bâtiment situé en x_i (0 < x_i < t) avec hauteur h_i,
#   la hauteur de la vue à x_i est donnée par l'équation de la droite entre (t,H) et (0,0):
#   y = H * (t - x) / t
# - Pour que le bâtiment ne cache pas la vue, il faut h_i < y (le bâtiment doit être strictement en-dessous de la ligne de vue),
#   ou h_i <= y si l'intersection en hauteur sur le sommet est acceptée, mais ici on exclue les intersections sauf au sommet de la tour.
# - Comme la hauteur du donjon en 0 est 0, la droite passe par (0,0).
# 
# Calcul de H minimal :
# - Pour chaque bâtiment, on a : h_i < H * (t - x_i)/t  <=>  H > h_i * t / (t - x_i)
# - Le minimum H doit satisfaire toutes ces inégalité, donc :
#   H >= max_i (h_i * t / (t - x_i))
# 
# Remarque : on doit prendre la plus grande valeur de h_i * t/(t - x_i) parmi tous les bâtiments pour que la vue ne soit pas obstruée.
# 
# Implémentation :
# - Lire N, t
# - Pour chaque bâtiment, calculer h_i * t / (t - x_i)
# - Prendre le maximum de ces valeurs
# - Afficher le résultat avec une précision suffisante (double précision par défaut)
# 
# Cette méthode est efficace en O(N), suffisante pour N ≤ 1000.


N, t = map(int, input().split())

max_height = 0.0  # stockera la hauteur minimale requise

for _ in range(N):
    x_i, h_i = map(int, input().split())
    # Calcul de la hauteur limite pour cette building
    # attention division par (t - x_i), t > x_i toujours selon les contraintes
    needed_height = h_i * t / (t - x_i)
    if needed_height > max_height:
        max_height = needed_height

# Affichage du résultat, valeur minimale de la hauteur pour la tour
print(max_height)