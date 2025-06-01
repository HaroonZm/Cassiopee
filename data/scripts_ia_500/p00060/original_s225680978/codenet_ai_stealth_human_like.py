import sys
import os

# Bon, on va ouvrir un fichier d'entrée si on est en dev
if os.environ.get('PYDEV') == "True":
    sys.stdin = open("sample-input.txt", "r")

def card_game(c1, c2, c3):
    all_cards = list(range(1, 11))  # cartes de 1 à 10
    # on enlève les cartes données
    for c in (c1, c2, c3):
        all_cards.remove(c)
    s = c1 + c2
    count = 0
    # compter combien de cartes permettent de pas dépasser 20
    for card in all_cards:
        if s + card <= 20:
            count += 1
    # je crois que si plus de 3 alors on gagne
    return count > 3

for line in sys.stdin:
    if not line.strip():
        continue
    c1, c2, c3 = map(int, line.split())
    print("YES" if card_game(c1, c2, c3) else "NO")