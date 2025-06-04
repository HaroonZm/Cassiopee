# Solution complète pour le problème de formatage de citations en pages

def format_pages(pages):
    """
    Fonction qui prend une liste de numéros de pages triés en ordre croissant
    et retourne une chaîne qui représente la notation abrégée selon les règles du problème.

    Arguments:
    pages -- liste d'entiers, pages référencées

    Retour:
    string formatée selon le style demandé.
    """
    n = len(pages)
    if n == 0:
        return ""

    result = []  # liste pour stocker les morceaux formatés
    start = pages[0]  # début de la plage courante
    prev = pages[0]   # page précédente dans la plage

    for i in range(1, n):
        if pages[i] == prev + 1:
            # la page est consécutive à la précédente, on continue la plage
            prev = pages[i]
        else:
            # fin d'une plage, on ajoute au résultat
            if start == prev:
                # plage d'une seule page
                result.append(str(start))
            else:
                # plage de plusieurs pages, on note "a-b"
                result.append(f"{start}-{prev}")
            # on démarre une nouvelle plage
            start = pages[i]
            prev = pages[i]

    # traiter la dernière plage après la boucle
    if start == prev:
        result.append(str(start))
    else:
        result.append(f"{start}-{prev}")

    # concaténer avec un espace sans espace extra en fin
    return " ".join(result)


def main():
    while True:
        n = int(input())
        if n == 0:
            break  # fin des jeux de données
        pages = list(map(int, input().split()))
        print(format_pages(pages))


if __name__ == "__main__":
    main()