import sys
from datetime import date

# Récupération de l'entrée standard pour lire les lignes de dates fournies par l'utilisateur
f = sys.stdin

# Dictionnaire contenant les différentes ères japonaises avec leurs dates de début et de fin
eras = {
    'pre-meiji': {'start': None, 'end': date(1868, 9, 7)},          # Avant l'ère Meiji, pas de date de début définie
    'meiji': {'start': date(1868, 9, 8), 'end': date(1912, 7, 29)}, 
    'taisho': {'start': date(1912, 7, 30), 'end': date(1926, 12, 24)},
    'showa': {'start': date(1926, 12, 25), 'end': date(1989, 1, 7)},
    'heisei': {'start': date(1989, 1, 8), 'end': None}              # Dernière ère sans date de fin définie
}

def convert_to_japanese_era(year, month, day):
    """
    Convertit une date grégorienne donnée en son équivalent dans les ères japonaises.
    
    Args:
        year (int): Année du calendrier grégorien.
        month (int): Mois du calendrier grégorien.
        day (int): Jour du calendrier grégorien.

    Returns:
        str: Une chaîne décrivant l'ère japonaise et l'année dans cette ère si applicable.
            Pour l'ère "pre-meiji", retourne seulement le nom de l'ère.
            Pour les autres ères, retourne le nom de l'ère, l'année de l'ère, le mois et le jour.
    """
    target = date(year, month, day)  # Création de l'objet date à partir des paramètres fournis
    
    # Parcours des périodes des ères japonaises pour trouver celle à laquelle la date appartient
    for era_name, period in eras.items():
        # Vérifie si la date cible est dans la plage de l’ère actuelle.
        # La date est valide si elle est postérieure ou égale au début de l'ère (sauf pour pre-meiji),
        # et antérieure ou égale à la fin de l'ère (sauf si la fin est None).
        if (period['start'] is None or period['start'] <= target) and \
           (period['end'] is None or target <= period['end']):
            if era_name == 'pre-meiji':
                # Pour l'ère pre-meiji, on ne donne que le nom de l'ère
                return era_name
            else:
                # Calcul de l'année dans l'ère japonaise par différence des années, plus 1
                year_in_era = target.year - period['start'].year + 1
                # Retourne l'ère, l'année dans l'ère, et la date complète
                return f"{era_name} {year_in_era} {target.month} {target.day}"
    # Si aucune ère ne correspond, retourner None ou un message d'erreur (peu probable)
    return None

# Boucle principale lisant chaque ligne depuis l'entrée standard
for line in f:
    # Extraction des valeurs année, mois, jour depuis la ligne d'entrée
    y, m, d = map(int, line.split())
    # Conversion et affichage du résultat correspondant à la date donnée
    print(convert_to_japanese_era(y, m, d))