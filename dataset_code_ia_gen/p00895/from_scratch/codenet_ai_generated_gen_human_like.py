import sys

directions = [
    (0,1), (0,-1), (1,0), (-1,0),
    (1,1), (1,-1), (-1,1), (-1,-1)
]

def get_sequence(grid, h, w, x, y, dx, dy, length):
    seq = []
    for i in range(length):
        nx = (x + dx*i) % h
        ny = (y + dy*i) % w
        seq.append(grid[nx][ny])
    return "".join(seq)

def no_overlap(length, h, w, dx, dy):
    # The maximum length of non-self-overlapping sequence in direction (dx,dy)
    # is limited by the minimal period before returning to start.
    # Because grid is torus, the distance to overlap can be found by
    # finding the minimal k>0 such that (k*dx)%h==0 and (k*dy)%w==0.
    k = 1
    while True:
        if (dx*k)%h == 0 and (dy*k)%w == 0:
            return k
        k += 1

def max_len_no_overlap(h, w, dx, dy):
    # compute minimal positive k such that (k*dx)%h==0 and (k*dy)%w==0
    # that is the minimal length before sequence overlaps itself
    # we want maximal length = minimal k
    if dx == 0 and dy == 0:
        return 0
    if dx == 0:
        # minimal k such that (0)%h=0 always true, and (k*dy)%w=0
        g = gcd(w, abs(dy))
        return w//g
    if dy == 0:
        g = gcd(h, abs(dx))
        return h//g
    # general case
    gh = h // gcd(h, abs(dx))
    gw = w // gcd(w, abs(dy))
    # minimal k such that k%gh==0 and k%gw==0 -> lcm(gh,gw)
    l = lcm(gh,gw)
    return l

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def find_longest_spell(grid, h, w):
    found = {}
    max_len = 0
    results = set()
    for x in range(h):
        for y in range(w):
            for dx, dy in directions:
                max_len_dir = max_len_no_overlap(h, w, dx, dy)
                # minimal length is 2
                for length in range(2, max_len_dir+1):
                    s = get_sequence(grid, h, w, x, y, dx, dy, length)
                    # To satisfy two sequences do not overlap themselves,
                    # length must be <= max_len_dir
                    # Save all found strings with their counts
                    found.setdefault(s, set()).add((x,y,dx,dy))

    # We must check strings that appear more than once with different (start or direction)
    # allowing shared squares between two sequences, but sequences themselves no overlap.
    # So count how many distinct (x,y,dx,dy) appear for each string
    # Actually done in found dict.

    # Select those with at least 2 distinct positions/directions
    candidates = [s for s, spots in found.items() if len(spots) > 1]

    if not candidates:
        return "0"
    # longest length strings only
    longest_len = max(len(s) for s in candidates)
    longest_candidates = [s for s in candidates if len(s) == longest_len]
    # lex smallest
    spell = min(longest_candidates)
    return spell

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        h,w = map(int,line.split())
        if h == 0 and w == 0:
            break
        grid = [input().strip() for _ in range(h)]
        ans = find_longest_spell(grid, h, w)
        print(ans)

if __name__ == "__main__":
    main()