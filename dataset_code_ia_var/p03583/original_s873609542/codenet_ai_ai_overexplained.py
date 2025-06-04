# Début du programme principal
def main():
    # Lecture de l'entrée utilisateur sous forme de chaîne de caractères via la fonction input(),
    # puis conversion explicite de cette chaîne de caractères en un entier grâce à int().
    N = int(input())
    
    # Initialisation des variables h, n, et w à la valeur -1 chacune.
    # Ceci sert à stocker plus tard les solutions trouvées.
    # Les valeurs -1 indiquent qu'aucune solution n'a encore été trouvée.
    h, n, w = -1, -1, -1
    
    # Boucle for externe allant de 1 inclus à 3501 non inclus.
    # La variable 'i' prendra successivement toutes les valeurs entières des bornes définies.
    # i commence à 1 car il est fort probable que les valeurs recherchées doivent être positives.
    for i in range(1, 3501):
        
        # Boucle for interne allant de la valeur actuelle de 'i' jusqu'à 3501 non inclus.
        # 'j' représente un autre paramètre de la solution potentielle, et est au moins égal à 'i'
        # pour limiter les combinaisons redondantes.
        for j in range(i, 3501):
            
            # Calcul et vérification de l'inégalité 4*i*j > N*i + N*j
            # Cette condition permet d'éviter une division par zéro ou des résultats négatifs plus loin.
            # Si la condition échoue, le corps du if n'est pas exécuté pour ce couple (i, j).
            if 4*i*j > N*i + N*j:
                
                # Calcul du dénominateur qui intervient dans le calcul de 'w' plus bas :
                # denom = 4*i*j - N*i - N*j
                # On teste ici si la multiplication N*i*j est exactement divisible par ce dénominateur,
                # c'est-à-dire si le reste de cette division euclidienne est nul.
                if N*i*j % (4*i*j - N*i - N*j) == 0:
                    
                    # Si les conditions sont vérifiées, attribution de i à h, j à n.
                    h, n = i, j
                    
                    # Calcul de w selon la formule :
                    # w = (N*i*j) // (4*i*j - N*i - N*j)
                    # On utilise l'opérateur // pour effectuer une division entière.
                    w = N*i*j // (4*i*j - N*i - N*j)
                    
                    # Sortie prématurée de la boucle for interne (celle sur j) à l'aide de 'break'
                    # Ceci signifie qu'une solution valide a été trouvée et il n'est pas nécessaire
                    # de continuer à tester d'autres valeurs pour ce 'i'.
                    break
            
            # FIN du if (fin de l'indentation correspondante)
        # La partie 'else' associée à la boucle for interne.
        # Cette clause ne s'exécute que si la boucle for interne n'a PAS été interrompue par un break.
        # Si 'break' a été exécuté, on skippe ce 'else' et on sort aussi de la boucle externe.
        else:
            # Si on entre dans ce else, alors aucune solution n'a été trouvée pour ce 'i'
            # On passe donc à la prochaine valeur de 'i' de la boucle externe.
            continue
        
        # Sortie prématurée de la boucle for externe (celle sur i)
        # Cela signifie qu'on a trouvé une solution valide et qu'on ne souhaite plus poursuivre les recherches.
        break
    
    # Affichage final des résultats trouvés, sous forme d'entiers séparés par des espaces.
    # print prend en charge l'affichage standard (console).
    print(h, n, w)

# Bloc conditionnel spécial, souvent utilisé en Python pour déterminer si ce fichier
# est exécuté comme programme principal et non importé comme module.
# Si '__name__' vaut littéralement la chaîne '__main__' cela signifie que ce script est démarré
# directement et non via une importation.
if __name__ == '__main__':
    # On appelle la fonction main() pour démarrer le programme écrit ci-dessus.
    main()