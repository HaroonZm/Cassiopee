# On importe le module math pour accéder à la fonction sqrt (racine carrée)
import math

# Définition de la fonction principale appelée "main" qui prend un argument "n"
def main(n):
    # Cette boucle for va itérer la variable i à rebours, c'est-à-dire de la plus grande valeur vers 1 (inclus).
    # La gamme de la boucle est déterminée ainsi :
    # - On commence par calculer une valeur sous la racine carrée :
    #     1 + 8 * n
    #   Ce calcul fait intervenir l'opérateur * qui multiplie 8 par n, puis on ajoute 1 au résultat.
    # - Ensuite, on prend la racine carrée du résultat obtenu : math.sqrt(...)
    # - On ajoute 1 à cette racine carrée.
    # - Ensuite, on divise (par // qui est la division entière) ce résultat par 2, ce qui donne le plus grand nombre entier inférieur ou égal au résultat.
    #   Cela correspond en fait à la résolution de l'équation quadratique pour énumérer certaines propriétés sur des suites de nombres entiers.
    # - Enfin, on ajoute 1 au résultat de cette division entière, pour inclure la limite supérieure dans la boucle.
    # - La fonction int convertir le résultat final en un entier, garantissant que i aura une valeur entière correcte.
    # - La boucle for commence donc à cette valeur maximale et décrémente jusqu'à 1 (inclus, car le stop est 0 et on va jusqu'à stop - 1).
    for i in range(int((1 + math.sqrt(1 + 8 * n)) // 2) + 1, 0, -1):

        # Maintenant, à chaque itération, on exécute le test suivant dans le if :
        # Premièrement, on effectue cette opération :
        #   n / i   --> on divise n par la valeur actuelle de i (résultat : float)
        #   (i - 1) / 2   --> on soustrait 1 à i, puis on divise le résultat par 2 (résultat : float)
        #   Ensuite, on effectue la soustraction :
        #      n / i - (i - 1) / 2
        #   Ceci donne un nombre (normalement float).
        # Ensuite, on vérifie que ce nombre est exactement un entier à l'aide de float.is_integer(...) :
        #   Cela vérifie que le résultat n'a pas de partie décimale (c'est-à-dire que c'est un entier déguisé en float)
        # En même temps, on vérifie que ce nombre est strictement supérieur à 0.
        # Si c'est le cas, alors la condition du if s'exécute.
        if float.is_integer(n / i - (i - 1) / 2) and n / i - (i - 1) / 2 > 0:
            # Affiche le résultat. 
            # - D'abord, on convertit la valeur (n / i - (i - 1) / 2) en entier,
            #   car même si float.is_integer ci-dessus est True, cela reste un float.
            # - Ensuite, on affiche i (qui est déjà un entier).
            # La fonction print affiche ces deux valeurs séparées par un espace selon la convention de print.
            print(int(n / i - (i - 1) / 2), i)
            # Après avoir trouvé et affiché la première solution valide,
            # on quitte la fonction main immédiatement avec return.
            return

# La boucle principale du programme commence ici.
# while 1: signifie "tant que 1 est vrai" (c'est toujours vrai, donc boucle infinie sauf interruption).
while 1:
    # On demande à l'utilisateur une valeur d'entrée avec la fonction input().
    # La chaîne lue est transformée en entier avec int() et stockée dans la variable n.
    n = int(input())
    # On vérifie si la valeur saisie par l'utilisateur est 0.
    # Si c'est le cas, on quitte la boucle (et donc finit le programme) avec break.
    if n == 0:
        break
    # Si n n'est pas 0, on appelle la fonction main avec n comme argument.
    main(n)