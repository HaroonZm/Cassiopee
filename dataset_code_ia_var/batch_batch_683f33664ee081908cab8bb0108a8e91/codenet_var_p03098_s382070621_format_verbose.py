# Entrée des paramètres de taille et du nombre d'opérations à effectuer
taille_permutation, nombre_operations = map(int, input().split())

# Lecture et transformation des permutations fournies en listes d'indices base 0
premiere_permutation = [int(valeur) - 1 for valeur in input().split()]
deuxieme_permutation = [int(valeur) - 1 for valeur in input().split()]

# Fonction pour appliquer une permutation 'ordre' sur la liste 'sequence'
def appliquer_permutation(sequence, ordre):
    return [sequence[ordre[indice]] for indice in range(taille_permutation)]

# Initialisation de la table des permutations composées
permutations_composées = [
    [0 for _ in range(taille_permutation)]
    for _ in range(6)
]

# Affectation des deux permutations de base
permutations_composées[0] = premiere_permutation
permutations_composées[1] = deuxieme_permutation

# Fonction pour calculer l'inverse d'une permutation
def inverse_permutation(permutation):
    resultat = [0] * taille_permutation
    for position in range(taille_permutation):
        resultat[permutation[position]] = position
    return resultat

# Construction des permutations successives par composition alternée
for indice_etape in range(4):
    permutation_suivante = appliquer_permutation(
        permutations_composées[indice_etape + 1], 
        inverse_permutation(permutations_composées[indice_etape])
    )
    permutations_composées[indice_etape + 2] = permutation_suivante

# Fonction récursive pour appliquer une permutation 'permutation' k fois efficacement
def exponentier_permutation(permutation, exposant):
    if exposant == 0:
        return list(range(taille_permutation))

    permutation_carrée = appliquer_permutation(permutation, permutation)
    demi_permutation = exponentier_permutation(permutation_carrée, exposant // 2)

    if exposant % 2 == 0:
        return demi_permutation
    else:
        return appliquer_permutation(demi_permutation, permutation)

# Étape 1 : Calcul de la permutation de départ à appliquer 'nombre_operations // 6' fois
permutation_de_base = appliquer_permutation(
    premiere_permutation,
    inverse_permutation(deuxieme_permutation)
)
permutation_de_base = appliquer_permutation(
    appliquer_permutation(
        deuxieme_permutation,
        inverse_permutation(premiere_permutation)
    ),
    permutation_de_base
)

# Application efficace du cycle principal
nombre_cycles = (nombre_operations - 1) // 6
permutation_apres_cycles = exponentier_permutation(permutation_de_base, nombre_cycles)

# Détermination de la permutation complémentaire finale
indice_permutation_complémentaire = (nombre_operations - 1) % 6
permutation_complémentaire = permutations_composées[indice_permutation_complémentaire]

# Application finale de la permutation correcte
resultat_final = appliquer_permutation(
    appliquer_permutation(permutation_apres_cycles, permutation_complémentaire),
    inverse_permutation(permutation_apres_cycles)
)

# Affichage de la permutation finale avec passage à l'indexation humaine (base 1)
affichage_resultat = [str(valeur + 1) for valeur in resultat_final]
print(" ".join(affichage_resultat))