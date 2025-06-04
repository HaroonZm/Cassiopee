from abc import ABC, abstractmethod
from typing import List


class Command(ABC):
    @abstractmethod
    def execute(self, dictionary: 'Dictionary'):
        pass


class InsertCommand(Command):
    def __init__(self, value: str):
        self.value = value

    def execute(self, dictionary: 'Dictionary'):
        dictionary.insert(self.value)


class FindCommand(Command):
    def __init__(self, value: str):
        self.value = value

    def execute(self, dictionary: 'Dictionary'):
        print("yes" if dictionary.find(self.value) else "no")


class Dictionary(ABC):
    @abstractmethod
    def insert(self, word: str):
        pass

    @abstractmethod
    def find(self, word: str) -> bool:
        pass


class TrieNode:
    __slots__ = ['children', 'is_end']

    def __init__(self):
        self.children = {}
        self.is_end = False


class TrieDictionary(Dictionary):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end = True

    def find(self, word: str) -> bool:
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.is_end


class CommandParser:
    def __init__(self):
        self.command_map = {
            'insert': InsertCommand,
            'find': FindCommand
        }

    def parse(self, line: str) -> Command:
        cmd, val = line.split()
        if cmd in self.command_map:
            return self.command_map[cmd](val)
        else:
            raise ValueError(f"Unknown command: {cmd}")


class DictionaryApp:
    def __init__(self, dictionary: Dictionary, commands: List[Command]):
        self.dictionary = dictionary
        self.commands = commands

    def run(self):
        for command in self.commands:
            command.execute(self.dictionary)


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    parser = CommandParser()
    commands = [parser.parse(input().strip()) for _ in range(n)]

    dictionary = TrieDictionary()
    app = DictionaryApp(dictionary, commands)
    app.run()


if __name__ == "__main__":
    main()