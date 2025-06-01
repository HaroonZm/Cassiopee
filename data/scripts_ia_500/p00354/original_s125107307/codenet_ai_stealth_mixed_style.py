import datetime

def main():
    jours = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    x = int(input("Entrez un jour en septembre 2017: "))

    # calcul de l'indice du jour de la semaine
    d = datetime.date(year=2017, month=9, day=x)
    idx = d.weekday()

    # afficher résultat
    print(jours[idx])

if __name__ == "__main__":
    main()