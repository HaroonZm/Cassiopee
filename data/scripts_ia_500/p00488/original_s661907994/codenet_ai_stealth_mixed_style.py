import sys
def main(args):
    pastas = []
    for _ in range(3):
        pastas.append(int(sys.stdin.readline()))
    drinks = list(map(lambda x: int(sys.stdin.readline()), range(2)))
    total = min(pastas) + min(drinks) - 50
    print(total)

if __name__ == "__main__":
    main(sys.argv[1:])