import math  # Importe le module math, qui fournit des fonctions mathématiques comme sqrt (racine carrée)

def main():
    # Fonction principale exécutée lors du démarrage du programme

    while True:
        # Boucle infinie, qui ne s'arrête que par une instruction break
        # Cela permet de demander plusieurs entrées à l'utilisateur

        # Demande à l'utilisateur une entrée, puis la divise en trois entiers
        # L'entrée doit être trois entiers séparés par des espaces
        a, d, n = map(int, input().split())

        # Si le premier terme a est égal à 0, le programme s'arrête
        if a == 0:
            break  # Quitte la boucle while

        # Appelle la fonction showprime avec les valeurs lues et affiche le résultat
        print(showprime(a, d, n))

    return  # Fin de la fonction (même si ce 'return' n'est pas strictement nécessaire)

def showprime(a, d, n):
    # Cette fonction recherche le n-ième nombre premier dans une suite arithmétique
    # La suite commence à 'a' et chaque terme suivant est augmenté de 'd'

    i = 0  # Compteur du nombre de nombres premiers trouvés dans la suite jusqu'à présent

    while True:
        # Boucle infinie pour chercher le n-ième nombre premier

        # Vérifie si 'a' est premier en appelant isprime(a);
        # si oui, isprime(a) retourne 1, sinon 0;
        # incrémente 'i' d'après cela
        i += isprime(a)

        # Si on a trouvé 'n' nombres premiers (i == n), retourne la valeur actuelle de 'a'
        if i == n:
            return a

        # Passe au terme suivant de la suite arithmétique en ajoutant 'd'
        a += d

def isprime(num):
    # Vérifie si un nombre 'num' est un nombre premier

    # Un nombre premier est un entier supérieur à 1 qui n'a que deux diviseurs : 1 et lui-même

    if num == 0 or num == 1:
        # 0 et 1 ne sont pas des nombres premiers
        return 0  # Retourne 0 pour indiquer "pas premier"

    # Calcule la racine carrée de num et la convertit en entier pour la borne de la boucle suivante
    sq_num = int(math.sqrt(num))
    # On n'a pas besoin d'aller au-delà de la racine carrée pour tester la primalité

    for i in range(2, sq_num + 1):
        # Boucle pour essayer tous les diviseurs possibles de 2 à sq_num inclus

        if num % i == 0:
            # Si num est divisible par i (le reste de la division euclidienne est 0)
            # alors num n'est pas premier
            return 0  # Retourne 0 pour indiquer "pas premier"

    # Si aucun diviseur n'a été trouvé dans la boucle, num est premier
    return 1  # Retourne 1 pour indiquer "nombre premier"

main()  # Appelle la fonction principale pour démarrer le programme