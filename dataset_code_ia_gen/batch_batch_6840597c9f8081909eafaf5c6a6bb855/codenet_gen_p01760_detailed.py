# Lecture des entrées
T, D = map(int, input().split())
tA, tB = map(int, input().split())
dA, dB = map(int, input().split())

# Initialisation de la meilleure différence (grande valeur car on souhaite minimiser)
min_diff = float('inf')

# Parcours de toutes les combinaisons possibles de débits pour A et B
# a et b sont des entiers multiplicateurs des pas dA et dB respectivement
# On cherche toutes les combinaisons avec 1 <= a*dA + b*dB <= D
for a in range(D // dA + 1):  # de 0 à max possible pour A
    for b in range(D // dB + 1):  # de 0 à max possible pour B
        total_flow = a * dA + b * dB

        # Vérifier que le débit total est dans la plage valide
        if total_flow == 0:
            # Pas de débit, donc pas d'eau qui coule, on continue
            continue
        if total_flow > D:
            # Débit trop élevé, on ignore
            continue

        # Calcul de la température moyenne du mélange
        # (tA * vA + tB * vB) / (vA + vB)
        # ici vA = a * dA, vB = b * dB
        temp = 0
        if total_flow > 0:
            temp = (tA * (a * dA) + tB * (b * dB)) / total_flow

        # Calcul de la différence absolue avec la température cible
        diff = abs(temp - T)

        # Mise à jour de la différence minimale
        if diff < min_diff:
            min_diff = diff

# Affichage du résultat avec 10 décimales
print(f"{min_diff:.10f}")