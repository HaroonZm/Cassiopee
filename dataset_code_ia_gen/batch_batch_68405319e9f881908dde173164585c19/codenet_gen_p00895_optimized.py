import sys
sys.setrecursionlimit(10**7)

directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

def get_seq(grid, h, w, r, c, dr, dc, length):
    seq = []
    for k in range(length):
        rr = (r + dr*k) % h
        cc = (c + dc*k) % w
        seq.append(grid[rr][cc])
    return ''.join(seq)

def has_self_overlap(seq, length):
    # Check if it can be split into repeats of substring of length d<length
    # Because of wrapping, the square sequence must not overlap itself,
    # so length must be <= half of the length to avoid overlap
    # But exact definition: no overlapping squares in the sequence itself
    # We consider no repeated positions in the sequence
    # Since the donut wraps, max length of non-self-overlapping seq is minimal period length
    # But the prompt says the sequences cannot overlap themselves;
    # length > half the dimension * 2? To keep simple,
    # self-overlap means that the repetition is shorter than length
    # So we exclude sequences that are formed by repeating smaller sequences multiple times
    # Actually, we must confirm that sequence doesn't repeat itself within length:
    # so check for periodicity:
    for sublen in range(1,length//2+1):
        if length % sublen != 0:
            continue
        if seq == seq[:sublen]*(length//sublen):
            return True
    return False

def solve_grid(h,w,grid):
    max_len = min(h,w)*max(2,max(h,w)) + 20  # upper bound sufficiently large
    # Because sequences wrap, length can be more than h or w
    # but the sequence can't overlap itself:
    # So max length is at most h*w (but checking that is expensive)
    # Use max length = lcm of h and w *2 or so is overkill.
    # According to problem constraints, 10*20=200 max cells,
    # and sequences can't overlap themselves, so max length <= h*w
    
    # We'll check lengths from longest possible down to 2
    max_search_len = h*w
    found = []
    # Precompute sequences for all starting points, directions and lengths
    # To do this efficiently, we store sequences in a dict length-> dict seq -> list of (r,c,d)
    # But memory can be large; so just do checking length from max_search_len down to 2,
    # and for each length we find sequences with count>1, respecting non-self-overlapping,
    # and pick lex smallest and return.
    
    # To speed up counting sequences, we can store sequences in dictionary and count.
    for length in range(max_search_len,1,-1):
        counter = {}
        for r in range(h):
            for c in range(w):
                for dr,dc in directions:
                    seq = get_seq(grid,h,w,r,c,dr,dc,length)
                    # Check self-overlap:
                    # If sequence doesn't have repeated positions, no overlap
                    # From problem's examples and constraints:
                    # The sequences are not allowed if they overlap themselves, e.g. periodic sequences
                    if has_self_overlap(seq,length):
                        continue
                    counter[seq] = counter.get(seq,0)+1
        candidates = [s for s,count in counter.items() if count>1]
        if candidates:
            return min(candidates)
    return "0"

def main():
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip()=='':
            line = input()
            if not line:
                return
        h,w = map(int,line.strip().split())
        if h==0 and w==0:
            break
        grid = [input().strip() for _ in range(h)]
        print(solve_grid(h,w,grid))

if __name__=="__main__":
    main()