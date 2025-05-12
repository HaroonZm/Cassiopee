#!/usr/bin/env python

#
# FileName: 	queue
# CreatedDate:  2020-07-08 17:27:31 +0900
# LastModified: 2020-07-08 17:38:55 +0900
#

import os
import sys
# import numpy as np
# import pandas as pd
from collections import deque

def main():
    n, q = map(int, input().split())
    big_queue = []
    for _ in range(n):
        p = deque()
        big_queue.append(p)

    for _ in range(q):
        query = list(map(int, input().split()))
        if len(query) == 3:
            big_queue[query[1]].append(query[2])
        else:
            if query[0] == 1:
                if big_queue[query[1]]:
                    print(big_queue[query[1]][0])
            else:
                if big_queue[query[1]]:
                    big_queue[query[1]].popleft()
        

if __name__ == "__main__":
    main()