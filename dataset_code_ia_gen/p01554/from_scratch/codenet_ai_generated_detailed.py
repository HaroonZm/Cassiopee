# Solution complète en Python avec commentaires détaillés

# L'idée est de gérer un système de verrouillage électronique qui utilise des IDs enregistrés.
# Initialement, la porte est verrouillée (施錠された状態).
# Chaque fois qu'une carte est utilisée, on vérifie si l'ID est connu :
# - Si oui, on bascule l'état (ouvrir si fermé, fermer si ouvert) et on affiche le message correspondant.
# - Si non, on affiche "Unknown ID" sans changer l'état.

def main():
    import sys

    input = sys.stdin.readline  # Pour une lecture plus rapide

    # Lecture du nombre d'IDs enregistrés
    N = int(input())
    registered_ids = set()

    # Lecture des IDs
    for _ in range(N):
        uid = input().strip()
        registered_ids.add(uid)

    # Lecture du nombre d'utilisations de cartes
    M = int(input())
    # État initial de la porte : True = fermé (施錠), False = ouvert (開錠)
    locked = True

    # Pour chaque tentative avec une carte donnée
    for _ in range(M):
        tid = input().strip()
        if tid in registered_ids:
            # ID connu, on bascule l'état
            if locked:
                # Si verrouillé, on ouvre
                locked = False
                print("Opened by " + tid)
            else:
                # Si ouvert, on ferme
                locked = True
                print("Closed by " + tid)
        else:
            # ID inconnu, on affiche le message sans changer l'état
            print("Unknown " + tid)

if __name__ == "__main__":
    main()