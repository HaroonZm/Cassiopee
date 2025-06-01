from datetime import date
import calendar

def main():
    """
    Boucle indéfinie demandant à l'utilisateur d'entrer un mois et un jour.
    Pour chaque couple (mois, jour), affiche le nom du jour de la semaine correspondant à la date en 2004.
    Le programme s'arrête lorsque le mois saisi est 0.
    """
    while True:
        # Lire deux entiers depuis l'entrée standard, séparés par un espace: mois (m) et jour (d)
        m, d = map(int, input().split())

        # Condition d'arrêt: si le mois est 0, on sort de la boucle
        if not m:
            break

        # Création d'un objet date correspondant à l'année 2004, mois m et jour d
        dt = date(2004, m, d)

        # Obtenir l'indice du jour de la semaine (0 = lundi, ..., 6 = dimanche)
        weekday_index = dt.weekday()

        # Afficher le nom complet du jour de la semaine en anglais
        # calendar.day_name est une liste contenant les noms des jours de la semaine
        print(calendar.day_name[weekday_index])

if __name__ == "__main__":
    main()