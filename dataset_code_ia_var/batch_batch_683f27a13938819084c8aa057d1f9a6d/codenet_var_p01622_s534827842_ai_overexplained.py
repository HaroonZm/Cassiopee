from __future__ import division, print_function  # Permet la division réelle par défaut et l'utilisation de print comme fonction, pour compatibilité entre Python 2 et 3

# Bloc pour assurer que 'input' fonctionne à la fois sous Python 2 (raw_input) et Python 3 (input)
try:
    input = raw_input  # En Python 2, 'raw_input' lit une ligne de texte comme chaîne de caractères; on l'assigne à 'input' pour unifier
except NameError:
    pass  # Si 'raw_input' n'existe pas (Python 3), rien à faire, 'input' existe déjà

from datetime import datetime  # Importe la classe datetime du module standard datetime (non utilisée ici, mais probablement pour des tests ou une extension)
import math                     # Importe le module math pour des fonctions mathématiques avancées (non utilisé ici, mais peut être utile)
MAXW = 1001  # Définit la constante MAXW à 1001, utilisée comme taille maximale possible pour des tableaux (notamment dp dans ce contexte)

def solve(n, read, write):
    """
    Fonction principale de résolution. 
    Prend en paramètre :
    n : nombre d'éléments
    read : liste des entiers de lecture
    write : liste des entiers d’écriture
    """
    sumR = sum(read)   # Calcule la somme totale de toutes les valeurs de la liste 'read'
    sumW = sum(write)  # Calcule la somme totale de toutes les valeurs de la liste 'write'

    next = []  # Liste pour stocker les paires (read[i], write[i]) qui répondent à une condition
    base = -1  # Initialisation d'une variable de base à une valeur impossible (sera redéfinie)
    for i in range(n):  # Boucle sur tous les éléments des listes
        if read[i] < sumR // 2:  # Si l’élément read[i] est strictement inférieur à la moitié de la somme totale de 'read'
            next.append((read[i], write[i]))  # On l’ajoute à la liste 'next' sous forme de tuple (read[i], write[i])
        else:
            base = read[i]  # Sinon, on définit 'base' comme étant la valeur de read[i]

    if (len(next) == n):  # Si tous les éléments ont été ajoutés à 'next', c’est-à-dire que 'base' n’a jamais été assignée (cas particulier)
        print(sumR + sumW)  # On affiche la somme des deux totaux
        return  # On quitte la fonction, rien d'autre à faire

    dp = [False] * MAXW  # On crée un tableau booléen 'dp' de taille MAXW, initialisé à False
                         # 'dp[i]' sera True si la somme i peut être atteinte par une combinaison de lectures
    dp[0] = True  # On peut toujours atteindre la somme 0 en ne choisissant aucun élément : on initialise dp[0] à True

    for i in range(n - 1):  # On parcourt les premiers n-1 éléments de la liste 'next'
        tmp = dp[:]  # On crée une copie de l’état actuel du tableau dp, car on va le modifier dans la boucle suivante
        for j in range(base + 1):  # On considère chaque valeur de somme possible de 0 à 'base' inclus
            if dp[j]:  # Si la somme 'j' est atteignable
                na = j + next[i][0]        # On considère le cas où on ajoute 'read' du i-ème élément de 'next'
                nb = j + next[i][0] + next[i][1]  # On considère aussi le cas où on ajoute 'read' + 'write' du même élément
                if na <= base:    # On vérifie que la nouvelle somme 'na' ne dépasse pas 'base'
                    tmp[na] = True  # On marque la somme 'na' comme atteignable
                if nb <= base:     # Pareil pour 'nb'
                    tmp[nb] = True # On marque aussi la somme 'nb' comme atteignable
        dp = tmp  # On remplace l’ancien tableau 'dp' par le nouveau après tous les ajouts de ce tour

    res = 0  # Initialisation de la variable résultat à 0
    for i in range(base + 1):  # On parcourt toutes les sommes possibles de 0 à base
        if dp[i]:  # Si la somme 'i' est possible
            res = base - i  # On met à jour 'res' à la différence 'base - i'. Ici, la dernière valeur atteinte sera gardée à la fin.

    # Le résultat final consiste à afficher la somme des 'read', des 'write', et de la valeur résiduelle 'res'
    print(sumR + sumW + res)

def main():
    """
    Fonction principale pour gérer les entrées/sorties et lancer la résolution pour plusieurs cas.
    """
    while True:  # Boucle infinie pour traiter plusieurs cas d'affilée
        n = int(input())  # Lit un entier qui détermine le nombre d'éléments à traiter dans ce cas
        if n == 0:
            return  # Si n vaut 0, on sort de la boucle et la fonction main s’arrête (fin du programme)
        read = []   # Initialise une liste vide pour stocker les valeurs de lecture
        write = []  # Initialise une liste vide pour stocker les valeurs d’écriture
        for i in range(n):  # Boucle n fois pour lire tous les couples d'entrée
            r, w = map(int, input().split())  # Lit une ligne de deux entiers séparés par un espace
            read.append(r)    # Ajoute la valeur r à la liste 'read'
            write.append(w)   # Ajoute la valeur w à la liste 'write'
        solve(n, read, write)  # Appelle la fonction de résolution avec les listes remplies

main()  # Appel final de la fonction principale pour lancer le programme