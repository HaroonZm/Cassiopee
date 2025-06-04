def get_letter_from_code(code, moji):
    """
    Convertit un code numérique représentant la saisie sur un clavier de type téléphone en une lettre ou un caractère.

    Paramètres :
        code (str): La séquence de chiffres correspondant à une touche pressée plusieurs fois (ex: '222').
        moji (list): Une liste de listes, où chaque indice correspond à une touche et la liste contient les caractères.

    Retourne :
        str: Le caractère correspondant à la séquence de touches.
    """
    # Convertit la première position du code en numéro de touche (entier)
    key_number = int(code[0])
    # Calcule l'index basé sur la longueur de la séquence (modulo la taille du mapping pour cette touche)
    index = len(code) % len(moji[key_number])
    # Retourne le caractère approprié depuis le mapping
    return moji[key_number][index]

def process_input_line(line, moji):
    """
    Traite une ligne d'entrée du texte, la convertissant depuis les codes numériques du clavier vers du texte.

    Paramètres :
        line (str): La ligne d'entrée, chaque séquence est séparée par un espace.
        moji (list): La structure de mapping des touches vers caractères.

    Retourne :
        str: La ligne convertie en texte.
    """
    # Remplace tous les '0' par des espaces pour séparer les mots, puis split sur les espaces
    codes = list(line.strip().replace('0',' ').split())
    result = []
    # Pour chaque code numérique, on récupère le caractère associé
    for code in codes:
        result.append(get_letter_from_code(code, moji))
    # Retourne la chaîne finale reconstruite
    return ''.join(result)

def main():
    """
    Point d'entrée principal du programme. Lit le nombre de lignes à traiter,
    puis pour chaque ligne, transforme les entrées numériques en texte grâce à un mapping type clavier de téléphone.
    """
    # Lecture du nombre de lignes à traiter
    n = int(input())
    # Mapping des touches (0-9) vers les caractères associés à chaque touche selon la logique présentée
    moji = [
        [],                         # 0 : pas utilisé directement
        [' ', '.', ',', '!', '?'],  # 1 : espace et ponctuation
        ['c', 'a', 'b'],            # 2
        ['f', 'd', 'e'],            # 3
        ['i', 'g', 'h'],            # 4
        ['l', 'j', 'k'],            # 5
        ['o', 'm', 'n'],            # 6
        ['s', 'p', 'q', 'r'],       # 7
        ['v', 't', 'u'],            # 8
        ['z', 'w', 'x', 'y']        # 9
    ]
    # Pour chaque ligne d'entrée, conversion puis affichage du résultat
    for _ in range(n):
        input_line = input()
        output_line = process_input_line(input_line, moji)
        print(output_line)

if __name__ == '__main__':
    main()