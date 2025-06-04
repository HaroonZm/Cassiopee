# Modélisation complète du dé avec simulation des rotations pour le problème "Die Game"

# Approche :
# - Le dé a 6 faces avec les numéros de 1 à 6.
# - Les faces opposées somment toujours à 7.
# - Initialement : top=1, north=2, west=3
# - A partir de ces 3 faces, on peut déduire les autres (bottom, south, east).
# - On représente le dé par un dictionnaire face -> valeur.
# - La position des faces est : top, bottom, north, south, west, east
# - Pour chaque commande (north, east, south, west), on effectue une rotation qui remet à jour la position des valeurs sur les faces.
# - A la fin de la séquence, on renvoie la valeur visible sur la face top.

def main():
    import sys

    # Classe représentant le dé et ses rotations
    class Die:
        def __init__(self):
            # Initialisation selon l'énoncé:
            # top=1, north=2, west=3
            # bottom = 7 - top = 6
            # south = 7 - north = 5
            # east = 7 - west = 4
            self.faces = {
                'top': 1,
                'bottom': 6,
                'north': 2,
                'south': 5,
                'west': 3,
                'east': 4
            }

        # Rotation vers le nord : le dé roule sur le bord nord
        # changement des faces : top->north, north->bottom, bottom->south, south->top
        def roll_north(self):
            f = self.faces
            self.faces['top'], self.faces['north'], self.faces['bottom'], self.faces['south'] = \
                f['south'], f['top'], f['north'], f['bottom']

        # Rotation vers le sud : inverse de roll_north
        def roll_south(self):
            f = self.faces
            self.faces['top'], self.faces['north'], self.faces['bottom'], self.faces['south'] = \
                f['north'], f['bottom'], f['south'], f['top']

        # Rotation vers l'est
        # Le dé roule sur son bord est
        # top->west, west->bottom, bottom->east, east->top
        def roll_east(self):
            f = self.faces
            self.faces['top'], self.faces['west'], self.faces['bottom'], self.faces['east'] = \
                f['west'], f['bottom'], f['east'], f['top']

        # Rotation vers l'ouest : inverse de roll_east
        def roll_west(self):
            f = self.faces
            self.faces['top'], self.faces['west'], self.faces['bottom'], self.faces['east'] = \
                f['east'], f['top'], f['west'], f['bottom']

    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n = int(input_lines[idx])
        idx += 1
        if n == 0:
            # Fin de l'entrée
            break
        die = Die()
        for _ in range(n):
            command = input_lines[idx]
            idx += 1
            if command == 'north':
                die.roll_north()
            elif command == 'south':
                die.roll_south()
            elif command == 'east':
                die.roll_east()
            elif command == 'west':
                die.roll_west()
            else:
                # Commande inconnue, on ignore (ou on pourrait lever une erreur)
                pass
        print(die.faces['top'])

if __name__ == '__main__':
    main()