import sys

def convert_japanese_era(date_str):
    """
    Convertit une date grégorienne au format 'YYYY MM DD' en la période de l'ère japonaise correspondante.

    Parameters:
    date_str (str): Une chaîne de caractères représentant une date au format 'YYYY MM DD'.

    Returns:
    str: Une chaîne indiquant l'ère japonaise et la date correspondante dans cette ère,
         ou 'pre-meiji' si la date est antérieure à l’ère Meiji.
    """
    # Supprime le saut de ligne en fin de chaîne et sépare les parties de la date en année, mois, jour
    y, m, d = map(int, date_str.strip().split())
    # Convertit la date en un entier au format YYYYMMDD pour faciliter la comparaison
    x = y * 10000 + m * 100 + d

    # Vérifie l'ère correspondant à la date selon les bornes définies
    if x < 18680908:
        return "pre-meiji"
    elif x < 19120730:
        # Ère Meiji : début 1868/09/08
        return "meiji {} {} {}".format(y - 1867, m, d)
    elif x < 19261225:
        # Ère Taisho : début 1912/07/30
        return "taisho {} {} {}".format(y - 1911, m, d)
    elif x < 19890108:
        # Ère Showa : début 1926/12/25
        return "showa {} {} {}".format(y - 1925, m, d)
    else:
        # Ère Heisei : début 1989/01/08 et après
        return "heisei {} {} {}".format(y - 1988, m, d)

# Lecture des lignes depuis l'entrée standard
for line in sys.stdin:
    # Convertit chaque date et affiche le résultat
    print(convert_japanese_era(line))