# Définition d'une fonction appelée 'check' qui vérifie si une condition particulière sur les paramètres est satisfaite.
def check(mid, b, c1, c2, q1):
    # Calcul de la quantité restante de ressource 'b' après avoir attribué 'mid' items du premier type (consommant chacun 'c1' unité).
    # Ce qui reste permet d'obtenir un certain nombre d'items du second type (consommant chacun 'c2' unité).
    # Calcul du nombre total d'items achetés : 'mid' du premier type + (quota de second type possible avec le reste).
    # On utilise la division entière '//' pour obtenir combien d'items du second type on peut acheter.
    if mid + (b - mid * c1) // c2 < q1:
        # Si la quantité totale obtenue est inférieure à la quantité requise 'q1',
        # alors on retourne False pour indiquer que ce choix de 'mid' ne convient pas.
        return False
    # Sinon, la condition est satisfaite, on retourne True.
    return True

# Boucle principale du programme : s'exécute indéfiniment jusqu'à une condition d'arrêt explicite.
while True:
    # Lecture d'une ligne de texte depuis l'entrée standard (typiquement le clavier).
    s = input()
    # Si l'utilisateur entre la chaîne "0" (sans espace ou caractère supplémentaire), cela signifie que
    # l'utilisateur souhaite terminer le programme, donc on sort de la boucle avec 'break'.
    if s == "0":
        break

    # On divise la chaîne entrée en morceaux en fonction des espaces, puis on convertit chaque morceau en entier.
    # Cela donne simultanément les *cinq* variables attendues pour le problème en une seule ligne :
    # q1 = quantite minimale d'items requise,
    # b = "budget" total disponible,
    # c1 = coût unitaire du premier type d'item,
    # c2 = coût unitaire du second type d'item,
    # q2 = maximum possible du premier type à acheter.
    q1, b, c1, c2, q2 = map(int, s.split())

    # On cherche le maximum possible d'items du premier type qu'on peut acheter, 
    # sachant qu'il ne faut pas dépasser ni notre budget ni la limite 'q2'.
    # On fait b // c1 (division entière) pour savoir combien on pourrait acheter avec tout le budget,
    # mais on respecte q2 (limite imposée). On prend donc le *minimum* de ces deux jauges.
    max_aizu = min(b // c1, q2)

    # Si le maximum d'items du premier type qu'on peut acheter est nul ou négatif,
    # cela signifie qu'il n'est pas possible d'en acheter (ni même un seul).
    # On affiche alors "NA" (not available), on continue à la prochaine itération.
    if max_aizu <= 0:
        print("NA")
        continue

    # Cas particulier : si le coût unitaire du second type est supérieur ou égal à celui du premier type,
    # il n'est pas judicieux d'acheter le second type tant qu'on peut acheter le premier.
    if c2 >= c1:
        # Calcul du nombre maximum d'items du second type qu'on peut acheter avec le budget restant, 
        # après avoir acheté le nombre maximal possible du premier type.
        max_normal = (b - max_aizu * c1) // c2  # division entière pour arrondir vers le bas.
        # Si la somme des items de chaque type achetés n'atteint pas le minimum requis 'q1',
        # On affiche "NA".
        if max_aizu + max_normal < q1:
            print("NA")
        else:
            # Sinon, on affiche la quantité achetée de chaque type : d'abord premier type, ensuite second type.
            print(max_aizu, max_normal)
        # Puisqu'on a géré ce cas particulier, on passe à la ligne suivante (prochaine entrée utilisateur).
        continue

    # Vérification rapide d'un cas d'impossibilité :
    # Pour acheter au moins 'q1' items (tous du second type sauf peut-être le premier),
    # il faut que le maximum possible d'items du second type suffise,
    # même en achetant au moins un item du premier type (c'est plus efficace car c1 < c2).
    # Si ce n’est pas possible, on imprime "NA" et on continue.
    if (b - c1) // c2 + 1 < q1:
        print("NA")
        continue

    # On cherche ici à déterminer, via une recherche dichotomique (binaire), combien d'items du premier type on doit acheter
    # pour maximiser leur nombre tout en satisfaisant la contrainte du nombre total d'items.
    left = 0  # Borne inférieure du nombre d'items du premier type à examiner.
    right = max_aizu + 1  # Borne supérieure (+1 pour rendre ce côté exclusif et s'assurer d'explorer l'ensemble de l'intervalle).

    # Tant que l'intervalle n'est pas réduit à une seule valeur de mid :
    while right - left > 1:
        # On prend le point médian de l'intervalle, division entière pour obtenir un entier.
        mid = (left + right) // 2
        # On teste si ce nombre d'items du premier type permet de satisfaire la contrainte sur le total (via la fonction check définie plus haut).
        if check(mid, b, c1, c2, q1):
            # Si c'est OK pour 'mid', on peut essayer d'en acheter plus, donc on remonte la borne inférieure à 'mid'.
            left = mid
        else:
            # Sinon, le maximum possible est plus bas, donc on diminue la borne supérieure à 'mid'.
            right = mid

    # À la sortie de la recherche binaire, 'left' contient la valeur maximale de premier type d'item qu'on peut acheter 
    # tout en respectant la contrainte principale (le nombre total minimal).
    # On affiche alors le nombre d'items du premier type, puis le nombre possible du second type calculé avec le budget restant.
    print(left, (b - left * c1) // c2)