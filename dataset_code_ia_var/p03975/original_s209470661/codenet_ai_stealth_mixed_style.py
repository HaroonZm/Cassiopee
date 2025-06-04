from sys import stdin

def process_input():
    tokens = stdin.readline().split()
    n = int(tokens[0])
    a, b = int(tokens[1]), int(tokens[2])
    cnt = 0
    for _ in range(n):
        val = int(stdin.readline())
        if not (a <= val < b):
            cnt += 1
    return cnt

if __name__ == "__main__":
    res = process_input()
    print(f"{res}")