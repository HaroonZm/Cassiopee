# Demande à l'utilisateur de saisir une chaîne de caractères, puis la divise en une liste de sous-chaînes en utilisant un espace comme séparateur.  
# La fonction input() lit une ligne entière depuis l'entrée standard (le clavier).  
# La méthode split() sans argument divise cette chaîne en une liste de mots séparés par un ou plusieurs espaces.  
l = list(input().split())

# Trie la liste l en place, c'est-à-dire modifie directement la liste l pour que ses éléments soient dans l'ordre croissant (ici ordre alphabétique car ce sont des chaînes).  
# La méthode sort() trie les éléments d'une liste.  
l.sort()

# Vérifie si les éléments aux indices 0, 1, 2 et 3 sont tous égaux,  
# et si les éléments aux indices 4, 5, 6 et 7 sont tous égaux,  
# et si les éléments aux indices 8, 9, 10 et 11 sont tous égaux.  
# L'opérateur == permet de comparer les valeurs.  
# L'écriture a == b == c == d signifie que a==b ET b==c ET c==d.  
if l[0] == l[1] == l[2] == l[3] and l[4] == l[5] == l[6] == l[7] and l[8] == l[9] == l[10] == l[11]:
    # Si la condition est vraie (toutes ces égalités sont vraies), alors on affiche le texte 'yes' à l'écran.  
    # La fonction print() affiche ce qui est passé en argument dans la console.  
    print('yes')
else:
    # Si la condition est fausse (au moins une des égalités n'est pas respectée), alors on affiche 'no'.  
    print('no')