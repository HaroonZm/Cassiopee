def main():
    # Style procédural pour la saisie de l'entrée
    N = int(input())
    ab = []
    for _ in range(N):
        ab.append(list(map(int, input().split())))

    # Paradigme fonctionnel pour trier
    ab = sorted(ab, key=lambda x: x[0])

    # Style compact, façon script
    result = None
    try:
        last = ab.__getitem__(-1)
        result = last[0] + last[1]
    except Exception as e:
        result = "Erreur"

    # Style orienté objet pour l'affichage (peu habituel mais original ici)
    class Printer:
        def show(self, value): print(value)
    Printer().show(result)

main()