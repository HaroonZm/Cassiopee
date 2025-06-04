def count_word_occurrences():
    """
    Compte le nombre de fois qu'un mot donné par l'utilisateur apparaît dans le texte saisi, 
    sans tenir compte de la casse. La saisie du texte prend fin lorsque l'utilisateur entre 'END_OF_TEXT'.
    
    Entrée:
    - Un mot à rechercher, saisi par l'utilisateur (ignorer la casse).
    - Plusieurs lignes de texte, saisies par l'utilisateur (la saisie s'arrête lorsque la ligne 'END_OF_TEXT' est saisie).
    
    Sortie:
    - Affiche le nombre d'occurrences du mot recherché dans l'ensemble du texte.
    """
    # Lecture du mot cible à trouver, conversion en minuscules
    target_word = raw_input().lower()
    
    # Liste pour stocker tous les mots saisis dans le texte
    words_list = []
    
    # Boucle de saisie des lignes de texte
    while True:
        # Lit une ligne de texte de l'utilisateur
        line = raw_input()
        
        # Vérifie si la saisie doit s'arrêter
        if line == "END_OF_TEXT":
            break
        
        # Ajoute les mots de la ligne actuelle (en minuscule) à la liste des mots
        # str.split() découpe la ligne en mots selon les espaces
        words_list += line.lower().split()
    
    # Compte le nombre d'occurrences du mot cible dans la liste de mots
    print(words_list.count(target_word))


# Exécution de la fonction principale
count_word_occurrences()