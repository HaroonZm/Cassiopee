import sys
from functools import reduce

class Enigma:
    def __init__(self):
        self.labyrinth = list(reduce(lambda acc, x: acc+[x], (line for line in sys.stdin.read().splitlines()[:9]), []))

    def cryptic_move(self, human):
        h = lambda t: (t[1]*2 + (t[2] in (1,2))) if t[2] % 2 == 1 else (t[1]*2 - (t[2] in (0,3)))
        i,j,d = human
        murs = self.labyrinth
        mod = [(-1,0),(0,1),(1,0),(0,-1)]
        def wall_at(r,c):
            return 0 <= r < 9 and 0 <= c < 4 and murs[r][c] == '1'
        guess = [(d+3)%4, d, (d+1)%4]
        check_coords = {
            0: [(h(human), i, True), (i, h(human)), (h(human)+2, i, False)],
            1: [(i, h(human)), (h(human)+2, i), (i-1, h(human))],
            2: [(h(human)+2, i), (i-1, h(human)), (h(human), i, True)],
            3: [(i-1, h(human)), (h(human), i, True), (i, h(human))]
        }
        # overcomplicated functional search with multiple map, all, any
        results = list(map(lambda dir_idx:
                           (dir_idx, 
                            (lambda coords: wall_at(coords[0], coords[1]) if len(coords) == 2 else wall_at(coords[0], coords[1]))(check_coords[d][check_coords[d].index(check_coords[d][dir_idx]) if dir_idx < len(check_coords[d]) else 0])
                           ), range(3)))
        filtered = list(filter(lambda x: x[1], results))
        if filtered:
            return guess[filtered[0][0]]
        return 2

def main():
    enigma = Enigma()
    solve = "R"
    human = (1,0,0)
    while human[0] != 0 or human[1] != 0:
        m = enigma.cryptic_move(human)
        direction = (human[2] + m) % 4
        i,j,d = human
        if direction == 0:
            human = (i + 1, j, direction)
            solve += "R"
        elif direction == 1:
            human = (i, j + 1, direction)
            solve += "D"
        elif direction == 2:
            human = (i - 1, j, direction)
            solve += "L"
        else:
            human = (i, j - 1, direction)
            solve += "U"
    print(solve)

if __name__ == "__main__":
    main()