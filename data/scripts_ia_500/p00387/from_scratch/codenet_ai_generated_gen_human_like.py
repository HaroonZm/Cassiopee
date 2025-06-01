A, B = map(int, input().split())
# On veut minimiser la fréquence maximale d'utilisation d'une robe
# Donc on répartit les B fêtes sur A robes de manière équilibrée
# Cela correspond à faire un plafond de B/A
result = (B + A - 1) // A  # division entière vers le haut
print(result)