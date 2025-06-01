# Solution complète en Python avec commentaires détaillés

# Problème résumé :
# On doit construire une tour à la position t sur une ligne (1D).
# Sur cette ligne, il existe N bâtiments situés avant t (x_i < t) chacun avec une hauteur h_i.
# Le château ("Keep") est à l'origine (x=0) avec une hauteur supposée nulle à la base.
# La tour doit être suffisamment haute pour que depuis son sommet,
# on puisse "voir" la base du château sans que la vue soit bloquée par un bâtiment.
# "Voir le château en entier" signifie que la ligne de vue partant du sommet de la tour (à t, hauteur H)
# jusqu'au bas du château (à 0, hauteur 0) ne doit pas intersecter aucun bâtiment (en particulier leurs hauteurs).
# On veut trouver la hauteur minimale H de la tour qui satisfera cette condition.

# Pour cela, on remarque que la ligne de vue est une droite entre (t, H) et (0, 0).
# La hauteur de la ligne de vue en un position x est y(x) = H * x / t.
# Pour que la vue ne soit pas bloquée, pour tout bâtiment i à position x_i, il faut que
# la hauteur du bâtiment h_i < y(x_i) (les intersections au sommet des bâtiments sont autorisées)

# On peut donc inverser la condition pour chaque bâtiment :
# h_i < H * x_i / t  <=>  H > h_i * t / x_i
# La tour doit avoir une hauteur au moins égale au maximum de ces valeurs,
# c’est-à-dire max(h_i * t / x_i) pour i=1..N

# On calcule donc max(h_i * t / x_i) et on le retourne.

# Remarques :
# - On peut retourner un float avec une précision suffisante (erreur ≤ 10^-3)
# - Pas besoin de considérer la hauteur finale du château car on veut voir sa base, qui est à hauteur 0.
# - On suppose qu'il y a au moins un bâtiment (N≥1) et qu'ils sont tous situés entre 1 et t-1.

def main():
    import sys
    
    input = sys.stdin.readline
    
    # Lecture des paramètres initiaux
    N, t = map(int, input().split())
    max_height_required = 0.0
    
    for _ in range(N):
        x_i, h_i = map(int, input().split())
        # Calcul de la hauteur minimal requise à partir de ce bâtiment
        # H > h_i * t / x_i
        required_height = (h_i * t) / x_i
        if required_height > max_height_required:
            max_height_required = required_height
    
    # Affichage du résultat avec une précision suffisante
    # On formatte pour que l'erreur soit ≤ 10^-3
    print(f"{max_height_required:.6f}")

if __name__ == "__main__":
    main()