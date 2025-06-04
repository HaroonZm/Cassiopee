import sys

class IOHelper:
    def __init__(self, func=None):
        self.func = func if func else self.default_input
    def __call__(self):
        return self.func()
    @staticmethod
    def default_input():
        return input()

def file_input(filename='inputFile.txt'):
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line: break
            yield line.rstrip('\n')
            
def resolve(io_instance):
    char = io_instance()
    r="vowel" if char in set(['a','i','u','e','o']) else "consonant"
    print(r)

if __name__=='__main__':
    reader = IOHelper()
    if sys.platform=="ios":
        fgen = file_input()
        reader = IOHelper(lambda: next(fgen))
    # functional style
    actions = [resolve]
    [fn(reader) for fn in actions]