def get_min_common_char_string(n, string_list):
    """
    Calcule et retourne une chaîne composée des caractères apparaissant dans toutes les chaînes
    de l'entrée, chaque caractère étant répété autant de fois qu'il apparaît dans toutes les chaînes
    (i.e., l'occurrence minimale pour chaque lettre de l'alphabet).

    Args:
        n (int): Le nombre de chaînes dans la liste.
        string_list (list of str): Liste contenant 'n' chaînes.

    Returns:
        str: Chaîne constituée des caractères communs répétés selon leur occurrence minimale.
    """
    # Initialiser une liste qui contiendra, pour chaque lettre, le minimum d'occurrences trouvées dans les chaînes.
    min_counts = [100] * 26  # 26 lettres de l’alphabet, initialement à un nombre très élevé.

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Parcourir toutes les chaînes d'entrée pour détecter le minimum de chaque caractère.
    for s in string_list:
        for i in range(26):
            letter = alphabet[i]
            letter_count = s.count(letter)
            # Mettre à jour le minimum pour ce caractère si une valeur plus faible est trouvée.
            if min_counts[i] > letter_count:
                min_counts[i] = letter_count

    # Construire la réponse finale en répétant chaque caractère selon son minimum trouvé.
    result = ""
    for i in range(26):
        char = chr(97 + i)  # Convertir l’indice en caractère (a=97 en ASCII)
        result += char * min_counts[i]

    return result

def main():
    """
    Fonction principale. Lit les entrées utilisateur, appelle la fonction de calcul
    et affiche le résultat.
    """
    # Lecture du nombre de chaînes à traiter.
    n = int(input())
    # Lecture des chaînes à traiter, une par ligne.
    S = [input() for _ in range(n)]
    # Appel de la fonction de calcul et affichage du résultat.
    print(get_min_common_char_string(n, S))

if __name__ == "__main__":
    main()