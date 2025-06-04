import sys

def find_digit(pos):
    length = 1
    count = 9
    start = 1
    while pos > length * count:
        pos -= length * count
        length += 1
        count *= 10
        start *= 10
    num = start + (pos - 1) // length
    digit_index = (pos - 1) % length
    return str(num)[digit_index]

for line in sys.stdin:
    N,K = map(int, line.split())
    if N == 0 and K == 0:
        break
    res = [find_digit(N + i) for i in range(K)]
    print(''.join(res))