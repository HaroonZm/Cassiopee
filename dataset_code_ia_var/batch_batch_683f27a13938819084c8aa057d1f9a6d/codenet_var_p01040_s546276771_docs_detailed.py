import datetime

def count_friday_13th(y1, m1, d1, y2, m2, d2):
    """
    Compte le nombre de vendredis 13 entre deux dates incluses, en optimisant
    le calcul par blocs de 400 ans pour accélérer le traitement sur de grandes périodes.

    Args:
        y1 (int): Année de début
        m1 (int): Mois de début
        d1 (int): Jour de début
        y2 (int): Année de fin
        m2 (int): Mois de fin
        d2 (int): Jour de fin

    Returns:
        int: Le nombre de vendredis tombant le 13 entre les deux dates.
    """
    # Détermine combien de cycles complets de 400 ans sont présents dans l'année de début
    complete_400_year_blocks, y1 = divmod(y1, 400)
    # Remet y1 dans la plage [400, 799] pour l'alignement des cycles
    y1 += 400
    # Décale le compteur de blocs pour correction lors du calcul ultérieur
    complete_400_year_blocks -= 1

    # Détermine combien de cycles de 400 ans sont compris entre y1 et y2
    num_400year_blocks = (y2 - y1) // 400
    # Récupère l'année de fin ajustée à la limite du bloc de 400 ans
    y2 -= 400 * num_400year_blocks

    # Calcule le nombre de vendredis 13 complets sur les blocs de 400 ans entre la première date et la seconde.
    # 688 représente le nombre de vendredis 13 sur un cycle de 400 ans dans le calendrier grégorien.
    a = 688 * (num_400year_blocks - complete_400_year_blocks)

    # Crée un objet date pour le début du parcours.
    d = datetime.date(y1, m1, d1)
    # Parcourt chaque jour jusqu'à la date de fin (incluse)
    while d <= datetime.date(y2, m2, d2):
        # Si le jour est un 13 ET c'est un vendredi (weekday()==4)
        if d.day == 13 and d.weekday() == 4:
            a += 1
        # Passe au jour suivant
        d += datetime.timedelta(days=1)
    return a

def main():
    """
    Fonction principale.
    Lit les dates au format 'y1 m1 d1 y2 m2 d2' depuis l'entrée standard,
    puis affiche le nombre de vendredis 13 compris (inclusivement) entre les deux dates.
    """
    # Lit les six entiers de l'entrée standard représentant les deux dates.
    y1, m1, d1, y2, m2, d2 = map(int, input().split())
    # Calcule et affiche le résultat à l'aide de la fonction principale.
    print(count_friday_13th(y1, m1, d1, y2, m2, d2))

# Point d'entrée du script
if __name__ == "__main__":
    main()