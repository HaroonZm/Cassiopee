import sys
sys.setrecursionlimit(10**7)

s = sys.stdin.readline().strip()
n = len(s)

from functools import lru_cache

@lru_cache(None)
def is_cat(l, r):
    if l > r:
        return True
    if r - l + 1 < 4:
        return False
    if s[l] != 'm' or s[r] != 'w':
        return False
    for mid1 in range(l+1, r-1):
        if s[mid1] == 'e':
            for mid2 in range(mid1+1, r):
                if is_cat(l+1, mid1-1) and is_cat(mid1+1, mid2-1) and s[mid2] == 'w':
                    if mid2 == r:
                        return True
    # The above loop checks possible split points where 'e' and 'w' fit cat structure
    # But as per definition last character has to be 'w', so let's adjust:
    # Actually, from BNF: 'm' + X + 'e' + Y + 'w'
    # So after 'm', X ends at position before 'e', then Y is between 'e'+1 and before last 'w'

    # So better to try all positions of 'e' and 'w' to split properly
    # Let's rewrite:

def is_cat_dp(l, r):
    if l > r:
        return True
    length = r - l + 1
    if length < 4:  # min length for 'm' + "" + 'e' + "" + 'w' is 4
        return False
    if s[l] != 'm' or s[r] != 'w':
        return False
    for e_pos in range(l+1, r-1):
        if s[e_pos] != 'e':
            continue
        # X = s[l+1:e_pos], Y = s[e_pos+1:r]
        if is_cat(l+1, e_pos-1) and is_cat(e_pos+1, r-1):
            return True
    return False

is_cat = lru_cache(None)(is_cat_dp)

print("Cat" if is_cat(0, n-1) else "Rabbit")