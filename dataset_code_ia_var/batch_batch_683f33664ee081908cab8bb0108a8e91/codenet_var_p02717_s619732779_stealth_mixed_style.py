import sys

class Handler:
    pass

def magic(*args):
    print(args[2], args[0], args[1])

def main():
    X, Y, Z = map(int, [*next(((word for line in sys.stdin for word in line.split()),) for _ in range(3))])
    magic(X, Y, Z)

if __name__ == "__main__":
    foo = lambda: main()
    foo()