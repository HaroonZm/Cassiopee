# Importation de la fonction 'reduce' depuis le module 'functools'.
# 'reduce' permet d'appliquer une fonction cumulativement à une séquence.
from functools import reduce

# Démarre une boucle infinie qui ne s'arrêtera que lors d'un break explicite.
while True:
    # Demande à l'utilisateur de saisir une valeur et la stocke dans la variable 'n'.
    # La fonction input() renvoie une chaîne de caractères.
    n = input()
    
    # Vérifie si l'utilisateur a saisi '0000'.
    # Si oui, la boucle sera stoppée grâce à break, ce qui termine le programme.
    if n == '0000':
        break

    # Si la longueur de la chaîne 'n' est inférieure à 4 caractères,
    # la méthode zfill(4) complète avec des zéros à gauche pour obtenir exactement 4 chiffres.
    # Par exemple, '7' deviendra '0007'.
    if len(n) < 4:
        n = n.zfill(4)

    # Cette partie vérifie si tous les caractères de 'n' sont identiques.
    # [n[0] == s for s in n] crée une liste booléenne où chaque élément vaut True
    # si le caractère courant 's' est identique au premier caractère de n, sinon False.
    # Ex: pour '1111', cela donne [True, True, True, True].
    # La lambda 'lambda x, y: x and y' combinée à reduce() vérifie que tous les éléments sont True,
    # c'est-à-dire que tous les chiffres sont identiques.
    if reduce(lambda x, y: x and y, [n[0] == s for s in n]):
        # Si c'est le cas, affiche 'NA' (not applicable) car la règle des 4 chiffres identiques est une exception de Kaprekar.
        print('NA')
    else:
        # Sinon, initialise un compteur à zéro pour compter combien d'itérations sont nécessaires pour atteindre 6174.
        cnt = 0

        # Démarre une boucle qui s'arrête lorsque la valeur de 'n' devient la constante de Kaprekar : 6174.
        while n != '6174':
            # Trie la chaîne 'n' par ordre décroissant (du plus grand au plus petit chiffre)
            # puis la recompose grâce à join. Ex: '1234' devient '4321'.
            l = ''.join(sorted(n, reverse=True))
            # Trie la chaîne 'n' par ordre croissant (du plus petit au plus grand chiffre)
            # Ex: '1234' reste '1234', '4312' devient '1234'.
            s = ''.join(sorted(n))
            # Convertit les deux chaînes triées en entiers pour effectuer la soustraction.
            # La différence est ensuite convertie en chaîne de caractères et réaffectée à 'n'.
            n = str(int(l) - int(s))
            # Si le résultat de la soustraction contient moins de 4 chiffres,
            # zfill(4) complète avec des zéros à gauche pour conserver 4 caractères à chaque étape.
            if len(n) < 4:
                n = n.zfill(4)
            # Incrémente le compteur pour cette itération.
            cnt += 1
        # Lorsque la boucle atteint 6174, affiche le nombre d'itérations effectuées pour y arriver.
        print(cnt)