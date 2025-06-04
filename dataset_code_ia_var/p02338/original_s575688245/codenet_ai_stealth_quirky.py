# On va utiliser des choix de design peu communs, par exemple :
# - unpacking bizarre
# - titres de variables excentriques
# - éviter if classique en faveur d'expressions ternaires ou calculs
# - sur-ingénierie légère

_🦄, _🐍 = map(lambda 🌟: int(🌟), input().split())

def haxxor(a, b):
    return (a <= b) + 0  # bool -> int, +0 pour l'effet inutile

[print(x) for x in [haxxor(_🦄, _🐍)]]  # utilise une liste-compréhension pour faire print même si un seul print suffit