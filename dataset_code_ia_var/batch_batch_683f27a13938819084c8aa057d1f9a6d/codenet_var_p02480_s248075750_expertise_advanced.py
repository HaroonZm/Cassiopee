import sys

def main():
    try:
        num = int(sys.stdin.readline())
        print(num ** 3)
    except (ValueError, TypeError):
        print("Entrée invalide", file=sys.stderr)

if __name__ == "__main__":
    main()