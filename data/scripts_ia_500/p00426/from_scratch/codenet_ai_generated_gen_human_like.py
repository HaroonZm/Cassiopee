import sys
from collections import deque

def encode_state(pos_list):
    """Encode position list to an integer state. Each cup position uses 2 bits:
    0 => A, 1 => B, 2 => C
    """
    state = 0
    for i, p in enumerate(pos_list):
        state |= p << (2 * i)
    return state

def decode_state(state, n):
    pos_list = []
    for i in range(n):
        pos_list.append((state >> (2 * i)) & 3)
    return pos_list

def get_top_cups(state, n):
    """Return a list of length 3, each element is the smallest cup number (index) on the tray top, or None."""
    pos = decode_state(state, n)
    # cups sorted by size (index ascending => smaller cup)
    # For each tray, find the top cup (largest cup number on that tray)
    top = [None, None, None]
    for c in range(n-1, -1, -1):
        tray = pos[c]
        if top[tray] is None:
            top[tray] = c
    return top

def solve(n, m, tray_lists):
    # tray_lists: [A_list, B_list, C_list], each sorted ascending cups on that tray (smallest at bottom)
    # We want to find min moves to have all cups on A or on C only.

    # Build initial position list for each cup index 0-based
    pos = [0]*n
    # tray_lists ordered by A,B,C (tray 0,1,2)
    # tray_lists have increasing cup size, smallest bottom, largest top, so last item in list is top
    for tray_idx, cups in enumerate(tray_lists):
        for c in cups:
            pos[c-1] = tray_idx

    start_state = encode_state(pos)
    # goal states: all cups on A (0) or all on C (2)
    goalA = 0
    goalC = 0
    for i in range(n):
        goalA |= 0 << (2 * i)
        goalC |= 2 << (2 * i)

    if start_state == goalA or start_state == goalC:
        return 0

    # Allowed direct moves:
    # A<->B, B<->C only.
    # So moves are edges between trays: (0<->1), (1<->2)
    # but not (0<->2)

    # For BFS, visited set
    visited = set()
    visited.add(start_state)
    q = deque()
    q.append((start_state, 0))

    while q:
        state, dist = q.popleft()
        if dist >= m:
            continue
        top = get_top_cups(state, n)
        pos = decode_state(state, n)
        # try moves:

        # For each tray pair with allowed moves
        # move from tray s to tray t, moving top cup from s if it exists, onto t if rules permit
        # pairs: (A,B), (B,A), (B,C), (C,B)
        for (s,t) in [(0,1),(1,0),(1,2),(2,1)]:
            scup = top[s]
            if scup is None:
                continue
            # check top cup of t to see if can move scup on t
            tcup = top[t]
            # Rule 2: no smaller cup above a bigger cup
            # cups are ordered by indices: smaller index is smaller cup, so we can only put bigger cup on smaller cup
            # moving cup scup onto tray t is allowed if:
            # t empty or scup > tcup (because bigger cups are on top)
            if tcup is None or scup > tcup:
                # move scup cup from s to t
                new_pos = pos[:]
                new_pos[scup] = t
                new_state = encode_state(new_pos)
                if new_state not in visited:
                    if new_state == goalA or new_state == goalC:
                        return dist + 1
                    visited.add(new_state)
                    q.append((new_state, dist + 1))
    return -1

def main():
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = input()
            if not line:
                return
        n,m = map(int,line.split())
        if n == 0 and m == 0:
            break

        tray_lists = []
        for _ in range(3):
            while True:
                line = input()
                if line.strip() != '':
                    break
            arr = list(map(int,line.strip().split()))
            k = arr[0]
            cups = []
            if k>0:
                # cups are given in ascending order: smallest bottom, largest top
                cups = arr[1:]
            tray_lists.append(cups)

        ans = solve(n,m,tray_lists)
        print(ans)

if __name__ == '__main__':
    main()