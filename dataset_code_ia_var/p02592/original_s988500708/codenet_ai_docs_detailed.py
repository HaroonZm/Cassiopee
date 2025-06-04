def print_header():
    """
    Affiche une en-tête composée de plusieurs éléments pour introduire la séquence principale.
    """
    a, l = "+<"  # Caractères spéciaux pour la mise en forme
    print(60451, l, 4, 0, 3)

def get_sequence_patterns():
    """
    Génère et retourne les motifs réutilisés dans la génération des lignes de séquence.
    Returns:
        tuple: (s, t) où s et t sont des listes servant de motifs de multiplication.
    """
    a, l = "+<"
    s = [a, 7, 7, 7]   # Motif s utilisé pour la première boucle
    t = [a, 8, 8, 8]   # Motif t utilisé pour la boucle imbriquée
    return s, t

def print_main_sequences():
    """
    Affiche la séquence principale dans deux boucles imbriquées :
    - La boucle extérieure construit un motif symétrique sur 30 lignes.
    - La boucle intérieure, pour chaque ligne extérieure, affiche une séquence de sous-motifs.
    """
    a, l = "+<"
    s, t = get_sequence_patterns()
    r = range(29, -1, -1)   # Descendant de 29 à 0
    for i in r:
        # Affiche la ligne principale pour la valeur courante de i
        print(
            a, 3, 4, 7,            # Bloc de départ
            *(s * i),              # Motif s répété i fois
            a, 5, 7, 7, l, 0, 7, 7,
            l, 7, 3, 7,
            a, 4, 4, 6             # Motif de queue
        )
        # Boucle interne pour ajouter des motifs imbriqués
        for j in r:
            print(
                a, 3, 4, 8,                # Bloc initial de la sous-ligne
                *(t * j),                  # Motif t répété j fois
                a, 6, 8, 8, l, 1, 8, 8,    # Suite
                l, 8, 3, 8, l, 8, 7, 9,
                *(t * j),                  # Motif t répété j fois
                a, 8, 6, 6, l, 9, 7, 8,    # Suite
                *(t * (i + j)),            # Motif t répété i + j fois
                a, 8, 2, 2                 # Bloc final de la sous-ligne
            )
        # Terminer chaque boucle extérieure par un motif spécifique
        print(*(s * i), a, 7, 5, 5)

def main():
    """
    Lance la génération des motifs en appelant toutes les fonctions nécessaires.
    """
    print_header()
    print_main_sequences()

if __name__ == "__main__":
    main()