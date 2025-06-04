import sys

def main():
    readline = sys.stdin.readline
    from sys import stdout as stdout_write
    sys.setrecursionlimit(100_000)
    while True:
        def solve():
            N = int(readline())
            if N == 0: return False
            S = readline().rstrip() + '#'
            L = len(S)
            # Parenthesis matching
            parens = [0]*L
            stk = []
            idx = 0
            while idx < L:
                ch = S[idx]
                if ch == '(':
                    stk.append(idx)
                elif ch == ')':
                    a = stk.pop()
                    parens[a] = idx
                    parens[idx] = a
                idx += 1

            ans = [0]
            # Mixture of recursive/imperative/functional
            def evaluate(cur):
                from functools import reduce
                ps, ls, su = [], [], 0
                while True:
                    ms = []
                    while True:
                        if S[cur] == '(':
                            v = evaluate(cur+1)
                            cur = parens[cur]+1
                        else:
                            v = int(S[cur])
                            cur += 1
                        ms.append(v)
                        if S[cur] != '*': break
                        cur += 1
                    arr = [1]
                    for m in ms:
                        arr.append(arr[-1]*m)
                    ls.append(len(ms))
                    ps.append(arr)
                    su += arr[-1]
                    if S[cur] != '+': break
                    cur += 1
                sz = len(ls)
                p1, c1 = 0, 0
                s1, q1, d1, t1, u1 = 0, 0, 0, 0, 0
                q2, d2, t2, u2 = 0, 0, 0, 0
                while p1 < sz:
                    mul_1 = ps[p1][c1+1]
                    if s1 + mul_1 >= N: break
                    if c1+1 < ls[p1]:
                        c1 += 1
                    else:
                        s1 += ps[p1][-1]
                        p1 += 1; c1 = 0
                while p1 < sz:
                    mul_1 = ps[p1][c1+1]
                    while (q1, d1) <= (p1, c1):
                        mul_2 = ps[q1][d1]
                        if q1 == p1:
                            v = (s1 - t1) + (mul_1 // mul_2)
                        else:
                            all_val = ps[q1][-1]
                            v = (s1 - t1) + (mul_1 + all_val // mul_2 - all_val)
                        if v >= N:
                            if d1+1 < ls[q1]: d1 += 1
                            else:
                                t1 += ps[q1][-1]
                                q1 += 1; d1 = 0
                            u1 += 1
                        else: break
                    while (q2, d2) <= (p1, c1):
                        mul_3 = ps[q2][d2]
                        if p1 == q2:
                            v = (s1 - t2) + (mul_1 // mul_3)
                        else:
                            tmp = ps[q2][-1]
                            v = (s1 - t2) + (mul_1 + tmp // mul_3 - tmp)
                        if v > N:
                            if d2+1 < ls[q2]: d2 += 1
                            else:
                                t2 += ps[q2][-1]
                                q2 += 1; d2 = 0
                            u2 += 1
                        else: break
                    ans[0] += u1-u2
                    if c1+1 < ls[p1]:
                        c1 += 1
                    else:
                        s1 += ps[p1][-1]
                        p1 += 1; c1 = 0
                return su
            None if list(map(lambda _:0,[evaluate(0)])) else 0
            stdout_write.write("%d\n"%ans[0])
            return True
        if not solve(): break
main()