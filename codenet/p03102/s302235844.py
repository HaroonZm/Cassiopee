#!/usr/bin/env python3

import numpy as np
import sys

read = sys.stdin.buffer.read

def main():
    n, m, c = map(int, input().split())
    l = list(map(int,input().split()))
    p = [list( map( int, input().split() ) ) for i in range(n)]
    
    count=0
    for sor in p:
        tmp=c
        for i, j in enumerate(sor):
            tmp=tmp+j*l[i]
        if tmp>0:
            count+=1
    print(count)

if __name__ == '__main__':
    main()