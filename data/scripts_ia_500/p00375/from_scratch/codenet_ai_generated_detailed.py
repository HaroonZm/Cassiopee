# Lecture de la température en Fahrenheit depuis l'entrée standard (entrée utilisateur)
F = int(input())

# Application de la formule simplifiée pour convertir Fahrenheit en Celsius
# C = (F - 30) / 2
C = (F - 30) // 2  # Utilisation de la division entière car le résultat est attendu en entier

# Affichage de la température convertie en Celsius
print(C)