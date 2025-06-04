# Demande à l'utilisateur de saisir une valeur. 
# Par défaut, la fonction input() retourne une chaîne de caractères.
n = input()

# Demande à l'utilisateur de saisir une deuxième valeur.
m = input()

# On suppose que n et m doivent être interprétés comme des entiers pour les opérations suivantes.
# Les convertit donc explicitement en int.
n = int(n)
m = int(m)

# On crée une liste nommée ks qui va contenir m éléments.
# Pour chaque itération de la boucle (pour i allant de 0 à m-1),
# on demande à l'utilisateur de saisir une valeur (qui est supposée pouvoir être convertie en int)
# Chaque fois, la valeur saisie est convertie en un entier avant d'être stockée dans la liste.
ks = [int(input()) for i in range(m)]

# Création d'une liste appelée card contenant les entiers de 1 à n*2 inclus.
# range(1, n*2+1) génère les nombres de 1 à n*2 (car le second argument est exclusif).
# La liste en compréhension sert ici juste à copier explicitement ces valeurs dans la liste card.
card = [v for v in range(1, n*2+1)]

# On parcourt chaque valeur de la liste ks, en utilisant la variable temporaire k.
for k in ks:
    # Si la valeur courante de k est 0, on va effectuer un entrelacement ('riffle shuffle').
    if k == 0:
        # On crée une liste temporaire vide tmp pour stocker le nouveau mélange de cartes.
        tmp = []
        # On divise la liste card en deux moitiés égales :
        # c1 contient la 1ère moitié (du début jusqu'à l'index n-1) ;
        # c2 contient la 2nde moitié (de l'index n jusqu'à la fin de la liste).
        c1, c2 = card[:n], card[n:]
        # On combine les deux moitiés en entrelaçant les éléments un à un.
        for i in range(n):
            # On ajoute à la liste tmp d'abord le i-ème élément de c1,
            # puis le i-ème élément de c2. Ainsi les cartes des deux moitiés s'alternent une à une.
            tmp += [c1[i], c2[i]]
        # On remplace la liste card par la nouvelle liste tmp qui est le résultat du mélange.
        card = tmp
    # Si k n'est pas égal à 0, on fait un "coupure" du paquet.
    else:
        # La syntaxe card[k:] + card[:k] déplace les k premières cartes à la fin du paquet :
        # card[k:] sélectionne les cartes de l'indice k à la fin de la liste ;
        # card[:k] sélectionne les cartes de l'indice 0 à k-1 ;
        # on les concatène pour simuler la coupe du paquet après les k premières cartes.
        card = card[k:] + card[:k]

# On parcourt chaque victoire (chaque valeur) dans la liste card.
for v in card:
    # On affiche la valeur courante v avec la fonction print (version Python 2 : pas de parenthèses).
    print v