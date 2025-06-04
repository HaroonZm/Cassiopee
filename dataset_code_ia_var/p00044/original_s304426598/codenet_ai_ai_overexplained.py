import math  # Importe la bibliothèque mathématique standard de Python, qui fournit des fonctions math comme sqrt (racine carrée) utilisée plus loin

def p_l(n):
    # Cette fonction retourne le plus grand nombre premier strictement inférieur à n
    # Arguments :
    #   n : un entier, la borne supérieure (exclusive) pour la recherche des nombres premiers
    # Valeur de retour :
    #   le plus grand nombre premier < n
    
    # La boucle suivante commence à partir de n-1 et décrémente jusqu'à 2 (inclus),
    # En allant de n-1 à 2 (pas de -1)
    for i in range(n-1, 1, -1):
        flag = 0  # Initialisation d'un indicateur (flag) à 0 ; cela servira à signaler si i est composé (non premier)
        
        # On vérifie tous les diviseurs possibles de 2 jusqu'à la racine carrée entière de i (inclus).
        # La racine carrée d'un nombre est utilisée par optimisation car aucun diviseur supérieur à racine(i) n'est possible sauf pour le nombre lui-même
        for j in range(2, int(math.sqrt(i)) + 1):
            # Pour chaque diviseur possible j, on vérifie si i est divisible par j sans reste
            if i % j == 0:
                # Si i est divisible par j, alors i n'est pas premier.
                flag = 1  # On met flag à 1 pour signaler la non-primalité
        
        # Après avoir testé tous les diviseurs potentiels pour i,
        # on regarde si flag a été activé (i.e., si i n'est pas premier)
        if flag == 1:
            # Si flag==1, i n'est pas premier : on saute à l'itération suivante du for principal
            continue
        # Si flag n'est pas égal à 1 (donc égal à 0), alors i est premier
        # On retourne alors i puisque c'est le plus grand nombre premier en-dessous de n trouvé lors de la descente
        return i

def p_h(n):
    # Cette fonction cherche le plus petit nombre premier strictement supérieur à n
    # Arguments :
    #   n : un entier, la borne inférieure (exclusive) pour la recherche
    # Valeur de retour :
    #   le plus petit nombre premier > n
    
    # On part de n+1 et on s'arrête à 50022 (exclu) ; cette borne supérieure arbitraire garantit qu'on trouvera un nombre premier raisonnablement grand
    for i in range(n+1, 50022):
        flag = 0  # Indicateur pour savoir si i est non-premier
        
        # Comme dans la fonction précédente, teste tous les diviseurs possibles jusqu'à racine(i)
        for j in range(2, int(math.sqrt(i)) + 1):
            # Vérifie si i est divisible par j
            if i % j == 0:
                # Si oui, alors i n'est pas premier
                flag = 1  # On signale la non-primalité de i
                
        # Après avoir tout testé :
        if flag == 1:
            # Si le flag est activé, i n'est pas premier, on passe au suivant
            continue
        # Si on y arrive, flag vaut 0 donc i est premier, retourne i immédiatement (on veut le premier trouvé, i.e., le plus petit)
        return i

# Boucle infinie qui gère l'entrée de l'utilisateur et affiche les résultats
while 1:
    try:
        # Demande à l'utilisateur de saisir un nombre entier au clavier
        n = int(input())
        # Appelle la fonction p_l pour trouver le plus grand nombre premier inférieur à n
        # Appelle la fonction p_h pour trouver le plus petit nombre premier supérieur à n
        # Affiche les deux résultats séparés par un espace
        print(p_l(n), p_h(n))
    except:
        # Si une exception se produit (EOFError, ValueError...), quitte la boucle et le programme
        break