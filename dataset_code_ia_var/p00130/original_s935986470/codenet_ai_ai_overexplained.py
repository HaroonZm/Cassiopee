# Demande à l'utilisateur de saisir un nombre entier
n = int(input())  # La fonction input() lit une ligne en entrée de l'utilisateur, int() la convertit en entier

# Lance une boucle qui va s'exécuter n fois, une fois pour chaque séquence fournie par l'utilisateur
for _ in range(n):  # L'underscore est utilisé comme nom de variable lorsque la valeur n'est pas utilisée
    train = ''  # Initialise la chaîne train vide ; elle va contenir progressivement le résultat final pour cette itération
    seq = input()  # Lit la séquence suivante depuis l'entrée utilisateur (chaîne de caractères)
    
    # Parcourt la séquence trois caractères à la fois (car les opérations se font par groupes de trois)
    for i in range(0, len(seq), 3):  # Commence à zéro, termine avant la longueur de seq, incrémente de 3 à chaque fois
        # Pour le tout premier groupe de trois caractères, ajoute le premier caractère à train
        if i == 0:  # Vérifie si c'est la première itération de la boucle interne
            train += seq[i]  # Ajoute le premier caractère de la séquence à la chaîne train
        
        # Cas où on détecte une flèche '->' juste avant la position i, et que le dernier caractère de train
        # est identique au caractère trois positions avant i (soit le départ de la flèche)
        if seq[i - 2:i] == '->' and train[-1] == seq[i - 3]:
            # Ajoute le caractère courant de la séquence à la fin de la chaîne train
            train = train + seq[i]
        
        # Cas où on détecte une flèche '<-' juste avant la position i, et que le premier caractère de train
        # est identique au caractère trois positions avant i (soit le départ de la flèche inversée)
        if seq[i - 2:i] == '<-' and train[0] == seq[i - 3]:
            # Ajoute le caractère courant de la séquence au début de la chaîne train
            train = seq[i] + train
    
    # Une fois toutes les opérations pour la séquence terminées, affiche le résultat pour cette itération
    print(train)  # Affiche le train reconstitué à partir de la séquence d'entrée fournie par l'utilisateur