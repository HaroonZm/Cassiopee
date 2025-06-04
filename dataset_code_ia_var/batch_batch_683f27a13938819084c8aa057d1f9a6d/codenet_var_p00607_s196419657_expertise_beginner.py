class Editer:
    def __init__(self, text):
        self.row = 0
        self.col = 0
        self.text = []
        for t in text:
            new_line = []
            for ch in t:
                new_line.append(ch)
            new_line.append('\n')
            self.text.append(new_line)
        self.buffer = []

    def row_head(self):
        return 0

    def row_tail(self):
        return len(self.text) - 1

    def col_head(self):
        return 0

    def col_tail(self):
        return len(self.text[self.row]) - 1

    def __repr__(self):
        s = ""
        for t in self.text:
            for ch in t:
                s += ch
        return s

    def command_a(self):
        self.col = self.col_head()

    def command_e(self):
        self.col = self.col_tail()

    def command_p(self):
        if self.row > self.row_head():
            self.row = self.row - 1
        self.col = self.col_head()

    def command_n(self):
        if self.row < self.row_tail():
            self.row = self.row + 1
        self.col = self.col_head()

    def command_b(self):
        if self.col > self.col_head():
            self.col = self.col - 1
        elif self.row > self.row_head():
            self.row = self.row - 1
            self.col = self.col_tail()

    def command_f(self):
        if self.col < self.col_tail():
            self.col = self.col + 1
        elif self.row < self.row_tail():
            self.row = self.row + 1
            self.col = self.col_head()

    def command_d(self):
        if self.col < self.col_tail():
            self.text[self.row].pop(self.col)
        elif self.row < self.row_tail():
            self.text[self.row].pop(self.col_tail())
            next_line = self.text.pop(self.row + 1)
            self.text[self.row].extend(next_line)

    def command_k(self):
        if self.col < self.col_tail():
            self.buffer = self.text[self.row][self.col:-1]
            self.text[self.row] = self.text[self.row][:self.col]
            self.text[self.row].append('\n')
            self.col = self.col_tail()
        elif self.row < self.row_tail():
            self.buffer = ['\n']
            self.text[self.row].pop(self.col_tail())
            next_line = self.text.pop(self.row + 1)
            self.text[self.row].extend(next_line)

    def command_y(self):
        if self.buffer != ['\n']:
            self.text[self.row][self.col:self.col] = self.buffer
            self.col = self.col + len(self.buffer)
        else:
            part = self.text[self.row][self.col:]
            self.text.insert(self.row + 1, part)
            self.text[self.row] = self.text[self.row][:self.col]
            self.text[self.row].append('\n')
            self.row = self.row + 1
            self.col = self.col_head()

def main():
    text = []
    while True:
        line = input()
        if line == 'END_OF_TEXT':
            break
        text.append(line)

    editer = Editer(text)

    while True:
        command = input()
        if command == 'a':
            editer.command_a()
        elif command == 'e':
            editer.command_e()
        elif command == 'p':
            editer.command_p()
        elif command == 'n':
            editer.command_n()
        elif command == 'f':
            editer.command_f()
        elif command == 'b':
            editer.command_b()
        elif command == 'd':
            editer.command_d()
        elif command == 'y':
            editer.command_y()
        elif command == 'k':
            editer.command_k()
        elif command == '-':
            break

    print(editer, end='')

if __name__ == '__main__':
    main()