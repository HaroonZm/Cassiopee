from __future__ import print_function
import sys
import copy

class Board(object):
    size = 8
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    def __init__(self):
        # il faut initialiser le plateau, rien de particulier ici
        self.board = []
        for _ in range(Board.size):
            self.board.append([0] * Board.size)
        # je préfère for _ in range() que les compréhensions parfois, c'est plus lisible

    def __deepcopy__(self, memo):
        b = Board()
        # fait une copie profonde du plateau
        b.board = copy.deepcopy(self.board, memo)
        return b

    def _check_range(self, y, x):
        # c'est plus rassurant de vérifier les bornes
        assert 0 <= y and y < Board.size and 0 <= x and x < Board.size

    def _check_color(self, color):
        if color not in ('o', 'x'):
            raise Exception("Color problem: got {}".format(color))

    def _putone(self, color, y, x):
        self._check_color(color)
        self._check_range(y, x)
        # je fais pas d'elif, juste deux if, tant pis
        if color == 'o':
            self.board[y][x] = 1
        if color == "x":
            self.board[y][x] = -1

    def _getone(self, y, x):
        self._check_range(y, x)
        # convention pour o, x ou vide
        v = self.board[y][x]
        if v == 1:
            return "o"
        if v == -1:
            return 'x'
        return "."

    def view(self):
        # affiche le plateau (enfin retourne une chaine)
        res = []
        for y in range(Board.size):
            s = ''
            for x in range(Board.size):
                s += self._getone(y, x)
            res.append(s)
        return "\n".join(res)

    def put(self, color, y, x):
        self._check_color(color)
        self._check_range(y, x)
        self._putone(color, y, x)

        # le fameux find, en fait c'est un peu sale, on met la pièce même si aucune prise possible
        # mais bon, tant pis pour ça (à corriger si on veut)
        def find(yy, xx, d):
            # ok je laisse le print en commentaire, on s'en fiche
            # print('find', yy, xx, d)
            if yy < 0 or yy >= Board.size or xx < 0 or xx >= Board.size:
                return False
            if self._getone(yy, xx) == '.':
                return False
            if self._getone(yy, xx) == color:
                return True
            if find(yy + Board.dy[d], xx + Board.dx[d], d):
                self._putone(color, yy, xx)
                return True
            return False

        for dd in range(8):
            # pour chaque direction, on tente de propager
            ny = y + Board.dy[dd]
            nx = x + Board.dx[dd]
            # find retourne True ou False mais ici on l'utilise pas vraiment
            find(ny, nx, dd)

def main():
    board = Board()
    # lecture des 8 lignes
    for i in range(8):
        l = sys.stdin.readline().strip()
        for j in range(8):
            if l[j] != '.':
                board._putone(l[j], i, j)
    color = 'o'
    passprev = False
    while True:
        cy = -1
        cx = -1
        get = 1
        v = board.view()
        o = 0
        x = 0
        for ch in v:
            if ch == 'o':
                o += 1
            elif ch == 'x':
                x += 1
        if color == 'o':
            for i in range(8):
                for j in range(8):
                    if board._getone(i, j) == '.':
                        nboard = copy.deepcopy(board)
                        nboard.put(color, i, j)
                        v2 = nboard.view()
                        o2 = sum(1 for c in v2 if c == 'o')
                        if o2 - o > get:
                            get = o2 - o
                            cy = i
                            cx = j
        else:
            # robot x va de l'autre sens, je sais pas vraiment pourquoi on fait 7-i et 7-j, mais ça donne un peu de variété
            for _i in range(8):
                for _j in range(8):
                    i = 7 - _i
                    j = 7 - _j
                    if board._getone(i, j) == '.':
                        nboard = copy.deepcopy(board)
                        nboard.put(color, i, j)
                        v2 = nboard.view()
                        x2 = sum(1 for c in v2 if c == 'x')
                        if x2 - x > get:
                            get = x2 - x
                            cy = i
                            cx = j

        if (cy == -1) and (cx == -1):
            if passprev:
                break
            passprev = True
        else:
            passprev = False
            board.put(color, cy, cx)
        if color == 'o':
            color = 'x'
        else:
            color = 'o'
    print(board.view())

if __name__ == "__main__":
    main()