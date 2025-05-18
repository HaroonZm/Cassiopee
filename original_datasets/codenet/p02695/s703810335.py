#!/usr/bin/env python3
import sys

def solve(N: int, M: int, Q: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]"):
    from itertools import combinations_with_replacement
    answer = 0
    for AA in combinations_with_replacement(range(1,M+1),r=N):
        
        tmp_ans = 0
        for q in range(Q):
            if AA[b[q]-1] - AA[a[q]-1] ==  c[q]:
                tmp_ans += d[q]
  
        answer = max(answer,tmp_ans)
    print(answer)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int()] * (Q)  # type: "List[int]"
    b = [int()] * (Q)  # type: "List[int]"
    c = [int()] * (Q)  # type: "List[int]"
    d = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, M, Q, a, b, c, d)

if __name__ == '__main__':
    main()