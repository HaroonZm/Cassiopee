import sys  # Importe le module système (gère les flux standards, arguments, sortie, etc.)
import math  # Importe le module mathématiques (pour accès à fonctions comme sqrt()

OFFSET = 20  # Déplacement de l'index pour indexer de -20 à +19 via un tableau de taille positive

def main():
    # Boucle principale, en attente d'entrées successives
    while True:
        # Lit une ligne depuis l'entrée standard (généralement clavier ou pipe)
        # Utilise .split() pour séparer les valeurs par espaces et map(int, ...) pour transformer en entiers
        r, n = map(int, sys.stdin.readline().split())
        # Condition d'arrêt : si les deux entrées sont nulles (0 0), on quitte la boucle
        if r == 0 and n == 0:
            break

        # Initialise une séquence de hauteurs pour chaque position possible, taille 40
        # Le tableau est initialisé à 0 pour indiquer qu'aucune hauteur n'est posée
        # seq[i] représentera la hauteur maximale entre les positions correspondant à l'indice i
        seq = [0] * 40

        # Pour chaque segment donné en entrée (il y en a n au total)
        for i in range(n):
            # Récupère trois entiers : les bornes du segment (x1, x2), ainsi que la hauteur h
            x1, x2, h = map(int, sys.stdin.readline().split())
            # Parcourt toutes les positions de x1 à x2-1 (extrémité droite exclue)
            for k in range(x1, x2):
                # On utilise OFFSET pour indexer dans seq qui va de 0 à 39 au lieu de -20 à +19
                # On conserve pour chaque position la hauteur maximale rencontrée jusqu'à présent
                seq[k + OFFSET] = max(seq[k + OFFSET], h)

        # Initialisation de la variable de réponse (valeur minimale à déterminer)
        # Une valeur très grande sert à l'initialisation, pour être remplacée par tout résultat calculé plus petit
        ans = 9999999999
        # Pour chaque valeur x allant de -r+1 à r-1 inclus (plage centrée autour de zéro)
        for x in range(-r+1, r):
            # Pour chaque x, on considère deux points adjacents x-1 et x dans la séquence
            # On récupère la hauteur minimale parmi ces deux positions, ce qui simule la limite basse entre deux segments
            y = min(seq[x + OFFSET - 1], seq[x + OFFSET])
            # Calcule la position verticale à cet endroit :
            # y + r est la somme de la hauteur rencontrée et du rayon du cercle
            # sqrt(r*r - x*x) est la hauteur du cercle à l'abscisse x (théorème de Pythagore)
            # Donc y + r - sqrt(r*r - x*x) donne l'ordonnée de la base courante plus l'élévation du cercle
            t = y + r - math.sqrt(r*r - x*x)
            # Mettre à jour notre réponse avec la valeur minimale trouvée jusqu'à présent
            ans = min(ans, t)

        # Affiche la réponse formatée avec 4 chiffres après la virgule
        print("{0:.4f}".format(ans))

# Ce bloc vérifie si le script est exécuté directement (et non importé comme un module)
if __name__ == '__main__':
    main()  # On appele la fonction principale pour lancer le traitement