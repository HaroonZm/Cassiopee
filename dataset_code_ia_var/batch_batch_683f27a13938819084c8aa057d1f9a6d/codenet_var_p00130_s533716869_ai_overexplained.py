import sys  # Le module sys permet d'accéder à des fonctions et des objets liés à l'interpréteur Python.
from sys import stdin  # On importe stdin pour lire les entrées standards (comme input mais plus performant).
input = stdin.readline  # On redéfinit 'input' pour lire une ligne de l'entrée standard plus rapidement.

from collections import deque  # Permet d'utiliser une file double-ended pour la BFS.

def bfs(u, result, out_edge, in_degree, processed):
    # Fonction effectuant un parcours en largeur (BFS : Breadth-First Search) à partir du sommet 'u' dans le graphe.
    # u : sommet de départ (index entier).
    # result : liste où sera stockée l'ordre des sommets traités.
    # out_edge : liste d'adjacence représentant pour chaque sommet, la liste des sommets vers lesquels il pointe.
    # in_degree : tableau contenant pour chaque sommet, son degré entrant (nombre d'arêtes qui arrivent dessus).
    # processed : tableau booléen indiquant si chaque sommet a déjà été traité par la BFS.

    q = deque()  # On crée une file (queue) pour gérer l'ordre de traitement des sommets à explorer.
    q.append(u)  # On ajoute le sommet de départ à la file.
    processed[u] = True  # On marque le sommet de départ comme traité.
    while q:  # Tant qu'il reste des sommets à explorer dans la file :
        u = q.popleft()  # On enlève le sommet en tête de la file pour le traiter maintenant.
        result.append(u)  # On ajoute ce sommet à la liste des résultats (ordre de traitement/topologique).
        for e in out_edge[u]:  # Pour chaque sommet 'e' accessible depuis 'u' (arête sortante de 'u') :
            in_degree[e] -= 1  # On diminue son degré entrant, car 'u' (un de ses prédécesseurs) vient d'être traité.
            # Si ce sommet atteint maintenant un degré entrant nul, c'est qu'il n'a plus de prédécesseur à traiter.
            if in_degree[e] == 0 and processed[e] == False:
                processed[e] = True  # On marque ce sommet comme traité.
                q.append(e)  # On l'ajoute à la file pour le traiter ultérieurement.

def solve(V, in_degree, out_edge):
    # Fonction qui réalise un tri topologique sur un graphe orienté.
    # V : nombre total de sommets dans le graphe.
    # in_degree : tableau du degré entrant de chaque sommet.
    # out_edge : liste d'adjacence des arcs sortants de chaque sommet.
    result = []  # Liste à remplir avec l'ordre topologique des sommets.
    processed = [False for _ in range(V)]  # Tableau pour marquer si chaque sommet a été traité (False au départ).
    for i, u in enumerate(in_degree):  # Pour chaque sommet, on regarde son degré entrant.
        if u == 0 and processed[i] == False:  # Si le sommet n'a pas de prédécesseur, on commence une BFS depuis lui.
            bfs(i, result, out_edge, in_degree, processed)
    return result  # On renvoie l'ordre topologique obtenu.

def decode_txt(S):
    # Cette fonction décode la chaîne S décrivant les contraintes d'ordre sous forme de texte.
    # Elle extrait tous les couples d'arêtes orientées imposées par S ainsi que la liste des 'voitures' (caractères uniques).
    es = set()  # Ensemble pour stocker de façon unique les arcs (arêtes orientées).
    cars = set()  # Ensemble des 'voitures', c'est-à-dire des caractères distincts rencontrés dans S.
    l = len(S)  # Longueur totale de la chaîne S.

    # On parcourt la chaîne caractère par caractère.
    for i in range(l):
        # On ignore les caractères qui ne sont pas des lettres minuscules (entre 'a' et 'z').
        if not 'a' <= S[i] <= 'z':
            continue
        s = S[i]  # On récupère le caractère à la position i, qui correspond à une voiture.
        # On essaie de récupérer le caractère à i+3, qui est la voiture cible dans la contrainte.
        try:
            t = S[i+3]  # Le caractère 3 positions plus loin est la destination de l'arc.
        except IndexError:
            break  # Si on dépasse la longueur de chaîne, on arrête la boucle.
        cars.add(s)  # On ajoute 's' (la voiture actuelle) à l'ensemble de toutes les voitures.
        cars.add(t)  # On ajoute aussi 't' (la voiture destination).
        # Si le caractère à la position suivante est '-', cela signifie que l'ordre est de 's' vers 't'.
        if S[i+1] == '-':
            es.add((s, t))  # On ajoute l'arc orienté (s, t) à l'ensemble.
        else:
            es.add((t, s))  # Sinon, l'ordre est de 't' vers 's', donc on ajoute (t, s).
    return es, cars  # On renvoie l'ensemble des arcs et l'ensemble des voitures.

def main(args):
    # Fonction principale du programme, exécutée lorsqu'on lance le script.
    n = int(input())  # On lit un entier depuis l'entrée standard, indiquant le nombre d'essais à traiter.
    for _ in range(n):  # On répète le traitement pour chaque cas d'essai.
        S = input().strip()  # On lit la ligne correspondante, en supprimant les espaces ou retours chariots en trop.
        if len(S) < 4:  # Si la chaîne est trop courte pour contenir une contrainte, on affiche directement S.
            print(S)
            continue  # On passe au cas d'essai suivant.
        # Sinon, on décode la chaîne pour obtenir la liste des arcs et des voitures.
        es_txt, cars = decode_txt(S)

        V = len(cars)  # On compte le nombre total de voitures, qui forme le nombre de sommets du graphe.
        num = 0  # Compteur pour attribuer à chaque voiture un numéro unique allant de 0 à V-1.
        mapping = dict()  # Dictionnaire associant chaque caractère de voiture à son index.
        for c in cars:  # Pour chaque voiture (chaîne caractères unique dans 'cars') :
            mapping[c] = num  # On lui associe le numéro courant.
            num += 1  # On incrémente le numéro pour la prochaine voiture.
        # On crée la correspondance inverse, pour retrouver la voiture à partir de son numéro d'index.
        rev_mapping = dict(zip(mapping.values(), mapping.keys()))
        es = []  # Liste des arcs sous forme d'indices numériques.
        for s, t in es_txt:  # Pour chaque arc sous forme de caractères d'origine et destination :
            es.append([mapping[s], mapping[t]])  # On ajoute cet arc avec les indices correspondants.

        in_degree = [0 for _ in range(V)]  # On initialise le degré entrant de chaque sommet à 0.
        out_edge = [[] for _ in range(V)]  # On initialise la liste des arcs sortants pour chaque sommet à une liste vide.
        for s, t in es:  # Pour chaque arc (s, t), on met à jour in_degree et out_edge :
            out_edge[s].append(t)  # On ajoute t à la liste des voisins sortants de s.
            in_degree[t] += 1  # On augmente le degré entrant de t (il reçoit un arc supplémentaire).

        result = solve(V, in_degree, out_edge)  # On effectue le tri topologique pour obtenir l'ordre correct.
        # On convertit la liste d'indices du résultat en la liste des caractères correspondants (voitures).
        txt = [rev_mapping[x] for x in result]
        print(''.join(txt))  # On affiche la solution transformée en chaîne de caractères, sans espaces.

# Ce bloc spécial permet de lancer la fonction main seulement si le script est exécuté (et pas importé comme module).
if __name__ == '__main__':
    main(sys.argv[1:])  # On transmet à main la liste des arguments de ligne de commande (qui n'est pas utilisée ici).