# Demande à l'utilisateur de saisir deux entiers séparés par un espace sur la même ligne.
# Utilise la fonction input() pour recevoir cette ligne en tant que chaîne de caractères (string).
# rstrip() supprime tout espace inutile à droite de la chaîne (fin de ligne, retour chariot).
# split() sépare la chaîne par défaut sur les espaces et retourne une liste de chaînes de caractères.
# map(int, ...) convertit chaque élément (ici chaque chaîne de chiffre) en entier (int).
# list(...) transforme l'objet map en une liste d'entiers.
# Les deux entiers sont assignés à n (nombre de processus) et q (quantum).
n, q = list(map(int, input().rstrip().split()))

# Initialise une liste vide pour stocker les processus.
ps = []

# Boucle qui itère exactement n fois (c'est-à-dire pour chaque processus saisi).
for i in range(n):
    # À chaque itération, saisit à nouveau une ligne contenant le nom et le temps du processus.
    # rstrip() enlève les espaces en fin de ligne.
    # split() sépare la ligne sur les espaces, donnant une liste de deux éléments : nom et temps.
    name, time = input().rstrip().split()
    # Ajoute à la liste des processus un dictionnaire contenant le nom et le temps converti en entier.
    # {'name': name, 'time': int(time)} ajoute l'élément dans la liste ps.
    ps.append({'name': name, 'time': int(time)})

# Initialise la variable current_time à 0.
# current_time va contenir le temps total écoulé au fur et à mesure de l'exécution des processus.
current_time = 0

# Tant que la liste des processus n'est pas vide, la boucle continue.
while ps:
    # Retire le premier élément de la liste ps (équivalent à la première position de la file d'attente).
    # La fonction pop(0) enlève et retourne ce premier élément.
    p = ps.pop(0)
    # Récupère le nom du processus du dictionnaire extrait (clé 'name').
    name = p['name']
    # Récupère le temps restant du processus du dictionnaire extrait (clé 'time').
    time = p['time']
    # Vérifie si le temps d'exécution restant de ce processus est supérieur au quantum q.
    if time > q:
        # Si le temps restant est supérieur au quantum,
        # décrémente le temps restant du processus du quantum q.
        # Ajoute le processus à la fin de la liste ps avec le temps mis à jour.
        ps.append({'name': name, 'time': time - q})
        # Ajoute le quantum passé à current_time, car ce temps vient d'être "consommé".
        current_time += q
    else:
        # Si le temps d'exécution restant est inférieur ou égal au quantum,
        # incrémente le temps total écoulé de la durée restante de ce processus (time).
        current_time += time
        # Affiche le nom du processus et le temps total écoulé au moment où il se termine.
        # Utilise la méthode format pour injecter les valeurs dans la chaîne à afficher.
        print('{0} {1}'.format(name, current_time))