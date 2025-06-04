# La fonction input() lit une ligne de l'entrée standard (généralement le clavier) et retourne une chaîne de caractères.
e = input

# On initialise une liste vide qui s'appellera 'a'.
# Cette liste contiendra, pour chaque itération de la boucle principale, une sous-liste 'z' (voir plus bas).
a = []

# On crée une boucle qui va s'exécuter un certain nombre de fois.
# Ce nombre est déterminé par l'utilisateur avec input(), transformé en entier par int().
# L'expression [0] * n crée une liste contenant n éléments égaux à 0.
# En itérant dessus avec _, on répète juste la boucle n fois sans se préoccuper de la valeur.
for _ in [0] * int(e()):
    # Pour chaque itération, on lit une nouvelle chaîne via input().
    # Cette chaîne est stockée dans la variable X.
    X = e()
    
    # On initialise une nouvelle liste vide z, qui servira à stocker des indices particuliers.
    z = []
    
    # On lit une seconde entrée via input(), supposée être une chaîne.
    # On itère sur chaque caractère (chaîne étant itérable, on a chaque 'y' étant un caractère de la chaîne).
    for y in e():
        # On initialise deux variables :
        # s commence à 0, c'est l'indice de départ pour les recherches dans la chaîne X.
        s = 0
        
        # i commence à 0, il sert à parcourir les indices de la liste z.
        i = 0
        
        # On commence une boucle sur chaque élément de la liste z (qui sont des entiers).
        for k in z:
            # La méthode 'find' cherche la première occurrence du caractère 'y' dans X, à partir de l'indice s.
            # find retourne l'indice (de base 0) de la première occurrence ou -1 si le caractère n'est pas trouvé.
            # On ajoute 1 au résultat donc t est l'indice + 1 si trouvé, 0 sinon.
            t = X.find(y, s) + 1
            
            # Si t < 1, cela signifie que le caractère n'a pas été trouvé, alors on quitte la boucle prématurément (break).
            if t < 1:
                break
            
            # Si t < k, c'est-à-dire si la position trouvée est avant la position précédente, alors :
            # On remplace l'élément d'indice i de la liste z par t (mise à jour de l'indice).
            z[i] = t
            
            # On prépare les valeurs pour la prochaine itération :
            # s prend la valeur de k (l'ancien indice pour la prochaine recherche).
            s = k
            
            # i est incrémenté de 1 pour viser l'élément suivant de z.
            i += 1
        
        # else ici est lié à la boucle for, il s'exécute uniquement si la boucle for n'a pas rencontré de break.
        else:
            # De nouveau, on cherche la position de y dans X, à partir de l'indice s.
            t = X.find(y, s) + 1
            
            # Si t n'est pas nul, cela veut dire que le caractère a été trouvé.
            if t:
                # On ajoute t à la fin de la liste z (syntaxe z += [t], qui étend la liste d'un nouvel élément).
                z += [t]
    
    # Après avoir traité tous les caractères de la sous-entrée, 
    # on ajoute la liste z à la liste principale a.
    a += [z]

# Enfin, on affiche une valeur pour chaque élément de la liste a.
# map(len, a) applique la fonction len (qui compte le nombre d'éléments) à chaque sous-liste z de a,
# produisant ainsi une liste d'entiers.
# print(*... , sep='\n') affiche chaque valeur sur une ligne séparée (grâce à sep='\n').
print(*map(len, a), sep='\n')