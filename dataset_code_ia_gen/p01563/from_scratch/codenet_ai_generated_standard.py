import sys
sys.setrecursionlimit(10**7)
R,C=map(int,input().split())
S=[input() for _ in range(R)]

dp=[{} for _ in range(R+1)]
# dp[i][mask]: for row i, mask is the columns occupied by letters,
# stores max score achievable after placing first i rows.

def adj_points(c, mask):
    # number of adjacent pairs inside this row for char c in mask
    # count number of adjacent bits set in mask to get points for c in this row
    res=0
    cur=(mask&(mask>>1))
    while cur:
        res+=1
        cur&=cur-1
    return res*2

def common_points(c, mask1, mask2):
    # points due to vertical adjacents for char c between rows mask1 and mask2
    return bin(mask1&mask2).count('1')*2

from collections import defaultdict

# Precompute for each row all possible placements with their masks by letter and intra-row points
row_pos = []
for i in range(R):
    s = S[i]
    length=len(s)
    positions = defaultdict(list) # char: list of masks with that char placed
    # Generate all masks picking length positions increasing order
    # We generate masks with exactly length bits set in positions [0..C-1] and keep order for letters
    def gen(pos,start,mask):
        if pos==length:
            # Calculate intra-row points
            pts=0
            chars={}
            for idx,ch in enumerate(s):
                if ch not in chars:
                    chars[ch]=0
                chars[ch]|= (1<<((mask >> idx)&15)) # mask stores columns in order?
            # above approach wrong, fix:
            # we stored mask as bitmask over columns, need mapping letters to columns:
            # Let's store mask as bitmask of columns where chars placed, but letters order must be kept
            # So better generate masks as subsets of columns with length bits set preserving order idx->col
            # We'll store mask as integer bits of columns
            pass

    # Instead of complicating, generate combinations of positions for letters in s's order
    from itertools import combinations
    from collections import Counter

    combos=[]
    for cols in combinations(range(C),length):
        # place s letters in these columns
        mask=0
        for c_ in cols:
            mask|=(1<<c_)
        combos.append(mask)
    # For each mask, compute intra-row points:
    # count pairs of adjacent letters equal, sum adjacency points
    # need to know character placement mask per character for this row
    # So for this mask, store mask per char
    per_char_masks=defaultdict(int)
    for idx,ch in enumerate(s):
        per_char_masks[ch]|=(1<<(cols[idx]))
    chars_masks = list(per_char_masks.items())
    # intra points: sum over chars each adjacency inside mask, pairs adjacent bits set
    pts=0
    for ch,m in chars_masks:
        # count pairs of adjacent bits in m
        pts+=bin(m & (m>>1)).count('1')*2
    row_pos.append([(mask, per_char_masks, pts) for mask in combos])

# dp initialization
dp[0][0]=0

for i in range(R):
    for prev_mask in dp[i]:
        prev_score=dp[i][prev_mask]
        for mask, per_char_masks, intra_pts in row_pos[i]:
            # Check letters order increasing not needed, generated in order
            # sum vertical adjacency points with previous row: for each char in both rows intersection
            
            vert_pts=0
            # prev_mask and mask are single masks of columns occupied in prev and current row respectively,
            # but per_char_masks contains masks per character for current row
            # We need per_char_masks for previous row, but dp only stores total mask
            # Adjust approach:
            # We must store per_char_masks in dp states per row to compute vertical adjacency
            # Since dp state is too big to store per_char_masks, simplify:
            # Store dp states keyed by tuple(per_char_masks) or similar? Memory explosion
            # Instead, for each row store all possible placements
            # So dp state tracks per_char_masks by row
            # We do this now by storing dp as dict keyed by tuple of (mask_c, mask_o, mask...) for chars? Not feasible.
            # Instead, let's do:
            # We can store only mask of occupied columns per row in dp key
            # At transition, we try to maximize score by combining placements of current and previous rows, add vertical adjacency only when letters coincide
            # But we don't know letter assignments in dp state
            # Therefore use a different approach:
            # Since C <=16, R <=128, and |s_i|<=C, total of letters are small
            # Try store for each row a list of possible placements: mask and per_char_masks
            # Then DP for i-th row: for each placement in row i, for each placement in i-1
            # and check vertical adjacency per char: sum of popcount of per_char_masks[char]_i & per_char_masks[char]_{i-1}
            # Speed should be ok since total combos per row ~ C choose |s_i| <= 2^16 worst (64k)
            # We can try prune combos or optimize
            # Let's implement DP between rows storing all combos

ans=0
from collections import defaultdict

prev_row = row_pos[0]
dp = defaultdict(int)
for mask, per_char_masks, intra_pts in prev_row:
    dp[(mask, tuple(sorted(per_char_masks.items())))] = intra_pts
for i in range(1,R):
    ndp = defaultdict(int)
    curr_row = row_pos[i]
    for mask2, per_char_masks2, intra_pts2 in curr_row:
        for (mask1, pcms1), val in dp.items():
            # compute vertical adjacency points
            pcms1 = dict(pcms1)
            vert_pts=0
            for ch in per_char_masks2:
                if ch in pcms1:
                    vert_pts+=bin(per_char_masks2[ch] & pcms1[ch]).count('1')*2
            score=val + intra_pts2 + vert_pts
            key=(mask2, tuple(sorted(per_char_masks2.items())))
            if score>ndp.get(key,0):
                ndp[key] = score
    dp=ndp
ans=max(dp.values())
print(ans)