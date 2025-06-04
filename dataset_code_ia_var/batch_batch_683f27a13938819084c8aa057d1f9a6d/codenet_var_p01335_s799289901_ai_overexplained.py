from collections import Counter  # Importe Counter de la bibliothèque collections pour compter les éléments facilement

def parse_card(card):
    # La fonction parse_card prend une carte en entrée sous forme de string, par exemple 'AS' pour As de Pique, '10H' pour Dix de Cœur, etc.
    suit = card[-1]  # La couleur de la carte est toujours le dernier caractère du string (ex : 'S', 'H', 'D', 'C')
    num = card[:-1]  # Le(s) caractère(s) avant la couleur forment la valeur de la carte (ex : '10', 'A', 'K' etc.)

    # On doit transformer les figures et l'as en leur représentation numérique, et convertir les chiffres en int
    if num == "A":  # Si c'est un As...
        num = 1     # ... sa valeur numérique est 1
    elif num == "K":  # Si c'est un Roi...
        num = 13      # ... sa valeur numérique est 13
    elif num == "Q":  # Si c'est une Dame...
        num = 12      # ... sa valeur numérique est 12
    elif num == "J":  # Si c'est un Valet...
        num = 11      # ... sa valeur numérique est 11
    elif num == "T":  # Le 'T' correspond à '10' car on veut un seul caractère pour tout
        num = 10      # ... sa valeur numérique est 10
    else:
        num = int(num)  # Sinon, il s'agit d'une carte numérotée, convertie en entier

    # On retourne un tuple contenant la valeur numérique et la couleur de la carte
    return (num, suit)

def parse_hand(hand):
    # La fonction parse_hand prend une liste de cartes (ex : ['AS','KH','TD','2C','7D']) et retourne la main sous forme de liste de (num, suit), triée
    # map applique parse_card à chaque élément de hand, ce qui retourne un itérable de tuples (num, suit)
    # sorted trie cet itérable suivant l'ordre croissant de num, puis de la couleur ASCII si égalité
    return sorted(map(parse_card, hand))

def judge(hand):
    # La fonction judge prend une main comme liste de tuples (num, suit) et retourne un code entier correspondant à la force de la main selon le poker

    # On extrait uniquement la valeur numérique de chaque carte via une compréhension de liste
    nums = [num for num, _ in hand]

    # flash_flag vérifie si toutes les couleurs (suits) sont identiques dans la main à l'aide du set :
    # si le set contient un seul élément, alors toutes les couleurs sont identiques (flush)
    flash_flag = len({suit for _, suit in hand}) == 1

    # head est la plus petite valeur numérique de la main, car la main est triée (index 0)
    head = nums[0]

    # straight_flag vérifie si la main est une suite (straight).
    # On crée une liste attendue avec 5 valeurs consécutives à partir de head, et on la compare à nums
    # Il y a une exception : As (1), 10, 11 (Valet), 12 (Dame), 13 (Roi) : cette combinaison [1,10,11,12,13] est une suite spéciale dite 'wheel'
    straight_flag = [head, head + 1, head + 2, head + 3, head + 4] == nums or [1, 10, 11, 12, 13] == nums

    # dist est une liste triée du nombre d'occurrences de chaque valeur dans la main (par exemple [1,4] pour un carré, [2,3] pour un full)
    # Counter(nums) crée un dictionnaire du type {clé:valeur} où clé est la valeur du numéro de carte, valeur est son nombre d'apparitions
    # .values() extrait la liste des occurrences
    # sorted trie cette liste pour faciliter les comparaisons
    dist = sorted(Counter(nums).values())

    # On compare dans l'ordre décroissant de force chaque configuration possible.
    # Royal Flush : Suite [1,10,11,12,13] + couleur identique (flush)
    if nums == [1, 10, 11, 12, 13] and flash_flag:
        return 9  # Code 9 pour Royal Flush
    # Straight Flush : suite + couleur identique
    if straight_flag and flash_flag:
        return 8  # Code 8 pour Straight Flush
    # Four of a Kind : distribution [1,4], c'est-à-dire une valeur apparaît 4 fois, une autre 1 fois
    if dist == [1, 4]:
        return 7  # Code 7 pour Carré
    # Full House : distribution [2,3], une valeur 3 fois et une valeur 2 fois
    if dist == [2, 3]:
        return 6  # Code 6 pour Full House
    # Flush : toutes les couleurs identiques
    if flash_flag:
        return 5  # Code 5 pour Flush
    # Straight : 5 valeurs consécutives
    if straight_flag:
        return 4  # Code 4 pour Suite
    # Three of a Kind : distribution [1,1,3], une valeur 3 fois et deux autres différentes
    if dist == [1, 1, 3]:
        return 3  # Code 3 pour Brelan
    # Two Pair : distribution [1,2,2], deux valeurs apparaissent 2 fois chacune, la dernière une seule fois
    if dist == [1, 2, 2]:
        return 2  # Code 2 pour Double Paire
    # One Pair : distribution [1,1,1,2], une valeur deux fois et trois différentes
    if dist == [1, 1, 1, 2]:
        return 1  # Code 1 pour Paire
    else:
        return 0  # Rien, main haute (carte supérieure)

