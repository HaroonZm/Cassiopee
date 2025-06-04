import sys
from collections import Counter

def can_form_sets(counts, sets_needed):
    if sets_needed == 0:
        return True
    for num in range(1,10):
        # Triple identical
        if counts[num] >= 3:
            counts[num] -= 3
            if can_form_sets(counts, sets_needed -1):
                counts[num] += 3
                return True
            counts[num] +=3
        # Triple consecutive
        if num <= 7:
            if counts[num]>=1 and counts[num+1]>=1 and counts[num+2]>=1:
                counts[num]-=1
                counts[num+1]-=1
                counts[num+2]-=1
                if can_form_sets(counts, sets_needed -1):
                    counts[num]+=1
                    counts[num+1]+=1
                    counts[num+2]+=1
                    return True
                counts[num]+=1
                counts[num+1]+=1
                counts[num+2]+=1
    return False

def can_complete_puzzle(s):
    orig_counts = Counter(int(c) for c in s)
    res = []
    for add_num in range(1,10):
        if orig_counts[add_num]==4:
            continue
        counts = orig_counts.copy()
        counts[add_num]+=1
        # find pairs
        for p in range(1,10):
            if counts[p]>=2:
                counts[p]-=2
                if can_form_sets(counts,4):
                    res.append(str(add_num))
                    counts[p]+=2
                    break
                counts[p]+=2
    if res:
        return ' '.join(res)
    else:
        return '0'

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    print(can_complete_puzzle(line))