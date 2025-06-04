def t9_decode(test_cases):
    """
    Décode une séquence de touches de téléphones en texte selon la correspondance du clavier T9.

    Args:
        test_cases (list of str): Liste de chaînes de caractères, chaque chaîne représentant une séquence de chiffres
                                  séparée par des '0'. Chaque séquence simule plusieurs pressions sur une même touche.

    Returns:
        list of str: Liste des chaînes décodées pour chaque ligne entrée.
    """
    # Liste contenant les caractères associés à chaque touche du clavier, suivant le modèle T9
    keylist = [
       [],  # Touche 0 (non utilisée pour les lettres)
       ['.', ',', '!', '?', ' '],  # Touche 1
       ['a', 'b', 'c'],             # Touche 2
       ['d', 'e', 'f'],             # Touche 3
       ['g', 'h', 'i'],             # Touche 4
       ['j', 'k', 'l'],             # Touche 5
       ['m', 'n', 'o'],             # Touche 6
       ['p', 'q', 'r', 's'],        # Touche 7
       ['t', 'u', 'v'],             # Touche 8
       ['w', 'x', 'y', 'z']         # Touche 9
    ]
    results = []

    # Itération sur chaque ligne de test
    for line in test_cases:
        output = ''  # Chaîne décodée pour la ligne courante
        # Découpe de la ligne en groupes consécutifs de la même touche, séparés par '0'
        for item in line.split('0'):
            if item == '':
                # Sauter les éléments vides (peuvent être générés par plusieurs '0' consécutifs, début ou fin)
                continue
            key = int(item[0])  # La touche utilisée pour ce groupe
            presses = len(item)  # Nombre d'appuis effectués sur la touche
            chars = keylist[key]  # Liste des caractères pour cette touche

            # Calcul de l'indice du caractère souhaité, tenant compte du nombre d'appuis (cycle sur la liste)
            idx = (presses % len(chars)) - 1
            # Ajout du caractère sélectionné à la sortie
            output += chars[idx]
        results.append(output)  # Ajoute le résultat de la ligne courante à la liste des résultats
    return results

def main():
    """
    Fonction principale pour lire les entrées de l'utilisateur, décoder les séquences T9
    et les afficher à l'écran.
    """
    # Lecture du nombre de cas de test à traiter
    n = int(input())
    test_cases = []

    # Collecte des cas de test
    for _ in range(n):
        # Lecture et stockage de chaque séquence de touches
        test_cases.append(input())

    # Décodage de chaque séquence de touches
    results = t9_decode(test_cases)

    # Affichage des résultats décodés
    for res in results:
        print(res)

# Exécution du programme principal si ce fichier est exécuté comme script
if __name__ == "__main__":
    main()