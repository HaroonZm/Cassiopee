rgb = set(["r", "g", "b"])

def process_worm(worm):
    """
    Traite une chaîne représentant une séquence de couleurs ('r', 'g', 'b') 
    en appliquant une transformation spécifique jusqu'à obtenir une chaîne 
    constituée d'un seul caractère ou jusqu'à un nombre maximal d'itérations.

    La transformation consiste à remplacer consécutivement deux caractères 
    différents par deux caractères identiques, choisis de manière à ne pas 
    utiliser les caractères d'origine.

    Args:
        worm (str): La chaîne initiale représentant la séquence des couleurs.

    Returns:
        int or str: Le nombre d'itérations nécessaires pour atteindre une chaîne 
        homogène si possible dans 15 itérations, sinon "NA".
    """
    n = len(worm)      # Taille de la chaîne initiale
    L = 1              # Nombre d'éléments dans le set de chaînes à traiter
    cnt = 0            # Compteur d'itérations
    flag = 0           # Indicateur si une chaîne homogène est trouvée

    # Ensemble contenant la chaîne actuelle à traiter
    quset = set([worm])

    while True:
        que = list(quset)  # Liste des chaînes à traiter au tour courant
        quset = set()      # Nouvel ensemble pour les chaînes transformées

        for r in range(L):
            Worm = que.pop(0)  # Récupérer une chaîne à traiter

            # Vérifier si la chaîne est homogène (un seul caractère)
            if len(set(Worm)) == 1:
                flag = 1
                break

            # Parcourir la chaîne pour trouver des paires consécutives distinctes
            for i in range(n - 1):
                if Worm[i] != Worm[i + 1]:
                    # Trouver la couleur qui n'est pas dans la paire en position i et i+1
                    nextclr = list(rgb - set(Worm[i:i+2]))[0]
                    # Remplacer la paire par deux caractères identiques de la couleur choisie
                    new_worm = Worm[:i] + 2 * nextclr + Worm[i + 2:]
                    quset.add(new_worm)

        L = len(quset)  # Mettre à jour le nombre de chaînes à traiter

        if flag:  # Si une chaîne homogène a été trouvée, sortir de la boucle
            break

        cnt += 1  # Incrémenter le nombre d'itérations

        if cnt > 15:  # Limite de 15 itérations pour éviter boucle infinie
            break

    # Retourner le nombre d'itérations si réussite, sinon "NA"
    return cnt if flag else "NA"

# Boucle principale qui lit les chaînes et applique le traitement
while True:
    worm = raw_input()  # Entrée utilisateur (pour Python 2)
    if worm == "0":     # Condition d'arrêt si la chaîne est "0"
        break

    result = process_worm(worm)
    print result