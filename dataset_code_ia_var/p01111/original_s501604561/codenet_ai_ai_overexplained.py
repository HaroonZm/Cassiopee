# 2018_c avec commentaires excessivement détaillés

# Définition de la fonction factorize, qui va trouver tous les diviseurs d'un nombre donné n
def factorize(n):
    # Si n est inférieur à 4, alors on considère que ses diviseurs sont simplement 1 et n lui-même
    if n < 4:
        # On retourne une liste contenant 1 et n
        return [1, n]
    # On initialise un entier i, qui commencera à 2
    i = 2
    # On initialise une liste l qui contiendra les diviseurs de n, en commençant avec 1
    l = [1]
    # On va parcourir toutes les valeurs de i telles que le carré de i soit inférieur ou égal à n
    while i ** 2 <= n:
        # On vérifie si n est divisible par i, c'est-à-dire si le reste de la division Euclidienne de n par i vaut 0
        if n % i == 0:
            # Si c'est le cas, alors i est un diviseur de n, on l'ajoute donc à la liste l
            l.append(i)
            # On vérifie maintenant si n//i est différent de i afin d'éviter d'ajouter deux fois le même diviseur lorsque n est un carré parfait
            if n // i != i:
                # Si c'est différent, alors n//i est également un diviseur de n, on l'ajoute à la liste
                l.append(n // i)
        # On incrémente i de 1 pour tester le nombre suivant
        i += 1
    # On ajoute enfin à la liste l le nombre n lui-même, qui est aussi un diviseur de lui-même
    l.append(n)
    # On trie la liste l pour que les diviseurs soient rangés dans l'ordre croissant
    l.sort()
    # On retourne la liste de tous les diviseurs trouvés
    return l

# On entre dans une boucle infinie qui ne s'arrêtera que si on rencontre la condition de sortie à l'intérieur de la boucle
while 1:
    # On récupère une entrée utilisateur (sous forme de chaîne de caractères, d'où l'utilisation de input())
    # On la convertit en entier avec int()
    b = int(input())
    # On vérifie si la valeur entrée par l'utilisateur est 0
    if b == 0:
        # Si c'est le cas, on quitte la boucle avec break, ce qui va donc mettre fin au programme
        break
    # On appelle la fonction factorize en lui passant 2*b en argument, et on stocke le résultat (une liste de diviseurs de 2*b) dans la variable f
    f = factorize(2 * b)
    # On parcourt la liste des diviseurs f en partant de la fin et en allant vers le début, donc dans l'ordre décroissant
    for n in f[::-1]:
        # Pour chaque diviseur n, on calcule la valeur de a en utilisant la formule a = 1 - n + (2*b)//n
        a = 1 - n + (2 * b) // n
        # Maintenant, on vérifie que a est supérieur ou égal à 1 et que a est pair (a%2 == 0 veut dire que le reste de a divisé par 2 est nul)
        if a >= 1 and a % 2 == 0:
            # On affiche deux valeurs séparées par un espace :
            # - a//2, c'est-à-dire la moitié de a (// est la division entière, qui ne garde que la partie entière du quotient)
            # - n, le diviseur actuel
            print(a // 2, n)
            # On sort de la boucle for immédiatement, car on ne souhaite imprimer qu'une seule paire par itération
            break