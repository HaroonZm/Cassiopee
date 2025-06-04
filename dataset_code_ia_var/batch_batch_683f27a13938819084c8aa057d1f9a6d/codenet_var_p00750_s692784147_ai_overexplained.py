from collections import defaultdict  # Importation de defaultdict depuis le module collections, permet de créer des dictionnaires avec des valeurs par défaut

def main(n, a, s, g):  # Définition de la fonction principale prenant 4 arguments : nombre de sommets, d'arêtes, sommet de départ, sommet d'arrivée
    # Création d'une liste d'adjacence pour représenter le graphe, initialisée avec des listes vides pour chaque sommet
    edg = [[] for i in range(n)]  # Chaque élément est une liste d'arêtes sortantes depuis le sommet i

    # Boucle pour lire chaque arête du graphe
    for _ in range(a):  # Pour chaque arête à ajouter dans le graphe
        x, y, lab = input().split()  # Lecture et découpage de l'entrée en trois parties : origine, destination, étiquette
        x, y = int(x), int(y)  # Conversion des sommets en entiers (car ils sont lus sous forme de chaînes de caractères)
        edg[x].append((y, lab))  # Ajout d'un tuple (destination, étiquette) dans la liste du sommet d'origine

    inf = "{"  # Valeur spéciale représentant l'infini pour les chaînes (plus grande que n'importe quelle minuscule)
    # Création d'une matrice dp: dp[i][j] contient le plus petit mot, selon l'ordre lexicographique, atteignant le sommet i en j étapes
    dp = [[inf] * 2600 for i in range(n)]  # Remplie initialement par l'infini pour tous les sommets et longueurs (ici jusqu'à 2599 inclus)
    dp[s][0] = ""  # Depuis le sommet de départ, avec longueur 0, le mot vide est le chemin le plus petit

    # Création d'un dictionnaire d pour mémoriser, pour chaque sommet et longueur, un masque de sommets visités (pour détection de cycles)
    d = defaultdict(lambda: defaultdict(int))  # Par défaut, les valeurs sont des entiers (0)

    # Dictionnaire X : pour chaque longueur, indique les sommets atteints à cette longueur
    X = defaultdict(list)  # Par défaut, liste vide
    X[0] = [s]  # À la longueur 0, seul le sommet de départ est accessible

    # Boucle principale pour essayer toute longueur de chemin jusqu'à 2500
    for leng in range(2500):  # Pour chaque longueur de 0 à 2499
        for i in set(X[leng]):  # Pour chaque sommet unique atteint à cette longueur
            l = dp[i][leng]  # Récupère le chemin courant (chaîne) pour ce sommet et cette longueur
            if l == inf: continue  # Si ce chemin n'est pas accessible (valeur infinie), on passe
            for e, lab in edg[i]:  # Pour chaque sortie depuis ce sommet i (e = destination, lab = étiquette/arête)
                if leng + len(lab) > 2500: continue  # Si la longueur totale du mot dépasse la limite, on ignore cet arc
                x = l + lab  # Concaténation du mot courant et de l'étiquette de l'arête (nouveau chemin)
                if dp[e][leng + len(lab)] > x:  # Si on a trouvé un chemin lexicographiquement plus petit pour e à cette longueur
                    # Mise à jour du masque des sommets visités sur ce chemin
                    d[e][leng + len(lab)] = d[i][leng] | (1 << i)  # Ajoute le sommet i visité dans le masque de bits
                    dp[e][leng + len(lab)] = x  # Met à jour le plus petit mot pour e à cette longueur
                    X[leng + len(lab)].append(e)  # Note que e est accessible à la nouvelle longueur

    ans = inf  # Variable pour stocker la réponse finale (initialement à infini)
    for i in range(2500):  # Parcourt toutes les longueurs possibles
        if dp[g][i] < ans:  # Si on a trouvé un mot plus petit pour atteindre le sommet g
            ans = dp[g][i]  # Met à jour la réponse

    if ans == inf:  # Si l'infini, aucun chemin n'a été trouvé
        print("NO")  # Affiche "NO" pour indiquer qu'il n'existe pas de chemin
        return  # Quitte la fonction

    # Vérification supplémentaire pour s'assurer de l'optimalité du mot trouvé :
    for leng in range(10):  # On considère les chemins encore un peu plus longs (de 2400 à 2409)
        leng += 2400  # Décalage pour atteindre la plage voulue
        for i in range(n):  # Pour chaque sommet du graphe
            l = dp[i][leng]  # Chemin courant pour ce sommet et cette longueur
            for e, lab in edg[i]:  # Pour chaque arête sortante depuis i
                x = l + lab  # Nouveau chemin potentiel
                # Vérifie si un chemin lexicographiquement plus petit existe via un cycle permettant de raccourcir/optimiser ans
                if x < ans and ((d[g][len(ans)] & (1 << e)) or (e == g)):
                    # Si tel chemin existe et rejoint g ou repasse par un sommet déjà dans le chemin final :
                    print("NO")  # La solution n'est pas valide (boucle non optimale)
                    return  # Quitte la fonction

    print(ans)  # Envoie le résultat final, c'est-à-dire le plus petit mot trouvé pour aller de s à g

if __name__ == "__main__":  # Condition spéciale s'assurant que ce code est exécuté en tant que script principal (pas lors d'un import)
    while 1:  # Boucle infinie pour traiter des instances successives du problème
        n, a, s, g = map(int, input().split())  # Lecture de quatre entiers : sommets, arêtes, départ, arrivée
        if n == 0: break  # Si le nombre de sommets est zéro, on termine la boucle (cas d'arrêt)
        main(n, a, s, g)  # Appel de la fonction principale pour traiter la nouvelle instance du problème