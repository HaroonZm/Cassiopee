import sys  # Importe le module sys, nécessaire pour accéder à sys.stdin (entrée standard du système)

# Boucle sur chaque ligne entrée par l'utilisateur via l'entrée standard (par exemple, tapée au clavier ou provenant d'un fichier)
for line in sys.stdin.readlines():
    # Convertit la ligne lue (de type chaîne de caractères) en nombre flottant à l'aide de la fonction float()
    # Cela suppose que chaque ligne contient une valeur qui peut être interprétée comme un nombre à virgule flottante
    i = float(line)
    
    # Initialise une variable 's' à 0, qui va accumuler une somme pendant la boucle suivante
    s = 0

    # Exécute la boucle 'for' cinq fois, car range(5) donne une séquence de 0 à 4 inclus (soit 5 entiers)
    for x in range(5):
        # Ajoute la valeur courante de 'i' à 's'
        # Le symbole += signifie 'ajouter à la variable existante'
        s += i
        
        # Multiplie la valeur courante de 'i' par 2, puis stocke le résultat de l'opération dans 'i'
        i *= 2  # équivalent à 'i = i * 2'
        
        # Ajoute la nouvelle valeur de 'i' (après multiplication) à 's'
        s += i
        
        # Divise la valeur courante de 'i' par 3, met à jour 'i' avec ce résultat
        i /= 3  # équivalent à 'i = i / 3'
    
    # Affiche la somme totale calculée pour la ligne courante.
    # La fonction print affiche la sortie standard (écran ou redirection)
    print(s)