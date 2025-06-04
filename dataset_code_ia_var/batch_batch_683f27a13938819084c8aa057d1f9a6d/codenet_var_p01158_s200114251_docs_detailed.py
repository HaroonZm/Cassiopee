import sys

# Augmente la limite de récursion pour permettre un traitement de chaînes et cycles complexes
sys.setrecursionlimit(10000)

def checkloop(pdict, product, inroute, made):
    """
    Vérifie s'il existe une boucle (cycle) dans la chaîne de fournisseurs, à partir d'un produit donné.
    
    Args:
        pdict (dict): Dictionnaire mappant le nom du produit à un tuple (d1, sup, d2).
        product (str): Nom du produit à vérifier.
        inroute (list): Liste des produits visités lors du parcours actuel (pour détecter des cycles).
        made (list): Liste des produits déjà traités (non concernés par une boucle).

    Returns:
        tuple: (booléen indiquant la présence d'un cycle, point de départ du cycle ou du problème)
    """
    inroute.append(product)
    # Cas où le fournisseur est déjà traité : pas de cycle à compter ici
    if pdict[product][1] in made:
        return (False, product)
    # Cas où un produit est son propre fournisseur (cycle trivial)
    elif pdict[product][1] == product:
        return (False, product)
    # Si le fournisseur est déjà dans la route actuelle : boucle détectée
    elif pdict[product][1] in inroute:
        return (True, pdict[product][1])
    else:
        # Sinon, on poursuit récursivement la recherche de boucle avec le fournisseur
        return checkloop(pdict, pdict[product][1], inroute, made)

def daysopen(pdict, product, made, notsearched):
    """
    Calcule le nombre de jours nécessaires pour obtenir un produit, en l'absence de cycle.

    Args:
        pdict (dict): Dictionnaire mappant le nom du produit à un tuple (d1, sup, d2).
        product (str): Nom du produit à traiter.
        made (list): Liste des produits déjà traités.
        notsearched (list): Liste des produits restant à chercher.

    Returns:
        int: Nombre total de jours pour obtenir le produit en suivant la chaîne des fournisseurs.
    """
    # Si le fournisseur du produit a déjà été traité, on ajoute juste le délai du dernier achat
    if pdict[product][1] in made:
        made.append(product)
        notsearched.remove(product)
        return pdict[product][2]
    # Si le produit est son propre fournisseur, on prend le délai d'achat initial
    if pdict[product][1] == product:
        made.append(product)
        notsearched.remove(product)
        return pdict[product][0]
    else:
        # On poursuit récursivement le traitement jusqu'à atteindre la base de la chaîne
        made.append(product)
        notsearched.remove(product)
        return daysopen(pdict, pdict[product][1], made, notsearched) + pdict[product][2]

def daysloop(pdict, product, made, notsearched, inloop):
    """
    Calcule le nombre de jours nécessaires en cas de boucle dans la chaîne des fournisseurs.
    Prend le point de la boucle où la différence (d1-d2) est minimale pour optimiser le total.

    Args:
        pdict (dict): Dictionnaire mappant le nom du produit à un tuple (d1, sup, d2).
        product (str): Point de départ du cycle.
        made (list): Liste des produits déjà traités.
        notsearched (list): Liste des produits restant à chercher.
        inloop (list): Liste des produits en cours de parcours dans la boucle.

    Returns:
        int: Nombre total de jours pour franchir la boucle.
    """
    inloop.append(product)
    # Si la boucle est détectée (le fournisseur est dans la boucle actuelle)
    if pdict[product][1] in inloop:
        smallestdifference = 100000
        smallestdifferenceitem = ""
        # Recherche du produit optimal pour "sortir" du cycle (différence minimale d1-d2)
        for item in inloop:
            if smallestdifference > pdict[item][0] - pdict[item][2]:
                smallestdifference = pdict[item][0] - pdict[item][2]
                smallestdifferenceitem = item
        # On considère ce produit comme point de sortie du cycle
        days = pdict[smallestdifferenceitem][0]
        made.append(smallestdifferenceitem)
        notsearched.remove(smallestdifferenceitem)
        inloop.remove(smallestdifferenceitem)
        # Ajoute à jours la durée pour chacun des autres éléments du cycle
        for item in inloop:
            made.append(item)
            notsearched.remove(item)
            days = days + pdict[item][2]
        return days
    else:
        # On poursuit récursivement la traversée du cycle
        return daysloop(pdict, pdict[product][1], made, notsearched, inloop)

# Boucle principale pour traiter l'entrée jusqu'à ce que N soit 0
while True:
    N = int(raw_input())
    if N == 0:
        break  # Fin de l'exécution
    else:
        pdict = {}        # Dictionnaire des données pour chaque produit
        notsearched = []  # Liste des produits restant à analyser
        made = []         # Liste des produits déjà fabriqués ou pour lesquels on connaît la durée
        days = 0          # Compteur global du nombre total de jours nécessaires
        # Lecture des données produits
        for i in range(N):
            indat = raw_input().split()
            # On stocke sous la forme : nom : (d1, sup, d2)
            pdict[indat[0]] = (int(indat[1]), indat[2], int(indat[3]))
            notsearched.append(indat[0])
        # Traitement tant qu'il reste des produits non traités
        while len(notsearched) != 0:
            inroute = []  # Liste temporaire pour la vérification de cycle
            product = notsearched[0]
            # Si le fournisseur est déjà traité, on ajoute simplement son délai logistique
            if pdict[product][1] in made:
                days = days + pdict[product][2]
                made.append(product)
                notsearched.remove(product)
            else:
                # Vérifie si une boucle est présente dans la chaîne des fournisseurs
                loopbool, loopstartpoint = checkloop(pdict, product, inroute, made)
                if loopbool:
                    inloop = []
                    # Calcule la durée totale induite par le cycle
                    days = days + daysloop(pdict, loopstartpoint, made, notsearched, inloop)
                else:
                    # Aucun cycle, calcule la durée classique en suivant la chaîne des fournisseurs
                    days = days + daysopen(pdict, product, made, notsearched)
        print days