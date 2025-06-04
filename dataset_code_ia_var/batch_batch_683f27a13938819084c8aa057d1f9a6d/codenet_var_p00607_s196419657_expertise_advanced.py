from typing import List

class Editer:
    __slots__ = ('row', 'col', 'text', 'buffer')

    def __init__(self, text: List[str]):
        self.row: int = 0
        self.col: int = 0
        self.text: List[List[str]] = [list(t) + ['\n'] for t in text]
        self.buffer: List[str] = []

    @property
    def row_head(self) -> int:
        return 0

    @property
    def row_tail(self) -> int:
        return len(self.text) - 1

    @property
    def col_head(self) -> int:
        return 0

    @property
    def col_tail(self) -> int:
        return len(self.text[self.row]) - 1

    def __repr__(self):
        return ''.join(map(''.join, self.text))

    def command_a(self):
        self.col = self.col_head

    def command_e(self):
        self.col = self.col_tail

    def command_p(self):
        if self.row > self.row_head:
            self.row -= 1
        self.col = self.col_head

    def command_n(self):
        if self.row < self.row_tail:
            self.row += 1
        self.col = self.col_head

    def command_b(self):
        if self.col > self.col_head:
            self.col -= 1
        elif self.row > self.row_head:
            self.row -= 1
            self.col = len(self.text[self.row]) - 1

    def command_f(self):
        if self.col < self.col_tail:
            self.col += 1
        elif self.row < self.row_tail:
            self.row += 1
            self.col = self.col_head

    def command_d(self):
        if self.col < self.col_tail:
            self.text[self.row].pop(self.col)
        elif self.row < self.row_tail:
            self.text[self.row].pop()
            self.text[self.row] += self.text.pop(self.row + 1)

    def command_k(self):
        if self.col < self.col_tail:
            self.buffer = self.text[self.row][self.col:-1]
            self.text[self.row] = self.text[self.row][:self.col] + ['\n']
            self.col = self.col_tail
        elif self.row < self.row_tail:
            self.buffer = ['\n']
            self.text[self.row].pop()
            self.text[self.row] += self.text.pop(self.row + 1)

    def command_y(self):
        if self.buffer != ['\n']:
            self.text[self.row][self.col:self.col] = self.buffer
            self.col += len(self.buffer)
        else:
            self.text.insert(self.row + 1, self.text[self.row][self.col:])
            self.text[self.row] = self.text[self.row][:self.col] + ['\n']
            self.row += 1
            self.col = self.col_head

def main():
    import sys
    from functools import partial

    text: List[str] = list(iter(input, 'END_OF_TEXT'))

    editer = Editer(text)

    commands: dict[str, callable] = {
        'a': editer.command_a,
        'e': editer.command_e,
        'p': editer.command_p,
        'n': editer.command_n,
        'f': editer.command_f,
        'b': editer.command_b,
        'd': editer.command_d,
        'k': editer.command_k,
        'y': editer.command_y
    }

    for command in iter(input, '-'):
        func = commands.get(command)
        if func:
            func()

    print(editer, end='')

if __name__ == '__main__':
    main()