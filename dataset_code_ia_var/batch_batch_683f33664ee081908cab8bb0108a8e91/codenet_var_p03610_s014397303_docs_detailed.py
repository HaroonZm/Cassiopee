def extract_odd_indexed_characters(s: str) -> str:
    """
    Extrait les caractères d'une chaîne d'entrée situés aux indices pairs (0, 2, 4, ...),
    jusqu'au premier caractère qui ne peut plus être accédé de cette manière.
    Si la chaîne est de longueur inférieure ou égale à 2, retourne simplement le premier caractère.

    Args:
        s (str): La chaîne d'entrée.

    Returns:
        str: Les caractères extraits selon la logique décrite.
    """
    # Si la chaîne contient 2 caractères ou moins, retourner le premier caractère
    if len(s) <= 2:
        return s[0]

    else:
        # Calculer N comme la moitié entière de la longueur de la chaîne
        N = len(s) // 2
        q = 0

        # Si N est impair, ajuster q pour couvrir le dernier caractère si besoin
        if N % 2 == 1:
            q = 1

        Odd = []
        # Parcourir les indices de 0 à N+q (exclus) pour récupérer les caractères d'indice pair
        for i in range(N + q):
            Odd.append(s[2 * i])

        # Fusionner la liste de caractères en une seule chaîne
        Odd = "".join(Odd)
        return Odd

def main():
    """
    Point d'entrée principal du script.
    Lit une chaîne depuis l'entrée standard,
    applique la fonction d'extraction, puis affiche le résultat.
    """
    # Lire l'entrée utilisateur
    s = input()
    # Appliquer la fonction et afficher le résultat
    print(extract_odd_indexed_characters(s))

if __name__ == "__main__":
    main()