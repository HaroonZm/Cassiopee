"""
AOJ ITP2_1_D: Vector II

Ce module implémente une version simplifiée de "vecteurs" associatifs via une liste de deque, selon les instructions des entrées standard.  
Fonctionnalités principales :
- Ajouter un élément à la fin d'un vecteur.
- Afficher le contenu d'un vecteur.
- Vider complètement un vecteur.

Auteur original : bal4u, version réécrite avec docstrings et commentaires détaillés.
"""

from collections import deque

def main():
    """
    Point d'entrée principal du script.
    
    Lis d'abord deux entiers depuis l'entrée standard :
        n : nombre de vecteurs à gérer.
        q : nombre de requêtes à traiter.
    Crée une liste de 'n' deque pour stocker les éléments de chaque vecteur.
    Traite ensuite 'q' requêtes, qui peuvent être :
        - Ajouter un élément à la fin d'un vecteur (pushBack).
        - Afficher le contenu d'un vecteur (dump).
        - Vider le vecteur (clear).
    """
    # Lecture du nombre de vecteurs 'n' et du nombre de requêtes 'q'
    n, q = map(int, input().split())
    
    # Initialisation d'une liste de n vecteurs, chacun étant une deque vide
    vectors = []
    for _ in range(n):
        vectors.append(deque())
    
    # Traitement des q requêtes
    for _ in range(q):
        process_command(input().split(), vectors)

def process_command(cmd, vectors):
    """
    Traite une commande sur un des vecteurs.
    
    Args:
        cmd (list of str): Liste contenant la commande et ses arguments.
            cmd[0] : type de la commande ('0', '1' ou '2').
            cmd[1] : index du vecteur ciblé (sous forme de chaîne, à convertir en int).
            cmd[2] : valeur à ajouter (seulement si type '0').
        vectors (list of deque): La liste des vecteurs manipulés.
    """
    # Extraction de l'indice du vecteur concerné
    t = int(cmd[1])
    if cmd[0] == '0':
        # Commande '0' : pushBack
        # Ajout de l'élément cmd[2] à la fin du vecteur t
        vectors[t].append(cmd[2])
    elif cmd[0] == '1':
        # Commande '1' : dump
        # Affichage de tous les éléments du vecteur t, séparés par des espaces. 
        print(*vectors[t])
    else:
        # Tout autre type (ici uniquement '2') : clear
        # Suppression de tous les éléments du vecteur t
        vectors[t].clear()

if __name__ == '__main__':
    main()