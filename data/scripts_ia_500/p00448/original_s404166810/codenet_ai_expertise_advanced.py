def v():
    from sys import stdin
    input_iter = iter(stdin.readline, '0 0\n')
    for line in input_iter:
        r, _ = map(int, line.split())
        matrix = [stdin.readline().split() for _ in range(r)]
        # Transpose and convert each column from binary to int
        d = [int(''.join(col), 2) for col in zip(*matrix)]
        max_score = 0
        limit = (1 << (r - 1)) if r > 1 else 1
        half = r // 2
        # Precompute popcounts for optimization
        from math import inf
        for m in range(limit):
            # XOR m with each column integer, then count set bits
            score = 0
            for s in d:
                c = bin(m ^ s).count('1')
                score += c if c > half else r - c
            if score > max_score:
                max_score = score
        print(max_score)
if __name__ == '__main__':
    v()