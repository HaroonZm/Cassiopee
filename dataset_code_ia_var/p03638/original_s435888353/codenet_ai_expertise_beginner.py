H, W = map(int, input().split())
N = int(input())
a_list = list(map(int, input().split()))

# Créer une liste avec chaque couleur et sa quantité
draw_order = []
for i in range(N):
    for _ in range(a_list[i]):
        draw_order.append(i + 1)

# Dessiner la grille
for row in range(H):
    start = row * W
    end = (row + 1) * W
    if row % 2 == 0:
        current_row = draw_order[start:end]
    else:
        current_row = draw_order[start:end][::-1]
    # Afficher la ligne avec des espaces
    print(' '.join(str(num) for num in current_row))