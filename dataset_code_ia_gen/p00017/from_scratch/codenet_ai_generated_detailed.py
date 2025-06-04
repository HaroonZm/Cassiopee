import sys

def caesar_decrypt(text, shift):
    """
    Déchiffre le texte chiffré avec un décalage Caesar donné.
    Seuls les caractères alphabétiques minuscules sont décalés.
    Les autres caractères (espace, point) sont laissés tels quels.
    """
    decrypted = []
    for ch in text:
        if 'a' <= ch <= 'z':
            # Décalage circulaire dans l'alphabet minuscules
            new_char = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            decrypted.append(new_char)
        else:
            decrypted.append(ch)
    return ''.join(decrypted)

def contains_keyword(text):
    """
    Vérifie si le texte contient au moins un des mots indiqués:
    'the', 'this' ou 'that'.
    """
    # Mettre en œuvre la recherche en utilisant des espaces pour limiter
    # les mots partiels, ou simplement une recherche brute ici
    # car les mots sont courts et distincts.
    keywords = ['the', 'this', 'that']
    # On peut rechercher parmi les mots découpés (split) ou string
    # pour être sûr d'éviter des sous-chaînes non voulues.
    words = text.split()
    for kw in keywords:
        if kw in words:
            return True
    return False

def main():
    # Lire toutes les lignes jusqu'à EOF
    lines = sys.stdin.read().splitlines()
    for line in lines:
        # Pour chaque ligne, essayer tous les décalages possibles (0..25)
        for shift in range(26):
            decrypted = caesar_decrypt(line, shift)
            if contains_keyword(decrypted):
                print(decrypted)
                break

if __name__ == "__main__":
    main()