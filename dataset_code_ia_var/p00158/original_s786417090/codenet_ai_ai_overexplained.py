import sys  # Importe le module sys qui donne accès à certains paramètres et fonctions du système
from sys import stdin  # Importe l'objet stdin du module sys pour la lecture des entrées standard
input = stdin.readline  # Assigne la fonction readline de stdin à la variable input pour une lecture rapide d'une ligne de l'entrée standard

def main(args):  # Définit la fonction principale main qui prend un argument args (liste d'arguments de la ligne de commande, mais non utilisé ici)
    while True:  # Commence une boucle infinie qui continuera jusqu'à ce qu'une instruction break soit rencontrée
        n = int(input())  # Lit une ligne de l'entrée standard, supprime le caractère de retour à la ligne et convertit cette valeur en entier. Cette valeur est stockée dans la variable n.
        if n == 0:  # Vérifie si n est égal à 0
            break  # Si c'est le cas, quitte la boucle (car 0 est le terme de fin des entrées)
        
        count = 0  # Initialise la variable count à 0. Cette variable tiendra le nombre d'opérations effectuées jusqu'à ce que n atteigne 1.
        while n != 1:  # Démarre une boucle qui continue tant que n n'est pas égal à 1
            if n % 2 == 0:  # Vérifie si n est un nombre pair en vérifiant si le reste de la division de n par 2 est égal à 0
                n //= 2  # Si n est pair, divise n par 2 en utilisant la division entière, c'est-à-dire n = n // 2
            else:  # Exécuté si n est impair (donc le reste de la division de n par 2 est différent de 0)
                n *= 3  # Multiplie n par 3 (n = n * 3)
                n += 1  # Ajoute 1 à n (n = n + 1)
            count += 1  # Incrémente la variable count de 1 pour enregistrer qu'une opération a été effectuée
        print(count)  # Après que la boucle interne a terminé (lorsque n vaut 1), affiche la valeur de count à la sortie standard

if __name__ == '__main__':  # Cette ligne permet de vérifier si ce script est exécuté comme programme principal (et non importé comme module)
    main(sys.argv[1:])  # Appelle la fonction main avec les arguments de la ligne de commande (à partir du deuxième élément, car le premier est le nom du script)