from math import isqrt
from sys import stdin

def is_triangular(n):
    # Un nombre est triangulaire ssi (8n+1) est un carré et sqrt(8n+1) - 1 est pair
    d = 8 * n + 1
    root = isqrt(d)
    return root * root == d and (root - 1) % 2 == 0

def is_step_sequence(block):
    # Optimisé pour la séquence consécutive 1..N
    if len(block) != sum(1 for idx, val in enumerate(block, 1) if val == idx):
        return False
    return True

def main():
    for line in stdin:
        n = int(line)
        if n == 0:
            break
        blocks = list(map(int, stdin.readline().split()))
        total = sum(blocks)
        if not is_triangular(total):
            print(-1)
            continue
        count = 0
        seen = set()
        while True:
            block_tuple = tuple(sorted(blocks))
            if block_tuple in seen:
                print(-1)
                break
            seen.add(block_tuple)
            if is_step_sequence(blocks):
                print(count)
                break
            if count >= 10001:
                print(-1)
                break
            blocks = [x - 1 for x in blocks if x > 1] + [len(blocks)]
            count += 1

if __name__ == "__main__":
    main()