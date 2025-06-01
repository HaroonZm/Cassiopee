import sys

def solve(target_name, n):
    first_char = target_name[0]
    length = len(target_name)
    count = 0

    for _ in range(n):
        signboard = input()
        positions = [i for i, ch in enumerate(signboard) if ch == first_char]

        if any(signboard[pos::gap].startswith(target_name)
               for pos in positions
               for gap in range(1, (len(signboard) - pos) // length + 1)):
            count += 1

    return count

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().rstrip('\n')
    print(solve(s, n))

if __name__ == '__main__':
    main()