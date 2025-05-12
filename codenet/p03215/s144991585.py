#!/usr/bin/env python3
import sys
from itertools import accumulate
import math

def solve(N: int, K: int, a: "List[int]"):
    accum = [0] + list(accumulate(a))
    sum_list = []
    for i in range(0,N):
        for j in range(i+1,N+1):
            sum_list.append(accum[j]-accum[i])
    sum_list.sort(reverse=True)
    max_bit = int(math.log2(sum_list[0]))
    answer = 0

    for i in range(max_bit,-1,-1):
        count = 0
        tmp = []
        for j in range(len(sum_list)):
            if sum_list[j] & 1<<i:
                count +=1
                tmp.append(sum_list[j])
            
        if count >= K:
            answer += 2**i
            sum_list = tmp
    print(answer)

    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a)

if __name__ == '__main__':
    main()