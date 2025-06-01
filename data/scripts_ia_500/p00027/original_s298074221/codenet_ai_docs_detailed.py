import datetime
import sys

# Liste des jours de la semaine en anglais, indexée de 0 (lundi) à 6 (dimanche)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def main():
    """
    Lit les lignes depuis l'entrée standard. Chaque ligne doit contenir deux valeurs séparées par un espace : 
    - m : le mois sous forme de nombre (1 à 12)
    - d : le jour du mois
    
    Pour chaque ligne :
    - Si m vaut '0', termine la lecture.
    - Sinon, crée un objet datetime pour l'année 2004, avec le mois et le jour spécifiés, et une heure fixe (13:13:13).
    - Affiche le nom du jour de la semaine correspondant à cette date.
    
    Remarque : l'année est fixée à 2004, car c'est une année bissextile cohérente pour la conversion.
    """
    for line in sys.stdin:
        # Supprime les espaces superflus et découpe la ligne en tokens
        data = line.strip().split()

        # Extraction des valeurs : mois et jour
        m = data[0]
        d = data[1]

        # Condition d'arrêt : si le mois vaut '0', on sort de la boucle
        if m == '0':
            break

        # Conversion en objet datetime en utilisant une date fixe dans l'année 2004 et une heure fixe
        date_str = '2004-' + m + '-' + d + ' 13:13:13'
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

        # Affichage du jour de la semaine correspondant à cet objet datetime
        print(weekdays[date.weekday()])

if __name__ == '__main__':
    main()