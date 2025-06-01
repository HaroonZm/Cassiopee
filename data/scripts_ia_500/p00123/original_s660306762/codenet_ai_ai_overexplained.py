# Importation du module sys qui permet d'interagir avec les entrées et sorties standards du système (ici, pour lire les données du terminal).
import sys

# Définition de la fonction 'solve' qui prend deux arguments : r500 et r1000.
# Ces arguments correspondent à deux valeurs numériques flottantes, représentant des temps mesurés pour certaines distances (probablement 500m et 1000m).
def solve(r500, r1000):
    # Définition d'une liste nommée 'criteria' contenant des tuples.
    # Chaque tuple représente un ensemble de critères sous la forme (valeur_max_500m, valeur_max_1000m, classement).
    # Par exemple, (35.50, 71.0, 'AAA') signifie que si r500 < 35.50 et r1000 < 71.0, alors le classement est 'AAA'.
    criteria = [(35.50,  71.0, 'AAA'),
                (37.50,  77.0, 'AA'),
                (40.0,   83.0, 'A'),
                (43.0,   89.0, 'B'),
                (50.0,  105.0, 'C'),
                (55.0,  116.0, 'D'),
                (70.0,  148.0, 'E')]
    
    # Initialisation de la variable 'rank' à None, ce qui signifie qu'aucun classement n'a encore été trouvé.
    rank = None
    
    # Parcours de chaque tuple dans la liste 'criteria' : c500 est la valeur max pour 500m, c1000 pour 1000m, r est le rang associé.
    for c500, c1000, r in criteria:
        # Vérification de la condition si les temps fournis (r500 et r1000) sont tous deux inférieurs aux critères respectifs.
        if r500 < c500 and r1000 < c1000:
            # Si la condition est remplie, affecter à 'rank' le rang associé 'r'.
            rank = r
            # Interrompre la boucle puisque le classement a été trouvé.
            break
    
    # Si après la boucle, aucune condition n'a été satisfaite, c'est-à-dire que rank est toujours None,
    # cela signifie que les temps ne correspondent à aucun classement connu.
    if rank == None:
        # On attribue alors le classement 'NA' qui signifie "Non Appliqué" ou "Non Attribué".
        rank = 'NA'
    
    # Retourner la valeur finale de 'rank'.
    return rank

# Définition de la fonction principale 'main' qui prend en argument 'args', une liste d'arguments en ligne de commande.
def main(args):
    # Boucle sur chaque ligne d'entrée standard (par exemple, ce qui est tapé dans le terminal ou redirigé depuis un fichier).
    for line in sys.stdin:
        # Utilisation de la méthode strip() pour retirer les espaces blancs au début et à la fin de la ligne,
        # puis split() pour diviser la ligne en une liste de chaînes de caractères en fonction des espaces.
        # Ensuite, compréhension de liste pour convertir chaque élément de la liste en float (nombre à virgule flottante).
        r500, r1000 = [float(x) for x in line.strip().split()]
        
        # Appel de la fonction 'solve' avec les deux valeurs obtenues.
        result = solve(r500, r1000)
        
        # Affichage du résultat retourné par la fonction 'solve'.
        print(result)

# Vérification si ce script est exécuté directement (et non importé comme module dans un autre script).
if __name__ == '__main__':
    # Appel de la fonction 'main' avec la liste des arguments en ligne de commande à partir de l'index 1
    # (sys.argv[0] correspond normalement au nom du script lui-même).
    main(sys.argv[1:])