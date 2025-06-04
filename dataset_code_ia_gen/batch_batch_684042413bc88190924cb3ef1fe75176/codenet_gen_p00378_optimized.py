A, B, X = map(int, input().split())
min_price = float('inf')
# Parcours possible du nombre de bouteilles 1L nécessaires de 0 à X//1000+2 (au cas où on dépasse)
for i in range(X // 1000 + 2):
    remaining = X - i * 1000
    # Si la quantité est négative, on peut acheter uniquement i bouteilles 1L car on a déjà assez
    if remaining <= 0:
        price = i * A
    else:
        # Calcul des bouteilles 0.5L nécessaires en arrondissant vers le haut
        j = (remaining + 499) // 500
        price = i * A + j * B
    if price < min_price:
        min_price = price
print(min_price)