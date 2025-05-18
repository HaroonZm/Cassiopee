#!/usr/bin/env python3

import sys

S = input().strip()
for i in range(len(S)):
    for j in range(i+1, len(S)):
        if S[i] == S[j]:
            print('no')
            sys.exit(0)
print('yes')