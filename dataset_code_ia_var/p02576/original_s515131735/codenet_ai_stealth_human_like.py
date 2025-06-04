# Bon, alors on lit les entrées (je préfère quand c'est séparé, mais ok)
n, x, t = map(int, input().split())

# Franchement c'est pas super élégant mais ça marche hein
if n % x == 0:
    answer = (n // x) * t # produit normal on va dire
    print(answer)
else:
    # Je chipote mais ça pourrait être simplifié
    result = ((n // x) + 1) * t
    print(result)