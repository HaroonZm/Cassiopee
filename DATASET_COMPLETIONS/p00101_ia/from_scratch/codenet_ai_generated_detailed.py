# Lire le nombre de jeux de données
n = int(input())

# Pour chaque ligne de texte,
# remplacer toutes les occurrences exactes de "Hoshino" par "Hoshina"
for _ in range(n):
    line = input()
    # La méthode str.replace remplace toutes les occurrences dans la chaîne
    # Cela correspond exactement à la consigne
    corrected_line = line.replace("Hoshino", "Hoshina")
    print(corrected_line)