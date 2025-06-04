from sys import stdin

def main():
    s = int(stdin.readline())
    consecutive = 0
    for _ in range(s):
        a, b = stdin.readline().split()
        consecutive = consecutive + 1 if a == b else 0
        if consecutive == 3:
            print('Yes')
            return
    print('No')

if __name__ == "__main__":
    main()