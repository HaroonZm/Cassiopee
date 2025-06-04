from sys import stdin

def decompose(n, powers=(1 << i for i in range(9, -1, -1))):
    return [p for p in powers if (n := n - p) >= -p]

for line in stdin:
    n = int(line)
    res = [str(1 << i) for i in range(10) if n & (1 << i)]
    print(' '.join(res))