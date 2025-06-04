# Importation du module Counter depuis la bibliothèque collections.
# Counter est utile pour compter les occurrences d'éléments dans une séquence mais n'est pas utilisé ici finalement.
from collections import Counter

# Importation du module sys pour permettre la manipulation des entrées/sorties standard à très bas niveau.
import sys

# Définition de la fonction solve qui sert à résoudre le problème donné pour un jeu de données.
def solve():
    # Assignation d'une fonction raccourcie 'readline' pour lire une ligne depuis l'entrée standard de façon efficace.
    # sys.stdin.buffer.readline lit directement les octets d'entrée.
    readline = sys.stdin.buffer.readline
    
    # Assignation d'une fonction raccourcie 'write' pour écrire des octets sur la sortie standard.
    write = sys.stdout.buffer.write
    
    # Lecture d'une ligne d'entrée et séparation des données en entiers.
    # readline().split() renvoie une liste de chaînes, map(int, ...) convertit chaque chaîne en entier.
    M, N = map(int, readline().split())
    
    # Si les deux valeurs M et N lues sont nulles, cela indique la fin de l'entrée.
    # Double égalité '==' vérifie que M == N et N == 0.
    if M == N == 0:
        # On retourne False pour indiquer que la boucle doit s'arrêter.
        return False
    
    # Création d'une liste B contenant N éléments tels que :
    # - readline() lit la ligne suivante en binaire (octets)
    # - int(..., 2) convertit la chaîne binaire lue en entier (base 2)
    # L'opération est effectuée pour chaque i dans l'intervalle N (de 0 à N-1).
    B = [int(readline(), 2) for i in range(N)]
    
    # Création d'un dictionnaire 'memo' servant de mémoization pour enregistrer les résultats intermédiaires de certaines requêtes,
    # ce qui accélère les appels récursifs en évitant de recalculer les mêmes situations.
    memo = {}
    
    # Définition de la fonction récursive 'dfs', qui explore l'espace des solutions possibles.
    # s : un entier représentant un ensemble de bits (quels attributs sont sélectionnés/fixés)
    # t : un entier représentant la valeur fixée de ces attributs
    def dfs(s, t):
        # Construction d'une clef, qui est un tuple des paramètres (s, t), pour indexer le dictionnaire de mémoization.
        key = (s, t)
        # Si on a déjà résolu ce sous-problème, on retourne la valeur enregistrée tout de suite.
        if key in memo:
            return memo[key]
        
        # Compteur permettant de compter combien d'éléments dans B satisfont la condition suivante.
        c = 0
        # Parcours de chaque élément b dans B.
        for b in B:
            # (b & s) fait un ET bit à bit entre b et s. On vérifie si le résultat est égal à t.
            # Cela signifie que, pour chaque bit fixé dans s/t, b a la même valeur pour ces bits.
            if (b & s) == t:
                # Incrémentation de c, car cet élément correspond aux bits imposés par s/t.
                c += 1
        # Si le nombre d’éléments satisfaisant la condition est inférieur ou égal à 1, alors plus de découpage ne sert à rien.
        if c <= 1:
            # On mémorise cette valeur pour la clef key : pas besoin de question supplémentaire.
            memo[key] = 0
            # On retourne 0 : plus aucune séparation n'est nécessaire.
            return 0
        # Initialisation de la variable résultat à M (le nombre maximum possible de questions).
        res = M
        # On teste chaque attribut/bit position i de 0 à M-1.
        for i in range(M):
            # b est égal à 1 << i, c’est-à-dire un masque avec le bit i activé.
            b = (1 << i)
            # Si ce bit n’a pas encore été testé/fixé dans s (le bit i est à 0 dans s).
            if s & b == 0:
                # dfs(s|b, t) : on teste en ajoutant le bit avec valeur 0 (la question "bit i = 0")
                # dfs(s|b, t|b) : on teste en ajoutant le bit avec valeur 1 (la question "bit i = 1")
                # On prend le maximum des deux (cas le plus difficile), puis on ajoute 1 pour la question posée.
                res = min(res, max(dfs(s|b, t), dfs(s|b, t|b))+1)
        # On mémorise le résultat calculé pour cette clef pour accélérer les appels ultérieurs.
        memo[key] = res
        # On retourne la valeur finale obtenue.
        return res

    # On appelle la fonction dfs avec s = 0 (aucun bit fixé), t = 0 (pas de valeur assignée) pour démarrer la recherche complète.
    # La fonction write attend des bytes : "%d\n" % ... formate le résultat entier suivi d'un retour à la ligne, puis .encode('ascii') automatiquement lors du passage à bytes par l'opérateur %.
    write(b"%d\n" % dfs(0, 0))
    # Comme l'entrée suivante doit être traitée, on retourne True.
    return True

# La boucle principale appelle la fonction solve tant qu’elle retourne True.
# Lorsqu'elle retourne False (fin de données), la boucle s’arrête.
while solve():
    # Les trois points '...' indiquent explicitement une opération nulle ; ici ils sont inutiles mais ne gênent pas le fonctionnement.
    ...