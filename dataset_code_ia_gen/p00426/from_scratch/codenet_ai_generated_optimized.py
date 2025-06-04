import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        # Read trays
        trays = [[], [], []]
        for i in range(3):
            line = list(map(int, input().split()))
            k = line[0]
            cups = line[1:]
            # cups are sorted ascending bottom->top, we need bottom->top order, so keep as is
            trays[i] = cups

        # We need to represent the state: for each cup (1..n), which tray it's on.
        # The problem states the cups in each tray are stacked smallest at bottom to largest at top.
        # The top cup = largest cup in that tray (last element in trays[i])
        # To know position of each cup, reconstruct from trays.

        pos = [0]*(n+1)  # cup -> tray
        for i in range(3):
            for c in trays[i]:
                pos[c] = i

        # Represent state as a base-3 number: for cup 1..n, pos[cup]*3^(cup-1)
        # Because n <= 15, this fits in an int64
        def encode(state_pos):
            code = 0
            for i in range(1, n+1):
                code += state_pos[i] * (3**(i-1))
            return code

        start = encode(pos)

        # The goal is to have all cups on tray 0 or all cups on tray 2
        # That means state where all pos[cup] == 0 or all pos[cup] == 2
        # Because any cup's position is in {0,1,2}, checking goal is quick.

        # Allowed moves according to the rules:
        # Move top cup from a tray to another tray, only if:
        # - moving cup is top of source tray (largest cup on that tray)
        # - no smaller cup on destination tray (rule 2)
        # - only moves between A<->B and B<->C allowed, no direct A->C or C->A

        # So moves allowed:
        # A->B, B->A, B->C, C->B only

        # We can implement BFS from start state until find goal or exceed m moves.

        # Precompute powers of 3
        power3 = [1]*(n+1)
        for i in range(1, n+1):
            power3[i] = power3[i-1]*3

        def decode(code):
            arr = [0]*(n+1)
            tmp = code
            for i in range(1, n+1):
                arr[i] = tmp % 3
                tmp //=3
            return arr

        # move function: given state code, returns list of next states by one valid move
        def next_states(code):
            arr = decode(code)
            tops = [-1]*3  # index of top cup (largest cup) per tray
            # Find cups in each tray
            cups_on_tray = [[] for _ in range(3)]
            for c in range(1, n+1):
                cups_on_tray[arr[c]].append(c)
            # top cup per tray = max cup number in that tray, or -1 if empty
            for i in range(3):
                if cups_on_tray[i]:
                    tops[i] = max(cups_on_tray[i])

            # Moves allowed (from,tray,to tray)
            moves = [(0,1),(1,0),(1,2),(2,1)]
            res = []
            for f,t in moves:
                if tops[f] == -1:
                    continue
                c = tops[f]  # cup to move
                # Rule 2: Cannot put smaller cup on bigger cup
                # Check if destination tray empty or top cup in t is larger than c
                if tops[t] == -1 or tops[t] > c:
                    # Move cup c from f to t
                    new_arr = arr[:]
                    new_arr[c] = t
                    new_code = 0
                    for i in range(1, n+1):
                        new_code += new_arr[i]*power3[i-1]
                    res.append(new_code)
            return res

        # Check if all cups on tray A or all on tray C
        def is_goal(code):
            arr = decode(code)
            allA = all(x==0 for x in arr[1:])
            if allA:
                return True
            allC = all(x==2 for x in arr[1:])
            return allC

        from collections import deque

        visited = {}
        visited[start] = 0
        que = deque([start])

        ans = -1
        while que:
            cur = que.popleft()
            dist = visited[cur]
            if dist > m:
                break
            if is_goal(cur):
                ans = dist
                break
            for nxt in next_states(cur):
                if nxt not in visited or visited[nxt] > dist+1:
                    visited[nxt] = dist+1
                    que.append(nxt)

        print(ans)

if __name__ == "__main__":
    solve()