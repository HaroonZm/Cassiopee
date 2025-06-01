import sys

def pokakito(num_line):
    """
    Essaie de trouver une combinaison valide dans la liste num_line selon des règles spécifiques.
    
    Cette fonction est récursive et tente de diviser num_line en groupes de trois ou deux 
    éléments égaux, ou en séquences consécutives de trois nombres.

    Args:
        num_line (list of int): Liste des nombres à analyser.
        
    Returns:
        bool: True si une combinaison valide est trouvée, False sinon.
    """
    if not num_line and flag == 1:
        # Si la liste est vide et une paire a été trouvée (flag == 1),
        # on ajoute le numéro courant à la liste des résultats
        result_lis.append(check_num)
        return True
    for num in num_line:
        # Tente d'extraire un triple identique au début de num_line
        if three(num, num_line): 
            return True
        # Tente d'extraire une paire identique au début de num_line
        if two(num, num_line): 
            return True
        # Tente d'extraire une suite de trois nombres consécutifs
        if straight(num, num_line): 
            return True
    return False

def three(num, num_line):
    """
    Vérifie si les trois premiers éléments de num_line sont égaux à num.
    Si oui, tente de résoudre récursivement le reste de la liste.

    Args:
        num (int): Nombre à vérifier.
        num_line (list of int): Liste des nombres.
        
    Returns:
        bool: True si une combinaison valide est trouvée en enlevant ce triple, False sinon.
    """
    count = 0
    for check in num_line[:3]:
        if check == num:
            count += 1
    else:
        if count == 3:
            # Supprime ce triple et continue la recherche sur le reste
            if pokakito(num_line[3:]): 
                return True
    return False

def two(num, num_line):
    """
    Vérifie si les deux premiers éléments de num_line sont égaux à num.
    Si oui, augmente le flag indiquant qu'une paire a été trouvée, puis
    tente de résoudre récursivement le reste de la liste avec ce flag.
    Si la recherche échoue, restaure le flag.

    Args:
        num (int): Nombre à vérifier.
        num_line (list of int): Liste des nombres.
        
    Returns:
        bool: True si une combinaison valide est trouvée en enlevant cette paire, False sinon.
    """
    global flag
    count = 0
    for check in num_line[:2]:
        if check == num:
            count += 1
    else:
        if count == 2:
            flag += 1  # Marque la présence d'une paire
            if pokakito(num_line[2:]): 
                return True
            flag -= 1  # Restaure flag si échec de la recherche
    return False

def straight(num, num_line):
    """
    Tente de trouver une séquence consécutive de trois nombres commençant par num.
    Si une séquence valide est trouvée, enlève ces nombres et continue la recherche sur le reste.

    Args:
        num (int): Le nombre de départ pour la séquence consécutive.
        num_line (list of int): Liste des nombres.
        
    Returns:
        bool: True si une combinaison valide est trouvée en enlevant cette séquence, False sinon.
    """
    num_lis = [num, num + 1, num + 2]
    # Recherche d'une suite de trois valeurs consécutives présentes dans num_line
    for i in range(3):
        for check in num_lis:
            if check < 0 or (check not in num_line):
                # La séquence n'est pas valide, essaye la séquence précédente décalée de 1
                for j in range(3):
                    num_lis[j] -= 1
                break
        else:
            # On a trouvé une séquence valide, on retire les éléments correspondants de num_line
            temp_line = num_line[:]
            for n in num_lis:
                index = 0
                while index < len(temp_line):
                    if temp_line[index] == n:
                        del temp_line[index]
                        break
                    index += 1
                else:
                    # Si un élément de la séquence n'est pas trouvé correctement, la séquence est invalide
                    break
            else:
                # Séquence retirée avec succès, on continue la recherche récursive
                if pokakito(temp_line): 
                    return True
    return False

# Initialisation des variables globales pour la gestion de l'état
flag = 0            # Indique si une paire a été trouvée (flag == 1)
result_lis = []     # Liste des numéros valides trouvés
check_num = 0       # Numéro actuel testé

for input_line in sys.stdin:
    # Pour chaque ligne d'entrée, on teste les nombres de 1 à 9 comme numéro check_num
    for i in range(9):
        check_num = i + 1
        input_line = input_line.rstrip()
        # Ajoute check_num à la chaîne puis trie les caractères
        line = sorted(input_line + str(check_num))
        line = ''.join(line)
        # Trouve l'index de check_num dans la chaîne triée
        index = line.find(str(check_num))
        # Si on a cinq occurrences consécutives de check_num, on ignore cette configuration
        if line[index:index + 5] == str(check_num) * 5:
            continue
        # Convertit la chaîne en liste d'entiers et tente de trouver des combinaisons valides
        pokakito([int(char) for char in line])
        # Trie et prépare les résultats sous forme de chaîne de caractères
        result = sorted([str(num) for num in result_lis])
        flag = 0  # Reset du flag après chaque tentative
    else:
        # Après avoir testé tous les numéros, affiche les résultats ou 0 si vide
        if result_lis:
            print(' '.join(result))
        else:
            print(0)
    # Réinitialisation des variables globales avant la prochaine ligne d'entrée
    flag = 0
    result_lis = []
    check_num = 0