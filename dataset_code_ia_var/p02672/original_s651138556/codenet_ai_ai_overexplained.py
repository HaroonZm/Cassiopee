import string  # Importe le module standard 'string' permettant d'accéder à des constantes de caractères comme les lettres et les chiffres
from heapq import heapify, heappop, heappush  # Importe trois fonctions utiles pour manipuler les files de priorité (tas) à savoir : création du tas, extraction du plus petit élément et ajout d'élément

# Définition d'une fonction appelée 'judge' qui n'est pas utilisée activement dans ce code mais sert à juger/interagir pour une session interactive.
def judge():
    import Levenshtein  # Importe la bibliothèque 'Levenshtein' qui permet de calculer la distance d'édition entre deux chaînes
    import subprocess   # Importe le module 'subprocess' pour créer et gérer des processus fils
    ans = 'OQqZbgyIYiB59fqHVsXu0PZVEWy1sApStRxCJFMeNkr5O0U4jEX9ksBTpKw7Z3ylYd3Hnd'  # Chaîne cible, à deviner
    query_count = 0  # Compte le nombre de requêtes effectuées
    # Lance un nouveau processus Python du même fichier, avec l'argument 'EXE'
    with subprocess.Popen(['python', __file__, 'EXE'],
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE) as p:
        # Boucle infinie pour traiter chaque interaction jusqu'à ce que la devinette soit terminée
        while True:
            query = p.stdout.readline().decode().strip()  # Lit une ligne de sortie, la décode en texte, et enlève les espaces autour
            print(query)  # Affiche la requête pour le débogage
            if query[0] == '?':  # Si la requête commence par un '?', c'est une demande de distance d'édition à traiter
                d = Levenshtein.distance(query[2:], ans)  # Calcule la distance de Levenshtein entre la chaîne proposée et la réponse
                print(d)  # Affiche la distance calculée
                p.stdin.write(f'{d}\n'.encode())  # Envoie la distance au processus enfant
                p.stdin.flush()  # Vide le buffer d'écriture pour s'assurer que la donnée est envoyée de suite
                query_count += 1  # Incrémente le compteur de requêtes
            elif query[0] == '!':  # Si la requête commence par un '!', c'est la proposition de réponse finale
                print(query[2:] == ans)  # Affiche si la réponse est correcte
                print(query_count)  # Affiche le nombre total de requêtes utilisées
                break  # Sort de la boucle donc termine la session
            else:
                pass  # Ne rien faire pour les autres cas (ici aucun autre cas n'est prévu)

# (Bloc commenté) Ce code vérifierait si le script est exécuté en mode 'test interactif' ou non et lancerait la fonction 'judge' si besoin.
# import sys
#
# if len(sys.argv) == 1:
#     print('Interactive Test Mode')
#     judge()
#     exit()

# STR est la chaîne contenant toutes les lettres ASCII en minuscules, en majuscules, et tous les chiffres décimaux (0 à 9)
STR = string.ascii_letters + string.digits

counter = {}  # Dictionnaire vide qui servira à compter les occurrences de chaque caractère dans la chaîne cible, selon la logique du jeu

# Pour chaque caractère 'c' dans la chaîne STR (soit, pour chaque lettre et chaque chiffre) :
for c in STR:
    # On affiche une requête de demande au juge :
    # '? {c * 128}' correspond à une chaîne constituée de 128 fois le caractère c.
    print(f'? {c * 128}')
    # Lecture de la réponse du juge, réponse qui doit être un entier représentant la distance de Levenshtein entre la chaîne d'entrée et la réponse cible.
    a = int(input())
    # Si la distance retournée est 128, cela signifie qu'aucune occurence de 'c' n'est dans la réponse cible
    # (Puisque toutes les lettres doivent être changées, aucune lettre ne correspond)
    if a == 128:
        continue  # On passe au caractère suivant sans rien faire
    # Sinon, il y a exactement (128 - a) lettres 'c' dans la chaîne cible.
    counter[c] = 128 - a  # On enregistre ce nombre dans le dictionnaire sous la clé 'c'

# Calculer le nombre total de caractères utiles dans la chaîne cible
l = sum(counter.values())  # Somme des occurrences de tous les caractères présents dans la cible

# Construction d'une liste de tuples chacun contenant un compteur (nb d'occurences) et une liste de ce même caractère répété
q = [(cnt, [c] * cnt) for c, cnt in counter.items()]

# Transforme la liste 'q' en un tas (heap) selon la première valeur de chaque tuple pour pouvoir toujours extraire les plus petits groupes en priorité
heapify(q)

# Tant qu'il reste au moins deux groupes dans le tas (c'est-à-dire qu'il n'est pas réduit à la chaîne unique finale)
while len(q) > 1:
    l1, t1 = heappop(q)  # On retire le plus petit groupe, récupération de sa taille (l1) et de sa liste de caractères (t1)
    l2, t2 = heappop(q)  # On retire le second plus petit groupe
    i = 0  # Indice pour parcourir la liste t1
    j = 0  # Indice pour parcourir la liste t2
    # On veut fusionner t2 dans t1 en essayant toutes les insertions possibles, de gauche à droite
    while i < len(t1) and j < l2:
        t1.insert(i, t2[j])  # On insère l'élément courant de t2 à la position i de t1
        s = ''.join(t1)  # On crée la chaîne résultante de la liste t1
        print(f'? {s}')  # On envoie une requête au juge pour connaître sa distance avec la chaîne cible
        a = int(input())  # Lecture de la réponse (distance de Levenshtein)
        # Si la taille de t1 dépasse le nombre de bonnes positions détectées (soit : t1 est incorrectement modifiée)
        if len(t1) > l - a:
            t1.pop(i)  # On supprime l'insertion précédente car elle a dégradé la qualité du résultat
        else:
            j += 1  # Sinon, on valide l'insertion et passe à la lettre suivante de t2 à insérer
        i += 1  # Dans tous les cas, on décale la position d'insertion à droite pour continuer à tester toutes les positions
    # Si jamais on n'a pas fini d'intégrer tous les caractères de t2, on les ajoute à la fin
    if j < len(t2):
        t1.extend(t2[j:])

    # Enfin, on remet le nouveau groupe fusionné (avec sa taille totale et la liste des lettres ordonnées) dans le tas pour continuer le processus
    heappush(q, (l1 + l2, t1))

# À la fin de la boucle, il reste un seul groupe (la chaîne finale reconstituée) dans la file de priorité/q
_, t = q[0]  # On extrait cette liste de caractères (on ignore la longueur car on sait qu'elle fait 'l')
s = ''.join(t)  # On crée la chaîne définitive en assemblant toutes les lettres de la liste

print(f'! {s}')  # On affiche la réponse finale au format demandé, ce qui devrait permettre de valider la chaîne reconstruite