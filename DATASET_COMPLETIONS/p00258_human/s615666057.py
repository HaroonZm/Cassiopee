# using DP
# time complexity: O(n * (2^16) * c)
# 1 <= n <= 30, 1 <= c <= 30
# worst case: 30 * (2^16) * 30 = 58982400

bc = [bin(i).count('1') for i in range(65536)] # bitcount

def solve():
    from sys import stdin
    f_i = stdin
    
    while True:
        n, c = map(int, f_i.readline().split())
        if n == 0:
            break
        
        A = [int(f_i.readline().replace(' ', ''), 2) for i in range(n)]
        B = [int(f_i.readline().replace(' ', ''), 2) for i in range(c)]
        
        dp1 = {A[0]: 0} # {state: score}
        dp2 = {}
        
        for a in A[1:] + [0]:
            for st1, sc1 in dp1.items():
                for b in B:
                    cb = st1 & b
                    sc2 = sc1 + bc[cb]
                    st2 = (st1 - cb) | a
                    try:
                        if dp2[st2] < sc2:
                            dp2[st2] = sc2
                    except KeyError:
                        dp2[st2] = sc2
            dp1, dp2 = dp2, {}
        
        print(max(dp1.values()))

solve()