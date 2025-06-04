from sys import stdin  # Importation du module 'sys' pour accéder à l'entrée standard (stdin)
from itertools import repeat  # Importation de la fonction 'repeat' du module 'itertools' (non utilisé dans ce code modifié)

def f(a):
    # Cette fonction prend en argument une liste 'a'
    # Elle retourne une liste 'l' accumulant certains coûts calculés via traitement de 'a'
    n = len(a)  # Détermination de la longueur de la liste d'entrée 'a'
    
    # Initialisation d'une liste 'l' de taille n+1 contenant des zéros
    # Cette liste est utilisée pour enregistrer les coûts cumulés à chaque étape
    l = [0] * (n + 1)
    
    # Initialisation d'une pile (implémentée comme une liste) 'st' avec un seul élément tuple
    # Ce tuple contient (a[0], a[0], 1), représentant le premier élément de 'a' deux fois,
    # et le nombre 1 signifiant la quantité associée dans le calcul ultérieur
    st = [(a[0], a[0], 1)]
    
    # Raccourcis locaux pour les méthodes append (pu) et pop (po) de la pile 'st'
    pu = st.append
    po = st.pop
    
    # Boucle pour parcourir les éléments restants de la liste 'a'
    for i in range(1, n):
        ad = 0  # Initialisation d'un accumulateur 'ad' à zéro pour suivre l'"ajout" total sur cet indice
        y = a[i]  # Définition de 'y' comme étant l'élément courant de la liste 'a'
        k = 1  # Initialisation du compteur/quantité à 1 pour ce tour
        
        # Tant que la pile 'st' n'est pas vide ET que la valeur courante 'y' est supérieure à la première composante
        # du dernier tuple de la pile (st[-1][0]), faire :
        while st and y > st[-1][0]:
            x, z, q = po()  # Dépile le dernier élément de la pile, qui est un tuple (x, z, q)
            
            c = 0  # Initialisation d'une variable 'c' à zéro pour compter les doubles-multiplications
            
            # Boucle interne : tant que 'x' est strictement inférieur à 'y'
            while x < y:
                x *= 4  # On multiplie 'x' par 4. (équivalent à x = x * 4)
                c += 2  # Incrémente 'c' de 2 à chaque multiplication (sert de compteur d'opérations)
            
            # Ajoute au total 'ad' la valeur 'c' * 'q', c'est-à-dire le nombre de double-multiplications
            # multiplié par la quantité extraite du tuple dépilé
            ad += c * q
            
            # Incrémente 'k' avec 'q', pour combiner les "quantités" fusionnées lors du traitement
            k += q
            
            # Met à jour 'y' au maximum entre l'ancien 'z' fois 2^c (ici, équivalent shifting left by c bits)
            # Comme c est systématiquement pair, c // 2 nous donnerait le nombre de multiplications par 4
            y = z << c  # Décale z à gauche de c bits (équivalant à multiplication par 2^c)
        
        # Ajoute un nouveau tuple à la pile 'st' pour poursuivre le traitement
        pu((a[i], y, k))
        
        # Met à jour la valeur suivante de la liste 'l', en y ajoutant le coût 'ad' à la valeur précédente
        l[i + 1] = l[i] + ad
    
    # A la fin, retourne la liste calculée 'l'
    return l

def main():
    # Fonction principale pour gérer l'ensemble du programme
    
    # Lecture d'une ligne depuis l'entrée standard, suppression du saut de ligne, conversion en entier
    n = int(stdin.readline())
    
    # Lecture de la ligne suivante depuis l'entrée standard (supposée contenir des entiers)
    # Découpage en éléments, conversion de chaque élément en entier pour obtenir la liste 'a'
    a = list(map(int, stdin.readline().split()))
    
    # Appel de la fonction f sur la liste 'a', stockage du résultat dans 'l'
    l = f(a)
    
    # Appel de la fonction f sur la liste inversée 'a[::-1]', puis inversion du résultat avec [::-1],
    # cela permet d'appliquer le même traitement dans l'autre sens de la liste, stockage dans 'r'
    r = f(a[::-1])[::-1]
    
    # Initialisation d'une variable 'ans' avec une très grande valeur (10^12)
    # Cette variable contiendra le résultat minimal trouvé lors de la boucle suivante
    ans = 10 ** 12
    
    # Boucle sur tous les indices de 0 à n inclus (range(n+1))
    for i in range(n + 1):
        
        # Si la somme des valeurs l[i], i et r[i] est inférieure à la valeur actuelle de ans,
        # alors on met à jour ans avec cette valeur plus petite
        if ans > l[i] + i + r[i]:
            ans = l[i] + i + r[i]
    
    # Affiche la valeur minimale trouvée
    print(ans)

# Appel à la fonction principale pour lancer le programme
main()