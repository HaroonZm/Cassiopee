import sys
from typing import List, Tuple, Any

class Cursor:
    BOL: Tuple[int, int] = (0, 1)

    def __init__(self, text: List[str]):
        assert isinstance(text, list)
        self.text: List[List[str]] = [list(line) for line in text]
        self.buffer: Any = ""
        self.line: int = 1
        self.pos: Tuple[int, int] = self.BOL

    @property
    def current_line(self) -> List[str]:
        return self.text[self.line - 1]

    @property
    def line_count(self) -> int:
        return len(self.text)

    def _check(self):
        assert self.line > 0

    def _get_pos_end_of_line(self) -> Tuple[int, int]:
        last_char = len(self.current_line)
        return (last_char, last_char + 1)

    def has_prev_line(self) -> bool:
        return self.line > 1

    def has_next_line(self) -> bool:
        return self.line < self.line_count

    def beginning_of_line(self) -> None:
        self.pos = self.BOL

    def end_of_line(self) -> None:
        self.pos = self._get_pos_end_of_line()

    def prev_line(self) -> None:
        if self.has_prev_line():
            self.line -= 1

    def next_line(self) -> None:
        if self.has_next_line():
            self.line += 1

    def right_pos(self) -> None:
        if self.pos != self._get_pos_end_of_line():
            self.pos = tuple(map(lambda x: x + 1, self.pos))
        elif self.has_next_line():
            self.line += 1
            self.pos = self.BOL

    def left_pos(self) -> None:
        if self.pos != self.BOL:
            self.pos = tuple(map(lambda x: x - 1, self.pos))
        elif self.has_prev_line():
            self.line -= 1
            self.pos = self._get_pos_end_of_line()

    def remove_current_pos(self) -> None:
        if self.pos != self._get_pos_end_of_line():
            l = self.current_line
            idx0, idx1 = self.pos
            del l[idx0:idx1]
        elif self.has_next_line():
            self.text[self.line - 1][self.pos[0]:self.pos[0]] = self.text[self.line]
            del self.text[self.line]

    def remove_to_end_of_line(self) -> None:
        if self.pos == self._get_pos_end_of_line():
            if self.has_next_line():
                self.remove_current_pos()
                self.buffer = '\n'
        else:
            idx = self.pos[0]
            self.buffer = self.current_line[idx:]
            del self.current_line[idx:]
            self.pos = self._get_pos_end_of_line()

    def paste(self) -> None:
        if not self.buffer:
            return
        if self.buffer == '\n':
            prev = self.current_line[:self.pos[0]]
            nextp = self.current_line[self.pos[0]:]
            self.text[self.line - 1] = prev
            self.text.insert(self.line, nextp)
            self.line += 1
            self.pos = self.BOL
        else:
            base = self.pos[0]
            insert_len = len(self.buffer)
            self.current_line[base:base] = self.buffer
            self.pos = (self.pos[0] + insert_len, self.pos[1] + insert_len)

    def print(self) -> None:
        print('\n'.join(''.join(line) for line in self.text))

class Editor:
    def __init__(self, text: List[str]):
        assert isinstance(text, list)
        self.cursor = Cursor(text)

    def process(self, commands: List[str]) -> None:
        for cmd in commands if isinstance(commands, list) else [commands]:
            self._process(cmd)
        self.cursor.print()

    def _process(self, command: str) -> None:
        dispatch = {
            'a': self.cursor.beginning_of_line,
            'e': self.cursor.end_of_line,
            'p': lambda: (self.cursor.prev_line(), self.cursor.beginning_of_line()),
            'n': lambda: (self.cursor.next_line(), self.cursor.beginning_of_line()),
            'f': self.cursor.right_pos,
            'b': self.cursor.left_pos,
            'd': self.cursor.remove_current_pos,
            'k': self.cursor.remove_to_end_of_line,
            'y': self.cursor.paste,
        }
        func = dispatch.get(command)
        if func:
            func()

def load_input() -> List[str]:
    return list(iter(input, ''))

def split_end_of_text(inputs: List[str]) -> Tuple[List[str], List[str]]:
    try:
        idx = inputs.index('END_OF_TEXT')
        return inputs[:idx], inputs[idx + 1:]
    except ValueError:
        print("DO NOT DETECT END_OF_TEXT. got:", inputs)
        sys.exit(1)

def main() -> None:
    inputs = []
    for line in sys.stdin:
        inputs.append(line.rstrip('\n'))
    text, commands = split_end_of_text(inputs)
    assert 'END_OF_TEXT' not in text
    assert 'END_OF_TEXT' not in commands
    editor = Editor(text)
    editor.process(commands)

if __name__ == '__main__':
    main()