# Création d'une liste nommée 'histo' contenant 6 chaînes de caractères vides.
# La compréhension de liste ci-dessous parcourt tous les entiers 'i' de 0 à 5 (6 valeurs car range(6) exclut 6)
# À chaque itération, un élément vide "" est ajouté à la liste, résultant en ['','','','','',''].
histo = ["" for i in range(6)]

# Demande à l'utilisateur de saisir une valeur qui correspond au nombre total de mesures de taille à entrer.
# La fonction 'raw_input()' lit une entrée au clavier (en tant que texte, c'est-à-dire chaîne de caractères).
# 'int()' convertit cette chaîne en entier.
n = int(raw_input())

# Boucle 'for' qui va s'exécuter 'n' fois, où 'n' est le nombre d'entrées à traiter.
# À chaque tour de boucle, on lit une nouvelle mesure de hauteur.
for i in range(n):
    # Lit la prochaine valeur de hauteur donnée par l'utilisateur.
    # 'raw_input()' lit la mesure au format chaîne de caractères.
    # 'float()' convertit la chaîne entrée en un nombre décimal (virgule flottante) pour permettre la comparaison numérique.
    h = float(raw_input())
    
    # Le bloc suivant sert à classer chaque hauteur dans un des 6 intervalles de classement dans l'histogramme.
    # Si la hauteur 'h' est strictement inférieure à 165.0, alors on ajoute un caractère '*' à l'élément d'indice 0 de 'histo'.
    if h < 165.0: 
        histo[0] += "*"
    # Sinon, si la hauteur 'h' est plus grande ou égale à 165.0 mais strictement inférieure à 170.0, 
    # alors on ajoute un '*' au deuxième élément (indice 1) de 'histo'.
    elif h < 170.0: 
        histo[1] += "*"
    # Sinon, si 'h' est au moins 170.0 mais strictement inférieure à 175.0 :
    elif h < 175.0: 
        histo[2] += "*"
    # Pour les valeurs comprises entre 175.0 inclus et 180.0 exclus :
    elif h < 180.0: 
        histo[3] += "*"
    # Pour les valeurs comprises entre 180.0 inclus et 185.0 exclus :
    elif h < 185.0: 
        histo[4] += "*"
    # Enfin, pour toutes les valeurs de hauteur 'h' qui sont au moins 185.0, 
    # on ajoute un '*' au dernier élément (indice 5) de 'histo'.
    else:          
        histo[5] += "*"

# Deuxième boucle 'for' qui permet d'afficher chaque ligne de l'histogramme.
# La boucle va de 0 à 5 (soit 6 itérations), ce qui permet de parcourir tous les intervalles.
for i in range(6):
    # 'print' affiche une ligne à l'écran.
    # L'opérateur '%' permet de formater la chaîne à afficher.
    # '%d' sera remplacé par un entier (i+1), qui représente la classe (on ajoute 1 car les listes commencent à l'indice 0).
    # '%-s' sera remplacé par la chaîne de caractères correspondante dans 'histo[i]', indiquant le nombre de '*' pour cet intervalle.
    # Chaque ligne affiche donc le numéro de l'intervalle (de 1 à 6), suivi d'un ':', puis de la chaîne de '*' représentant graphiquement le nombre de valeurs dans cet intervalle.
    print "%d:%-s" % (i+1, histo[i])