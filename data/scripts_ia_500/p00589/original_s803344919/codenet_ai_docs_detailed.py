# AOJ 1003: Extraordinary Girl II
# Python3 2018.7.4 bal4u

# Table associant chaque chiffre à un groupe de caractères correspondant aux touches d'un ancien téléphone
tbl = [
    "",             # 0 : vide (utile pour décalage d'index)
    "',.!?",        # 1 : signes de ponctuation
    "abcABC",       # 2 : lettres associées à la touche '2'
    "defDEF",       # 3 : lettres associées à la touche '3'
    "ghiGHI",       # 4 : lettres associées à la touche '4'
    "jklJKL",       # 5 : lettres associées à la touche '5'
    "mnoMNO",       # 6 : lettres associées à la touche '6'
    "pqrsPQRS",     # 7 : lettres associées à la touche '7'
    "tuvTUV",       # 8 : lettres associées à la touche '8'
    "wxyzWXYZ"      # 9 : lettres associées à la touche '9'
]

def decode_sequence(sequence: str) -> str:
    """
    Décode une séquence de chiffres en utilisant la table de correspondance des touches d'un téléphone.
    
    Le principe est que chaque groupe consécutif de chiffres identiques représente une seule lettre ou un espace.
    Le chiffre '0' représente un espace, dont la longueur dépend du nombre de zéros consécutifs.
    Pour les autres chiffres, la lettre choisie est déterminée par le nombre de répétitions modulo la taille
    du groupe associé dans la table tbl.

    Args:
        sequence (str): La chaîne de caractères composée de chiffres à décoder.

    Returns:
        str: La chaîne décodée en texte lisible.
    """
    ans = ''    # Résultat décodé
    i = 0       # Index de parcours de la chaîne d'entrée

    while i < len(sequence):
        c = sequence[i]           # caractère actuel (chiffre)
        d = int(c)               # convertir le caractère en entier (touche)
        i += 1                   # avancer l'index pour analyser les répétitions
        w = 0                    # compteur de répétitions du même chiffre

        # Compter combien de fois le même chiffre est répété consécutivement
        while i < len(sequence) and sequence[i] == c:
            w += 1
            i += 1

        if d == 0:
            # Pour le chiffre 0, ajouter des espaces correspondant au nombre de répétitions + 1
            # car la première occurrence correspond aussi à un '0'
            ans += ' ' * (w + 1)
        else:
            # Pour les autres chiffres, sélectionner un caractère dans tbl[d]
            # la position est donnée par le nombre total de répétitions modulo la longueur de tbl[d]
            # nombre total de répétitions = w + 1 (car w compte les répétitions après la première)
            index = (w) % len(tbl[d])
            ans += tbl[d][index]

    return ans


def main():
    """
    Lecture continue des lignes d'entrée jusqu'à la fin (EOF).
    Chaque ligne est décodée grâce à la fonction decode_sequence et le résultat est affiché.
    """
    while True:
        try:
            s = input().strip()
            if not s:
                # Si la ligne est vide, continuer à lire la suivante
                continue
        except EOFError:
            # Fin de l'entrée
            break

        # Décodage de la ligne lue
        result = decode_sequence(s)
        # Affichage du résultat décodé
        print(result)


if __name__ == '__main__':
    main()