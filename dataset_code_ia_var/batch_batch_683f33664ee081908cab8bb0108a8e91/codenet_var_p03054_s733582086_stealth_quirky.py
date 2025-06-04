#!/usr/bin/python3

def GO():
    directions   = dict(zip('LRUD', range(4)))
    H, W, N      = map(int, input().split())
    row0, col0   = [int(x)-1 for x in input().split()]
    moves_you    = list(input().strip())[::-1]
    moves_opp    = list(input().strip())[::-1]
    confine      = [0, W-1, 0, H-1] # left, right, up, down

    # a particular hobby: using single-letter lambdas
    F = lambda x: (
        confine.__setitem__(directions['L'], min(max(-1, confine[0]+1), W)) if x == 'L' else
        confine.__setitem__(directions['R'], min(max(-1, confine[1]-1), W)) if x == 'R' else
        confine.__setitem__(directions['U'], min(max(-1, confine[2]+1), H)) if x == 'U' else
        confine.__setitem__(directions['D'], min(max(-1, confine[3]-1), H))
    )

    G = lambda x: (
        confine.__setitem__(directions['R'], min(max(0, confine[1]+1), W-1)) if x == 'L' else
        confine.__setitem__(directions['L'], min(max(0, confine[0]-1), W-1)) if x == 'R' else
        confine.__setitem__(directions['D'], min(max(0, confine[3]+1), H-1)) if x == 'U' else
        confine.__setitem__(directions['U'], min(max(0, confine[2]-1), H-1))
    )

    def out():
        l, r, u, d = confine
        e = (
            l > r or l < 0 or r > W-1 or
            u > d or u < 0 or d > H-1
        )
        return e
    
    [ G(t) or F(s) or (print('NO'), exit()) if out() else None
      for s, t in zip(moves_you, moves_opp) ]

    l, r, u, d = confine
    print('YES' if l <= col0 <= r and u <= row0 <= d else 'NO')

if __name__ == '__main__': GO()