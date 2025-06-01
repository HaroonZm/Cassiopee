def process_input():
    """
    Fonction principale pour traiter les entrées utilisateur dans une boucle infinie.
    
    Pour chaque itération, la fonction :
    - lit une entrée (n),
    - arrête la boucle si n est égal à 0,
    - sinon, lit une liste d'entiers,
    - puis affiche "NA" si le maximum de cette liste est inférieur à 2,
      ou bien affiche 1 plus le nombre d'éléments strictement positifs dans la liste.
    
    Cette fonction ne prend pas d'arguments et ne retourne rien.
    """
    while True:
        # Lecture d'une valeur depuis l'entrée standard
        n = input()
        
        # Contrôle de la condition d'arrêt : si n est "0", on quitte la boucle
        if n == '0':
            break
        
        # Lecture d'une liste d'entiers depuis l'entrée standard
        # La fonction raw_input() est utilisée ici en Python 2 pour lire une ligne entière,
        # puis split() découpe la chaîne en éléments séparés,
        # map(int, ...) convertit chacun des éléments en entier.
        t = map(int, raw_input().split())
        
        # Si le maximum de la liste t est inférieur à 2, on affiche "NA"
        # Sinon, on affiche 1 plus le nombre d'éléments strictement positifs dans t
        if max(t) < 2:
            print "NA"
        else:
            # Comptage des éléments strictement positifs dans t
            count_positive = len([i for i in t if i > 0])
            print 1 + count_positive

# Appel de la fonction principale pour lancer le programme
process_input()