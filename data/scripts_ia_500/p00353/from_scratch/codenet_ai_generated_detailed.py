# Lecture des entrées : m (mon argent), f (argent d'Alice), b (prix du livre)
m, f, b = map(int, input().split())

# On calcule combien d'argent il nous manque
manquant = b - m

# Si je possède déjà assez d'argent, il n'y a rien à emprunter
if manquant <= 0:
    print(0)
# Sinon, si l'argent d'Alice suffit à couvrir le manque, on emprunte seulement ce qu'il manque
elif manquant <= f:
    print(manquant)
# Sinon, même avec l'aide d'Alice, on ne peut pas acheter le livre
else:
    print("NA")