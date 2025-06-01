class Editer:
    def __init__(self, text):
        self.row = 0
        self.col = 0
        self.text = [list(line) + ['\n'] for line in text]
        self.buffer = []

    @property
    def row_head(self):
        return 0

    @property
    def row_tail(self):
        return len(self.text) - 1

    @property
    def col_head(self):
        return 0

    @property
    def col_tail(self):
        return len(self.text[self.row]) - 1

    def __repr__(self):
        return ''.join(''.join(line) for line in self.text)

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
            self.col = self.col_tail

    def command_f(self):
        if self.col < self.col_tail:
            self.col += 1
        elif self.row < self.row_tail:
            self.row += 1
            self.col = self.col_head

    def command_d(self):
        line = self.text[self.row]
        if self.col < self.col_tail:
            line.pop(self.col)
        elif self.row < self.row_tail:
            line.pop()  # remove '\n'
            line.extend(self.text.pop(self.row + 1))

    def command_k(self):
        line = self.text[self.row]
        if self.col < self.col_tail:
            self.buffer = line[self.col:-1]
            self.text[self.row] = line[:self.col] + ['\n']
            self.col = self.col_tail
        elif self.row < self.row_tail:
            self.buffer = ['\n']
            line.pop()  # remove '\n'
            line.extend(self.text.pop(self.row + 1))

    def command_y(self):
        if self.buffer == ['\n']:
            remainder = self.text[self.row][self.col:]
            self.text.insert(self.row + 1, remainder)
            self.text[self.row] = self.text[self.row][:self.col] + ['\n']
            self.row += 1
            self.col = self.col_head
        else:
            line = self.text[self.row]
            line[self.col:self.col] = self.buffer
            self.col += len(self.buffer)


def main():
    import sys
    lines = []
    for line in sys.stdin:
        line = line.rstrip('\n')
        if line == 'END_OF_TEXT':
            break
        lines.append(line)

    editer = Editer(lines)

    commands_map = {
        'a': editer.command_a,
        'e': editer.command_e,
        'p': editer.command_p,
        'n': editer.command_n,
        'b': editer.command_b,
        'f': editer.command_f,
        'd': editer.command_d,
        'k': editer.command_k,
        'y': editer.command_y,
    }

    for command in sys.stdin:
        cmd = command.rstrip('\n')
        if cmd == '-':
            break
        if cmd in commands_map:
            commands_map[cmd]()

    print(editer, end='')


if __name__ == '__main__':
    main()