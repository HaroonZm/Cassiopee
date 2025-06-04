from collections import Counter
from itertools import chain
import sys

def main():
    h, w = map(int, sys.stdin.readline().split())
    a = [sys.stdin.readline().strip() for _ in range(h)]

    char_counter = Counter(chain.from_iterable(a))
    f_num = t_num = 0

    for count in char_counter.values():
        f, rem = divmod(count, 4)
        t, rem2 = divmod(rem, 2)
        f_num += f
        t_num += t

    req_f = (h // 2) * (w // 2)
    req_t = (h % 2) * (w // 2) + (w % 2) * (h // 2)

    if f_num < req_f:
        print('No')
        return
    t_num += (f_num - req_f) * 2
    if t_num < req_t:
        print('No')
        return
    print('Yes')

if __name__ == '__main__':
    main()