def calculer_valeur(a, t, r):
    """
    Calcule et retourne la valeur obtenue en multipliant t par r divisé par a.

    Arguments :
    a -- un entier, dénominateur du calcul
    t -- un entier, facteur multiplicatif
    r -- un entier, numérateur du calcul

    Retour :
    Un float résultant de (r / a) * t
    """
    return (r / a) * t


# Lecture des valeurs entières a, t, r séparées par des espaces depuis l'entrée utilisateur
a, t, r = map(int, input("Entrez trois entiers séparés par des espaces (a t r) : ").split())

# Calcul du résultat en appelant la fonction calculer_valeur
resultat = calculer_valeur(a, t, r)

# Affichage du résultat calculé
print(resultat)