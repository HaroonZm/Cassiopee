# Définition de la correspondance des boutons aux caractères selon l'énoncé
BUTTON_MAPPING = {
    '1': ['.', ',', '!', '?', ' '],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

def decode_message(button_sequence: str) -> str:
    """
    Décode une chaîne de chiffres représentant la séquence des boutons pressés
    et retourne le message texte correspondant en utilisant le mapping fourni.
    L'appui sur '0' correspond à la confirmation du caractère courant.
    """
    result = []  # Liste pour stocker les caractères décodés
    current_button = None  # Bouton actuellement pressé
    press_count = 0  # Nombre d'appuis consécutifs sur le même bouton (non '0')

    # Parcours de chaque chiffre dans la séquence
    for ch in button_sequence:
        if ch == '0':
            # Si on appuie sur '0', on confirme la lettre en cours
            if current_button is not None and press_count > 0:
                # On récupère la liste des caractères possibles de ce bouton
                chars = BUTTON_MAPPING[current_button]
                # Calcul de l'index du caractère choisi avec boucle sur le nombre d'appuis
                index = (press_count - 1) % len(chars)
                # Ajout du caractère correspondant au résultat
                result.append(chars[index])
            # Réinitialiser l'état pour commencer une nouvelle lettre
            current_button = None
            press_count = 0
        else:
            # Si c'est un bouton différent du précédent, on initialise un nouveau comptage
            if ch == current_button:
                # Même bouton, incrémentation du comptage
                press_count += 1
            else:
                # Différent bouton, démarrage d'un nouveau comptage
                current_button = ch
                press_count = 1
    # On ne traite pas de caractère non confirmé à la fin car l'énoncé impose confirmation par '0'
    return ''.join(result)

def main():
    import sys
    input = sys.stdin.readline

    # Lecture du nombre de cas de test
    T = int(input())

    # Traitement de chaque test
    for _ in range(T):
        sequence = input().strip()
        decoded = decode_message(sequence)
        print(decoded)

if __name__ == "__main__":
    main()