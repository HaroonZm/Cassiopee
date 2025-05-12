from __future__ import print_function
import copy
import sys

class Board(object):
    size = 8
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    dx = [1, 1, 0, -1, -1, -1, 0, 1]

    def __init__(self):
        self.board = [[0] * Board.size for _ in xrange(Board.size)]

    def __deepcopy__(self, memo):
        ret = Board()
        ret.board = copy.deepcopy(self.board, memo)
        return ret

    def _check_range(self, y, x):
        assert 0 <= y < Board.size and 0 <= x < Board.size

    def _check_color(self, color):
        assert color == 'o' or color == 'x'

    def _putone(self, color, y, x):
        self._check_color(color)
        self._check_range(y, x)

        if color == 'o':
            self.board[y][x] = 1
        if color == 'x':
            self.board[y][x] = -1

    def _getone(self, y, x):
        self._check_range(y, x)
        
        if self.board[y][x] == 1:
            return 'o'
        if self.board[y][x] == -1:
            return 'x'
        return '.'

    def view(self):
        return '\n'.join(''.join(self._getone(y, x) for x in xrange(Board.size)) for y in xrange(Board.size))

    def put(self, color, y, x):
        self._check_color(color)
        self._check_range(y, x)
        self._putone(color, y, x)

        def find(y, x, d):
            # print("y = ", y, ", x = ", x, ", d = ", d)
            if y < 0 or y >= Board.size or x < 0 or x >= Board.size:
                return False
            if self._getone(y, x) == '.':
                return False
            if self._getone(y, x) == color:
                return True
            if find(y + Board.dy[d], x + Board.dx[d], d):
                self._putone(color, y, x)
                return True
            return False

        for d in xrange(Board.size):
            # print('d = ', d)
            find(y + Board.dy[d], x + Board.dx[d], d)
            # print(self.view())

def main():
    board = Board()
    for i in xrange(8):
        l = raw_input()
        for j in xrange(8):
            if l[j] != '.':
                board._putone(l[j], i, j)
    color = 'o'
    passprev = False
    while True:
        cy = -1
        cx = -1
        get = 1
        o = sum(1 for c in board.view() if c == 'o')
        x = sum(1 for c in board.view() if c == 'x')
        if color == 'o':
            for i in xrange(8):
                for j in xrange(8):
                    if board._getone(i, j) == '.':
                        board2 = copy.deepcopy(board)
                        board2.put(color, i, j)
                        o2 = sum(1 for c in board2.view() if c == 'o')
                        if o2 - o > get:
                            get = o2 - o
                            cy = i
                            cx = j
        else:
            for _i in xrange(8):
                for _j in xrange(8):
                    i = 7 - _i
                    j = 7 - _j
                    if board._getone(i, j) == '.':
                        board2 = copy.deepcopy(board)
                        board2.put(color, i, j)
                        x2 = sum(1 for c in board2.view() if c == 'x')
                        if x2 - x > get:
                            get = x2 - x
                            cy = i
                            cx = j

        if cy == -1 and cx == -1:
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

if __name__ == '__main__':
    main()