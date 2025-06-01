class Cursor:
    def __init__(self, text):
        self.text = []
        for line in text:
            self.text.append(list(line))
        self.line = 1
        self.pos = 0
        self.buffer = ""

    def beginning_of_line(self):
        self.pos = 0

    def end_of_line(self):
        self.pos = len(self.text[self.line - 1])

    def prev_line(self):
        if self.line > 1:
            self.line -= 1
            self.pos = 0

    def next_line(self):
        if self.line < len(self.text):
            self.line += 1
            self.pos = 0

    def right_pos(self):
        if self.pos < len(self.text[self.line -1 ]):
            self.pos += 1
        else:
            if self.line < len(self.text):
                self.line += 1
                self.pos = 0

    def left_pos(self):
        if self.pos > 0:
            self.pos -= 1
        else:
            if self.line > 1:
                self.line -= 1
                self.pos = len(self.text[self.line -1 ])

    def remove_current_pos(self):
        line_index = self.line -1
        if self.pos < len(self.text[line_index]):
            del self.text[line_index][self.pos]
        else:
            if self.line < len(self.text):
                # Merge next line to current
                self.text[line_index] += self.text[self.line]
                del self.text[self.line]

    def remove_to_end_of_line(self):
        line_index = self.line -1
        if self.pos == len(self.text[line_index]):
            if self.line < len(self.text):
                self.buffer = '\n'
                self.remove_current_pos()
        else:
            self.buffer = self.text[line_index][self.pos:]
            self.text[line_index] = self.text[line_index][:self.pos]

    def paste(self):
        if self.buffer == '':
            return

        line_index = self.line -1
        if self.buffer == '\n':
            current_line = self.text[line_index]
            new_line = current_line[self.pos:]
            self.text[line_index] = current_line[:self.pos]
            self.text.insert(self.line, new_line)
            self.line += 1
            self.pos = 0
        else:
            for i, ch in enumerate(self.buffer):
                self.text[line_index].insert(self.pos + i, ch)
            self.pos += len(self.buffer)

    def print_text(self):
        for line in self.text:
            print("".join(line))

class Editor:
    def __init__(self, text):
        self.cursor = Cursor(text)

    def process(self, commands):
        if type(commands) != list:
            commands = [commands]
        for c in commands:
            self.process_command(c)
        self.cursor.print_text()

    def process_command(self, command):
        if command == 'a':
            self.cursor.beginning_of_line()
        elif command == 'e':
            self.cursor.end_of_line()
        elif command == 'p':
            self.cursor.prev_line()
            self.cursor.beginning_of_line()
        elif command == 'n':
            self.cursor.next_line()
            self.cursor.beginning_of_line()
        elif command == 'f':
            self.cursor.right_pos()
        elif command == 'b':
            self.cursor.left_pos()
        elif command == 'd':
            self.cursor.remove_current_pos()
        elif command == 'k':
            self.cursor.remove_to_end_of_line()
        elif command == 'y':
            self.cursor.paste()

def load_input():
    inputs = []
    while True:
        try:
            line = input()
            inputs.append(line)
        except EOFError:
            break
    return inputs

def split_end_of_text(inputs):
    for i in range(len(inputs)):
        if inputs[i] == 'END_OF_TEXT':
            return inputs[:i], inputs[i+1:]
    print("END_OF_TEXT not found")
    exit(1)

def main():
    inputs = load_input()
    text, commands = split_end_of_text(inputs)
    editor = Editor(text)
    editor.process(commands)

main()