import sys

class Cursor:
    def __init__(self, text):
        self.text = []
        for line in text:
            self.text.append(list(line))
        self.buffer = ""
        self.line = 1
        self.pos = (0, 1)  # beginning of line

    def _get_end_of_line_pos(self):
        last_char_idx = len(self.text[self.line - 1])
        return (last_char_idx, last_char_idx + 1)

    def has_prev_line(self):
        return self.line > 1

    def has_next_line(self):
        return self.line < len(self.text)

    def move_to_beginning(self):
        self.pos = (0, 1)

    def move_to_end(self):
        self.pos = self._get_end_of_line_pos()

    def go_to_prev_line(self):
        if self.has_prev_line():
            self.line -= 1

    def go_to_next_line(self):
        if self.has_next_line():
            self.line += 1

    def move_right(self):
        if self.pos != self._get_end_of_line_pos():
            self.pos = (self.pos[0] + 1, self.pos[1] + 1)
        else:
            if self.has_next_line():
                self.line += 1
                self.pos = (0, 1)

    def move_left(self):
        if self.pos != (0,1):
            self.pos = (self.pos[0] - 1, self.pos[1] - 1)
        else:
            if self.has_prev_line():
                self.line -= 1
                self.pos = self._get_end_of_line_pos()

    def remove_current(self):
        if self.pos != self._get_end_of_line_pos():
            line_chars = self.text[self.line - 1]
            self.text[self.line - 1] = line_chars[:self.pos[0]] + line_chars[self.pos[1]:]
        else:
            if self.has_next_line():
                self.text[self.line - 1] = self.text[self.line - 1][:self.pos[0]] + self.text[self.line]
                self.text.pop(self.line)

    def remove_to_end(self):
        if self.pos == self._get_end_of_line_pos():
            if self.has_next_line():
                self.remove_current()
                self.buffer = '\n'
        else:
            rest = self.text[self.line - 1][self.pos[0]:]
            self.buffer = rest
            self.text[self.line - 1] = self.text[self.line - 1][:self.pos[0]]
            self.pos = self._get_end_of_line_pos()

    def paste(self):
        if self.buffer:
            if self.buffer == '\n':
                before = self.text[self.line - 1][:self.pos[0]]
                after = self.text[self.line - 1][self.pos[0]:]
                self.text[self.line - 1] = before
                self.text.insert(self.line, after)
                self.line += 1
                self.pos = (0, 1)
            else:
                for i in range(len(self.buffer)):
                    self.text[self.line - 1].insert(self.pos[0] + i, self.buffer[i])
                self.pos = (self.pos[0] + len(self.buffer), self.pos[1] + len(self.buffer))

    def print_text(self):
        for line in self.text:
            print("".join(line))

class Editor:
    def __init__(self, text):
        self.cursor = Cursor(text)

    def process(self, commands):
        if not isinstance(commands, list):
            commands = [commands]
        for cmd in commands:
            self._do_command(cmd)
        self.cursor.print_text()

    def _do_command(self, cmd):
        if cmd == 'a':
            self.cursor.move_to_beginning()
        elif cmd == 'e':
            self.cursor.move_to_end()
        elif cmd == 'p':
            self.cursor.go_to_prev_line()
            self.cursor.move_to_beginning()
        elif cmd == 'n':
            self.cursor.go_to_next_line()
            self.cursor.move_to_beginning()
        elif cmd == 'f':
            self.cursor.move_right()
        elif cmd == 'b':
            self.cursor.move_left()
        elif cmd == 'd':
            self.cursor.remove_current()
        elif cmd == 'k':
            self.cursor.remove_to_end()
        elif cmd == 'y':
            self.cursor.paste()

def load_input():
    all_lines = []
    while True:
        try:
            line = input()
            all_lines.append(line)
        except EOFError:
            break
    return all_lines

def split_end_of_text(data):
    if "END_OF_TEXT" not in data:
        print("DO NOT DETECT END_OF_TEXT. got:", data)
        sys.exit(1)
    idx = data.index("END_OF_TEXT")
    return data[:idx], data[idx+1:]

def main():
    inputs = load_input()
    text, commands = split_end_of_text(inputs)
    editor = Editor(text)
    editor.process(commands)

main()