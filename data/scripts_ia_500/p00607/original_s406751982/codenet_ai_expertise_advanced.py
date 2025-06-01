import sys
from collections import deque
from typing import List, Tuple

class Cursor:
    BOL: Tuple[int, int] = (0, 1)

    def __init__(self, text: List[str]):
        assert all(isinstance(line, str) for line in text), "Text must be list of strings"
        self.text = [list(line) for line in text]
        self.buffer: List[str] = []
        self.line: int = 1
        self.pos: Tuple[int, int] = self.BOL

    def _check_line(self) -> None:
        if not (1 <= self.line <= len(self.text)):
            raise IndexError("Line number out of range")

    def _end_of_line_pos(self) -> Tuple[int, int]:
        length = len(self.text[self.line - 1])
        return length, length + 1

    def has_prev_line(self) -> bool:
        return self.line > 1

    def has_next_line(self) -> bool:
        return self.line < len(self.text)

    def beginning_of_line(self) -> None:
        self.pos = self.BOL

    def end_of_line(self) -> None:
        self.pos = self._end_of_line_pos()

    def prev_line(self) -> None:
        if self.has_prev_line():
            self.line -= 1
            self.beginning_of_line()

    def next_line(self) -> None:
        if self.has_next_line():
            self.line += 1
            self.beginning_of_line()

    def right_pos(self) -> None:
        eol_pos = self._end_of_line_pos()
        if self.pos != eol_pos:
            self.pos = (self.pos[0] + 1, self.pos[1] + 1)
        elif self.has_next_line():
            self.line += 1
            self.pos = self.BOL

    def left_pos(self) -> None:
        if self.pos != self.BOL:
            self.pos = (self.pos[0] - 1, self.pos[1] - 1)
        elif self.has_prev_line():
            self.line -= 1
            self.pos = self._end_of_line_pos()

    def remove_current_pos(self) -> None:
        eol_pos = self._end_of_line_pos()
        line_idx = self.line - 1

        if self.pos != eol_pos:
            start, end = self.pos
            self.text[line_idx] = self.text[line_idx][:start] + self.text[line_idx][end:]
        elif self.has_next_line():
            # Merge current line with next line at cursor pos
            next_line = self.text.pop(self.line)
            self.text[line_idx][self.pos[0]:self.pos[0]] = next_line

    def remove_to_end_of_line(self) -> None:
        eol_pos = self._end_of_line_pos()
        line_idx = self.line - 1

        if self.pos == eol_pos:
            if self.has_next_line():
                self.remove_current_pos()
                self.buffer = ['\n']
        else:
            start = self.pos[0]
            self.buffer = self.text[line_idx][start:]
            self.text[line_idx] = self.text[line_idx][:start]
            self.pos = self._end_of_line_pos()

    def paste(self) -> None:
        if not self.buffer:
            return

        line_idx = self.line - 1
        if self.buffer == ['\n']:
            before = self.text[line_idx][:self.pos[0]]
            after = self.text[line_idx][self.pos[0]:]
            self.text[line_idx] = before
            self.text.insert(self.line, after)
            self.line += 1
            self.pos = self.BOL
        else:
            self.text[line_idx][self.pos[0]:self.pos[0]] = self.buffer
            length = len(self.buffer)
            self.pos = (self.pos[0] + length, self.pos[1] + length)

    def print(self) -> None:
        print('\n'.join(''.join(line) for line in self.text))

class Editor:
    _command_map = {
        'a': lambda cur: cur.beginning_of_line(),
        'e': lambda cur: cur.end_of_line(),
        'p': lambda cur: (cur.prev_line(), cur.beginning_of_line()),
        'n': lambda cur: (cur.next_line(), cur.beginning_of_line()),
        'f': lambda cur: cur.right_pos(),
        'b': lambda cur: cur.left_pos(),
        'd': lambda cur: cur.remove_current_pos(),
        'k': lambda cur: cur.remove_to_end_of_line(),
        'y': lambda cur: cur.paste(),
    }

    def __init__(self, text: List[str]):
        self.cursor = Cursor(text)

    def process(self, commands: List[str]) -> None:
        for cmd in (commands if isinstance(commands, list) else [commands]):
            action = self._command_map.get(cmd)
            if action:
                action(self.cursor)
        self.cursor.print()

def load_input() -> List[str]:
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
    return lines

def split_end_of_text(inputs: List[str]) -> Tuple[List[str], List[str]]:
    try:
        index = inputs.index('END_OF_TEXT')
    except ValueError:
        print("DO NOT DETECT END_OF_TEXT. got:", inputs)
        sys.exit(1)
    return inputs[:index], inputs[index+1:]

def main() -> None:
    inputs = load_input()
    text, commands = split_end_of_text(inputs)
    editor = Editor(text)
    editor.process(commands)

if __name__ == '__main__':
    main()