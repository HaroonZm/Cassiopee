from datetime import date

def get_weekday_name(day: int) -> str:
    """
    Renvoie le nom du jour de la semaine correspondant à un jour donné de septembre 2017.
    
    Paramètres :
        day (int): Jour du mois de septembre 2017 (1 à 30).
    
    Retourne :
        str: Abréviation en anglais du jour de la semaine ('mon', 'tue', etc.).
    
    Exceptions :
        ValueError: Si le jour n'est pas valide pour septembre 2017.
    """
    # Liste des jours de la semaine, l'indice 0 correspond à lundi
    weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    # Calcul l'indice du jour de la semaine pour le jour demandé
    idx = date(2017, 9, day).weekday()
    # Retourne le nom du jour correspondant
    return weekdays[idx]

def main():
    """
    Fonction principale qui demande à l'utilisateur un numéro de jour et affiche le jour de la semaine correspondant.
    """
    try:
        # Sollicite la saisie d'un entier à l'utilisateur correspondant au jour du mois
        x = int(input("Entrez le jour du mois de septembre 2017 (1 à 30) : "))
        # Récupère le nom du jour de la semaine à l'aide de la fonction dédiée
        weekday_name = get_weekday_name(x)
        # Affiche le résultat à l'utilisateur
        print(weekday_name)
    except ValueError as e:
        # Gère le cas où la saisie n'est pas un entier ou le jour n'est pas valide
        print("Entrée invalide ou jour non valide pour septembre 2017 :", e)

if __name__ == "__main__":
    # Exécute la fonction principale si le script est lancé directement
    main()