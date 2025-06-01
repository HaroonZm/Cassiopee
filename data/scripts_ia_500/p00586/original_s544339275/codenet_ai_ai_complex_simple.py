import sys
from functools import reduce
from operator import add
class StreamProcessor:
    def __init__(self, stream):
        self.stream = stream
    def __iter__(self):
        return self
    def __next__(self):
        line = next(self.stream)
        parts = list(map(lambda x: int(x), filter(lambda x: x.strip() != '', line.split())))
        if len(parts) < 2:
            raise StopIteration
        return parts[0], parts[1]
def complex_addition(pair):
    return reduce(lambda x, y: x + y, (pair[0], pair[1]))
def main():
    sp = StreamProcessor(iter(sys.stdin))
    while True:
        try:
            a, b = next(sp)
            print(complex_addition((a, b)))
        except StopIteration:
            break
if __name__ == '__main__':
    main()