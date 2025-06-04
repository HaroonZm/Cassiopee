# Définition de la fonction principale du programme
def main():
    # Lecture de la première ligne de l'entrée standard, typiquement espace-séparée (par exemple "3 5")
    s1 = input()
    # Lecture de la deuxième ligne de l'entrée standard, typiquement espace-séparée (par exemple "1 2 3 10 20")
    s2 = input()
    # Appel de la fonction solve avec les deux chaînes d'entrée, retourne le résultat dans ret
    ret = solve(s1, s2)
    # Affichage dans la sortie standard du résultat calculé
    print(ret)

# Définition de la fonction 'solve' qui prend deux paramètres : s1 et s2 (tous deux des chaînes de caractères)
def solve(s1, s2):
    # On découpe la chaîne 's1' selon les espaces et on convertit chaque morceau en entier,
    # le résultat est décompressé dans les variables N et M
    N, M = list(map(int, s1.split()))
    
    # On découpe la chaîne 's2' selon les espaces et on convertit chaque morceau en entier,
    # pour obtenir la liste X des coordonnées (par exemple [1, 2, 3, 10, 20])
    X = list(map(int, s2.split()))
    
    # Si le nombre de groupes ou capteurs (N) est supérieur ou égal au nombre de positions (M),
    # alors il n'est pas nécessaire de regrouper les positions (ou regrouper chaque position individuellement),
    # donc la somme minimale des distances couvertes est zéro (aucun déplacement nécessaire)
    if (N >= M):
        return 0

    # On trie la liste X par ordre croissant pour que les différences soient calculées sur des positions adjacentes
    X.sort()

    # On crée une liste vide l dans laquelle on va stocker les distances entre chaque paire de positions adjacentes
    l = []

    # La boucle parcourt chaque indice 'i' de 0 à M-2 (car pour M éléments, il y a M-1 intervalles),
    # et on calcule la différence entre la position suivante et la position actuelle
    for i in range(M-1):
        l.append(X[i+1] - X[i])  # On ajoute la différence dans la liste l

    # On trie la liste des intervalles de distance calculés par ordre croissant,
    # afin de pouvoir facilement sélectionner les plus petites distances
    l.sort()

    # Initialisation du compteur de la somme totale minimale des distances sélectionnées
    ct = 0

    # On souhaite regrouper les positions en N groupes,
    # ce qui revient à supprimer les N-1 plus grands intervalles pour minimiser la distance totale,
    # donc on additionne les M-N plus petits intervalles
    for j in range(M-N):
        ct += l[j]  # On ajoute la distance la plus petite encore non prise en compte à la somme ct

    # On retourne la somme minimale des distances après regroupement optimal
    return ct

# Appel initial de la fonction principale pour démarrer l'exécution du programme
main()