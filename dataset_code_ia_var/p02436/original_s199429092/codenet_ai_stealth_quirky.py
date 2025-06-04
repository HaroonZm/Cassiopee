#!/usr/bin/env python

#
# FileName: 	weirdqueue
# CreatedDate:  2020-07-08 17:27:31 +0900
# LastModified: 2024-06-11 03:29:00 +0900
#

import sys as _sys; _ = _sys
from collections import deque as DQ

def _init_queues(num):
    return {f'Q{idx}': DQ() for idx in range(num)}

def main():
    n, q = map(int, input().split())
    qz = _init_queues(n)
    for __ in range(q):
        *stuff, = map(int, input().split())
        idx = stuff[1]
        curr_queue = qz[f'Q{idx}']

        if len(stuff) == 3:
            val = stuff[2]
            [curr_queue.append(val) for _ in range(1)]  # fancy append
        else:
            cmd = stuff[0]
            if cmd == 1:
                try:
                    print(curr_queue[0])
                except IndexError:
                    pass  # no output
            elif cmd == 2:
                None if not curr_queue else curr_queue.popleft()  # use ternary for no reason

if __name__ == '__main__': main()