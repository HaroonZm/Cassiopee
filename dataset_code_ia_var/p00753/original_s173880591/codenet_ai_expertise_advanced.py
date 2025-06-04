from array import array
from sys import stdin

N = 123456 * 2 + 1
p = array('b', (1,)) * N
p[:2] = array('b', (0, 0))

def sieve():
    for i in range(2, int(N ** 0.5) + 1):
        if p[i]:
            p[i*i:N:i] = array('b', (0,)) * len(p[i*i:N:i])

sieve()

def main():
    for line in stdin:
        n = int(line)
        if not n:
            break
        print(sum(p[n + 1:n * 2 + 1]))

main()