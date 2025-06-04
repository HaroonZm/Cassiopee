from sys import stdin

def main():
    *pastas, = (int(stdin.readline()) for _ in range(3))
    *drinks, = (int(stdin.readline()) for _ in range(2))
    print(min(pastas) + min(drinks) - 50)

if __name__ == '__main__':
    main()