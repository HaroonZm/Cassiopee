# Solution détaillée pour le problème "Secret of Chocolate Poles"
# 
# Énoncé résumé :
# On veut construire des "poles" de disques de chocolat avec des contraintes :
# - Chaque pole est une pile verticale de disques.
# - Les disques peuvent être :
#   - blanc fin (épaisseur 1)
#   - noir fin (épaisseur 1)
#   - noir épais (épaisseur k)
# - La hauteur totale des disques dans un pole ≤ l.
# - Le dessus ET le dessous du pole doivent être un disque noir (fin ou épais).
# - On alterne les couleurs entre disques adjacents (blanc après noir, noir après blanc), impossible d'avoir deux blancs ou deux noirs consécutifs.
# 
# On cherche à compter le nombre de piles distinctes possibles.
#
# Approche :
# Nous utilisons une programmation dynamique (DP) pour compter les combinaisons possibles.
#
# Les états vont dépendre de :
# - épaisseur déjà utilisée
# - couleur du disque du dessus (noir ou blanc)
# - hauteur du dernier disque (fin=1 ou épais=k)
#
# Remarques / Contraintes :
# - Le premier disque (au-dessus) est noir.
# - Le dernier disque (au-dessous) est aussi noir.
# - L'épaisseur totale ≤ l
# - On alterne les couleurs : noir - blanc - noir - blanc ...
#
# La DP comptera le nombre de piles finissant par :
# - une certaine épaisseur totale utilisée,
# - un disque de couleur c au sommet,
# - avec une pile commençant par un disque noir (obligatoire).
#
# et respectant les contraintes.
#
# On utilisera deux dimensions principales :
# - l'épaisseur utilisée (0...l)
# - la couleur du disque au sommet (0=blanc, 1=noir)
#
# On devra gérer les épaisseurs des disques et les transitions sur les couleurs (noir -> blanc, blanc -> noir).
#
# Conditions spéciales :
# - Le premier disque posé est noir (on commence la pile en posant un disque noir).
# - On n'autorise que des piles terminant sur une couleur noire.
#
# Détail sur la représentation des disques noirs :
# - Le disque noir fin a épaisseur 1
# - Le disque noir épais a épaisseur k
#
# Disques blancs fins seulement (épaisseur 1).
#
# Donc transitions possibles :
# De noir (fin ou épais) -> blanc fin (1 cm)
# De blanc fin -> noir fin (1 cm) ou noir épais (k cm)
#
# On compte le nombre total de piles commençant par noir (au début), alternant couleurs, terminant sur noir, et avec épaisseur ≤ l.
#
# Implémentation :
# - dp[s][c] = nombre de piles avec épaisseur totale s, disque au sommet de couleur c,
#   (avec une pile valide commençant par noir au bas)
# - On initialise dp avec 0 sauf dp[épaisseur disque noir fin] = 1 et dp[épaisseur disque noir épais] = 1
# - Puis itération sur s de 1 à l
# - transitions selon la couleur et possible épaisseur suivante
# - On sommera à la fin dp[s][noir] pour s ≤ l (piles finissant sur noir)
#
# ATTENTION : Les piles doivent comporter au minimum un disque.
#
# Nous retournons la somme de tous dp[s][1] pour s ≤ l (car la pile doit finir sur un disque noir).
#
# La réponse peut être très grande, on utilise int natif de Python (sans modulo).
#

import sys
sys.setrecursionlimit(10**7)

def count_poles(l, k):
    # Couleurs : 0 = blanc, 1 = noir
    # épaisseur disque blanc fin : 1
    # épaisseur disque noir fin : 1
    # épaisseur disque noir épais : k
    
    # dp[s][c] nombre de piles avec épaisseur s et sommet couleur c
    # pile valide commençant par noir et alternant couleurs
    
    dp = [[0]*(2) for _ in range(l+1)]
    
    # Initialisation : un seul disque en pile (au-dessus)
    # Le disque seul doit être noir (fin ou épais)
    if 1 <= l:
        dp[1][1] += 1  # disque noir fin (épaisseur 1)
    if k <= l:
        dp[k][1] += 1  # disque noir épais (épaisseur k)
    
    for s in range(1, l+1):
        # Si au sommet c=0 (blanc fin)
        if dp[s][0] > 0:
            ways = dp[s][0]
            # Peut ajouter un disque noir (fin ou épais)
            # noir fin (1)
            if s + 1 <= l:
                dp[s+1][1] += ways
            # noir épais (k)
            if s + k <= l:
                dp[s+k][1] += ways
        
        # Si au sommet c=1 (noir)
        if dp[s][1] > 0:
            ways = dp[s][1]
            # Peut ajouter un disque blanc fin (1)
            if s + 1 <= l:
                dp[s+1][0] += ways
    
    # Somme de toutes les piles finissant sur un disque noir (c=1)
    # avec épaisseur ≤ l
    result = 0
    for s in range(1, l+1):
        result += dp[s][1]
    return result

def main():
    l,k = map(int, input().split())
    print(count_poles(l, k))

if __name__ == "__main__":
    main()