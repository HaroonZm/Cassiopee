utilisateur_texte = input()

compte_lettre_K = utilisateur_texte.count('K')
compte_lettre_U = utilisateur_texte.count('U')
compte_lettre_P = utilisateur_texte.count('P')
compte_lettre_C = utilisateur_texte.count('C')

liste_occurrences_lettres = [
    compte_lettre_K,
    compte_lettre_U,
    compte_lettre_P,
    compte_lettre_C
]

occurence_minimale_lettre = min(liste_occurrences_lettres)

print(occurence_minimale_lettre)