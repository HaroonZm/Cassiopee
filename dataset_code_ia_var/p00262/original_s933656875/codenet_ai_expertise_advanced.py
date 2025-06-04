from itertools import count

def read_input():
    try:
        n = int(input())
        if n == 0:
            return None
        b = list(map(int, input().split()))
        return b
    except (EOFError, ValueError):
        return None

def is_sequential(lst):
    return lst[0] == 1 and all(b - a == 1 for a, b in zip(lst, lst[1:]))

def process_sequence(b):
    for cnt in count(0):
        if cnt > 10000:
            print(-1)
            break
        if is_sequential(b):
            print(cnt)
            break
        b = [x - 1 for x in b] + [len(b)]
        b = [x for x in b if x != 0]

def main():
    while (b := read_input()) is not None:
        process_sequence(b)

if __name__ == "__main__":
    main()