import datetime  # Importe le module datetime, permettant de manipuler des dates et des heures en Python
import sys  # Importe le module sys, utilisé ici pour accéder à l'entrée standard de la console (stdin)

# Création d'une liste contenant les jours de la semaine sous forme de chaînes de caractères.
# L'ordre correspond à la façon dont Python représente les jours (0 pour lundi, 6 pour dimanche).
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Boucle sur chaque ligne fournie en entrée standard (par exemple, lors de l'exécution du script depuis le terminal).
# sys.stdin est un objet qui permet de lire l'entrée ligne par ligne.
for line in sys.stdin:
    # Supprime les espaces, retours à la ligne ou autres caractères “blancs” au début et à la fin de la ligne.
    # Ensuite, sépare la ligne en éléments distincts (par défaut en utilisant un espace comme séparateur).
    data = line.strip().split()
    # Récupère le premier élément de la liste 'data' et le stocke dans la variable 'm'. 
    # Il est supposé que cet élément est le mois.
    m = data[0]
    # Récupère le deuxième élément de la liste 'data' et le stocke dans la variable 'd'.
    # Il est supposé que cet élément est le jour du mois.
    d = data[1]
    # Si la saisie du mois est '0', cela signifie que l'utilisateur veut arrêter la saisie.
    # On utilise donc 'break' pour sortir de la boucle for et arrêter de traiter les prochaines lignes.
    if m == '0':
        break

    # Concatène les éléments pour construire une chaîne de caractères représentant une date et une heure complètes.
    # - '2004-' est l'année, suivie d'un tiret pour séparer le mois.
    # - m est le mois sous forme de chaîne.
    # - '-' sépare le mois du jour.
    # - d est le jour du mois aussi sous forme de chaîne.
    # - ' 13:13:13' précise l'heure (fixée arbitrairement à 13h13min13s).
    # Ex : si m='02' et d='28', cela produit : '2004-02-28 13:13:13'
    date_string = '2004-' + m + '-' + d + ' 13:13:13'

    # Utilisation de la fonction strptime du module datetime pour convertir la chaîne 'date_string'
    # en un objet de type datetime.datetime.
    # Le second argument indique le format précis de la chaîne afin que Python sache comment la lire.
    # %Y -> année sur 4 chiffres, %m -> mois sur 2 chiffres, %d -> jour sur 2 chiffres
    # %H -> heure sur 2 chiffres, %M -> minutes sur 2 chiffres, %S -> secondes sur 2 chiffres
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

    # Appel de la méthode weekday() de l'objet datetime.
    # Cette méthode retourne un entier allant de 0 (lundi) à 6 (dimanche) correspondant au jour de la semaine.
    day_index = date.weekday()

    # Utilisation de l'entier obtenu précédemment (day_index) pour sélectionner le bon nom du jour
    # depuis la liste 'weekdays'. On passe l'indice entre crochets pour obtenir le jour au format texte.
    print weekdays[day_index]  # Affiche le nom du jour de la semaine (exemple : 'Saturday') dans la sortie standard