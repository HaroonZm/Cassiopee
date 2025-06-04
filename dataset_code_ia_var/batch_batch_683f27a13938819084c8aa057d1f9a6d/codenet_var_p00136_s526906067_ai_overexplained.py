import os  # Importe le module 'os', qui fournit des fonctions pour interagir avec le système d'exploitation (pas utilisé dans ce code)
import math  # Importe le module 'math', qui offre des fonctions mathématiques (pas utilisé ici non plus)

def main():  # Définit la fonction principale du programme appelée 'main'
    # Crée une liste nommée 'lst' qui contient 6 éléments, tous initialisés à la valeur 0.
    # Cette liste sert à compter le nombre d'entrées dans chaque catégorie de tailles.
    lst = [0,0,0,0,0,0]
    
    # Affiche un message à l'utilisateur pour saisir le nombre d'éléments à traiter (non requis, mais souvent fait ainsi)
    # Utilise la fonction input() pour lire une entrée depuis l'utilisateur, qui est par défaut une chaîne de caractères.
    # Convertit cette chaîne en entier avec int() pour obtenir le nombre d'itérations à faire dans la boucle for.
    n = int(input())
    
    # Lance une boucle for qui va répéter le bloc de code indenté un nombre 'n' de fois.
    # La fonction range(0, n) crée une séquence d'entiers de 0 à n-1 inclus (itère n fois).
    for i in range(0, n):
        # À chaque itération, lit une nouvelle entrée, la convertit en flottant pour manipuler des valeurs décimales.
        temp = float(input())
        
        # Ces instructions conditionnelles (if/elif/else) servent à classer chaque valeur dans une catégorie.
        # Si la valeur de 'temp' est inférieure à 165, alors on augmente de 1 le compteur du premier groupe (index 0).
        if temp < 165:
            lst[0] += 1  # Augmente le compteur de la première catégorie
        # Si la valeur n'était pas <165 mais est <170, on augmente de 1 le compteur du deuxième groupe (index 1).
        elif temp < 170:
            lst[1] += 1  # Augmente le compteur de la deuxième catégorie
        # Si la valeur n'était pas <170 mais est <175, on augmente le compteur du troisième groupe (index 2).
        elif temp < 175:
            lst[2] += 1  # Augmente le compteur de la troisième catégorie
        # Si la valeur n'était pas <175 mais est <180, on incrémente le compteur du quatrième groupe (index 3).
        elif temp < 180:
            lst[3] += 1  # Augmente le compteur de la quatrième catégorie
        # Si la valeur n'était pas <180 mais est <185, on incrémente le compteur du cinquième groupe (index 4).
        elif temp < 185:
            lst[4] += 1  # Augmente le compteur de la cinquième catégorie
        # Si aucune des conditions précédentes n'est satisfaite, c'est que temp >=185,
        # donc on incrémente le compteur du sixième et dernier groupe (index 5).
        else:
            lst[5] += 1  # Augmente le compteur de la sixième catégorie
    
    # Après la boucle de saisie et de classification, cette boucle va afficher les résultats.
    # On utilise une boucle for pour itérer de 0 à 5 inclus (6 catégories au total).
    for i in range(0,6):  # Pour chaque catégorie
        # Affiche l'indice de la catégorie (i+1 pour un affichage débutant à 1), suivi de deux-points,
        # mais sans passer à la ligne (grâce à end="").
        print("{}:".format(i+1), end="")
        
        # Imprime autant d'étoiles '*' qu'il y a eu d'éléments dans la catégorie correspondante.
        # La boucle for va de 0 jusqu'à lst[i]-1 inclus.
        for j in range(0, lst[i]):
            # Affiche une étoile et reste sur la même ligne (end="").
            print("*", end = "")
        
        # Après toutes les étoiles pour cette catégorie, affiche un retour à la ligne.
        print()

# Appelle la fonction principale pour lancer l'exécution du programme lorsque ce script est exécuté.
main()