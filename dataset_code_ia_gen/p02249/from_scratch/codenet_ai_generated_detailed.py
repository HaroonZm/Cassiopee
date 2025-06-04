# Lire les dimensions de la région
H, W = map(int, input().split())

# Lire la région ligne par ligne
region = [input() for _ in range(H)]

# Lire les dimensions du motif (pattern)
R, C = map(int, input().split())

# Lire le motif ligne par ligne
pattern = [input() for _ in range(R)]

# Liste pour stocker les coordonnées des occurrences trouvées
results = []

# Pour chaque position possible où le motif peut tenir dans la région
for i in range(H - R + 1):
    for j in range(W - C + 1):
        # Supposons que le motif est trouvé ici
        found = True
        # Vérifier chaque caractère du motif
        for r in range(R):
            # Extraire la sous-chaîne correspondante à la ligne r du motif dans la région
            if region[i + r][j:j + C] != pattern[r]:
                found = False
                break
        # Si le motif correspond parfaitement
        if found:
            results.append((i, j))

# Trier les résultats par numéro de ligne, puis colonne
results.sort(key=lambda x: (x[0], x[1]))

# Afficher les coordonnées des motifs trouvés
for coord in results:
    print(coord[0], coord[1])