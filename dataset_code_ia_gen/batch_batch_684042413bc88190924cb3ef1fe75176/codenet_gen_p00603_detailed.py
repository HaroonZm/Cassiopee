import sys

def riffle_shuffle(deck, c):
    """
    Effectue une opération de riffle shuffle sur un deck donné avec un paramètre c.
    deck : liste représentant le deck (de bas en haut, index 0 = bas)
    c : nombre de cartes à tirer par groupe depuis le bas de chaque moitié
    Retourne le nouveau deck après la shuffle.
    """
    n = len(deck)
    # Calcul de la taille des deux demi-paquets A et B
    half = (n + 1) // 2  # deck A a un de plus si n est impair

    deck_A = deck[-half:]  # Top half (deck A)
    deck_B = deck[:-half]  # Bottom half (deck B)

    # On tire les cartes depuis le bas des paquets A et B
    # ici, le bas est l'index 0 (car deck est bottom-to-top)
    deck_A = deck_A[::-1]  # inverser pour avoir bottom à l'index 0
    deck_B = deck_B[::-1]

    deck_C = []

    # Répéter jusqu'à ce que A et B soient vides
    while deck_A or deck_B:
        # Prendre c cartes du bas de A
        take_A = min(c, len(deck_A))
        for _ in range(take_A):
            deck_C.append(deck_A.pop(0))
        # Prendre c cartes du bas de B
        take_B = min(c, len(deck_B))
        for _ in range(take_B):
            deck_C.append(deck_B.pop(0))

    # deck_C contient les cartes dans l'ordre du bas vers le haut
    # On doit remettre deck_C en bottom-to-top:
    deck_C = deck_C[::-1]

    return deck_C

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while idx < len(input_lines):
        # Lire n et r
        if not input_lines[idx].strip():
            idx += 1
            continue
        n_r = input_lines[idx].strip().split()
        if len(n_r) < 2:
            # Peu probable, mais passer à la ligne suivante
            idx += 1
            continue
        n, r = map(int, n_r)
        idx += 1
        c_values = []
        while len(c_values) < r:
            # Lire les valeurs de c, potentiellement plusieurs sur la même ligne
            c_values += list(map(int, input_lines[idx].strip().split()))
            idx += 1
        # Initialiser le deck: cartes numérotées de 0 (bas) à n-1 (top)
        deck = list(range(n))
        # Pour chaque c, effectuer une opération de riffle shuffle
        for c in c_values:
            deck = riffle_shuffle(deck, c)
        # Afficher la carte au sommet du deck (= dernière carte de la liste)
        print(deck[-1])

if __name__ == "__main__":
    main()