from collections import deque
import sys

def solve(n, k, m):
    dq = deque(range(1, n+1))
    dq.rotate(-(m-1))
    while len(dq) > 1:
        dq.popleft()
        dq.rotate(-(k-1))
    return dq[0]

def main():
    input_lines = sys.stdin.read().splitlines()
    results = []
    for line in input_lines:
        if not line.strip():
            continue
        n, k, m = map(int, line.split())
        if n == 0 and k == 0 and m == 0:
            break
        results.append(solve(n, k, m))
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    main()