def score(hand, dic, point):
    # La fonction score calcule le score d'une main en fonction de la valeur de chaque carte et du niveau de la main

    ret = 0  # Initialisation du score de la main à 0

    # Pour chaque carte dans la main (num, suit)... 
    for num, suit in hand:
        # On additionne la valeur correspondante à cette carte dans la matrice de scores "dic" (la table des valeurs pour chaque couleur)
        # On utilise num - 1 car en Python, les listes commencent à l'index 0 alors que les numéros commencent à 1
        ret += dic[suit][num - 1]

    # judge(hand) retourne le code de la force de la main (0 à 9)
    # point est une table qui donne le coefficient multiplicatif pour chaque type de combinaison
    # On multiplie donc le score total par le coefficient du type de main
    ret *= point[judge(hand)]

    return ret  # On renvoie le score final de la main

def main():
    # Fonction principale qui gère l'entrée et la sortie du programme

    first_flag = True  # Permet de savoir si nous en sommes à la première série de données (pour gérer les impressions de lignes vides entre les cas)

    while True:
        try:
            # On lit un entier n, qui est le nombre de mains à traiter dans le cas courant
            n = int(input())
        except EOFError:
            # Si la lecture échoue (fin du fichier, aucune entrée), on quitte la boucle et la fonction main()
            break

        # Si ce n'est pas la première série, on affiche une ligne vide pour séparer les blocs de sorties
        if not first_flag:
            print()
        else:
            first_flag = False  # Pour la série suivante

        dic = {}  # Dictionnaire pour stocker la table des points pour chaque couleur de carte

        # On lit les valeurs de chacune des quatre couleurs et on les associe dans dic
        dic["S"] = list(map(int, input().split()))  # Valeurs pour Pique ('S')
        dic["C"] = list(map(int, input().split()))  # Valeurs pour Trèfle ('C')
        dic["H"] = list(map(int, input().split()))  # Valeurs pour Cœur ('H')
        dic["D"] = list(map(int, input().split()))  # Valeurs pour Carreau ('D')

        # On lit les coefficients pour chaque type de mains, en insérant un zéro à la première position pour les mains 'Hautes'
        # La liste point sera de la forme [0, coeff_paire, ..., coeff_flush, ..., coeff_royal_flush]
        point = [0] + list(map(int, input().split()))

        # On traite les n mains saisies
        for _ in range(n):
            # On lit une ligne, coupe en morceaux et transforme en main de poker (listes de tuples (num, suit))
            hand = parse_hand(input().split())

            # On utilise la fonction score pour obtenir le score de la main et on l'affiche
            print(score(hand, dic, point))

main()  # Appel de la fonction principale pour démarrer le programme