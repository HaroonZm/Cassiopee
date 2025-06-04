def calculer_resultat(a, t, r):
    """
    Calcule le résultat de l'expression (r / a) * t.

    Args:
        a (int): Le diviseur.
        t (int): Le multiplicateur.
        r (int): Le dividende.

    Returns:
        float: Le résultat du calcul.
    """
    # Effectue la division r / a, puis multiplie le résultat par t
    return (r / a) * t

def lire_entrees_utilisateur():
    """
    Demande à l'utilisateur de saisir trois entiers séparés par des espaces,
    puis les convertit en variables distinctes.

    Returns:
        tuple: Un triplet (a, t, r) d'entiers issus de la saisie utilisateur.
    """
    # Demande la saisie à l'utilisateur sous la forme "a t r"
    entrees = input().split(" ")
    # Convertit chaque valeur en entier
    a, t, r = [int(x) for x in entrees]
    return a, t, r

if __name__ == "__main__":
    # Lecture des entrées utilisateur au format "a t r"
    a, t, r = lire_entrees_utilisateur()
    # Calcul du résultat en utilisant la fonction appropriée
    resultat = calculer_resultat(a, t, r)
    # Affichage du résultat à l'écran
    print(resultat)