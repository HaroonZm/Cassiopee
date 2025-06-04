import sys

value_map = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13}
suit_map = {'S':0,'C':1,'H':2,'D':3}

def hand_score(hand, base_points, multipliers):
    vals = [value_map[c[0]] for c in hand]
    suits = [suit_map[c[1]] for c in hand]
    base_sum = sum(base_points[s][v-1] for s,v in zip(suits, vals))
    if base_sum == 0:
        return 0
    from collections import Counter
    c_val = Counter(vals)
    c_suit = Counter(suits)
    counts = sorted(c_val.values(), reverse=True)
    distinct_vals = len(c_val)
    sorted_vals = sorted(vals)
    unique_vals = sorted(c_val)
    is_flush = (len(c_suit) == 1)
    def is_straight(vs):
        # check if consecutive values
        return all(vs[i]+1 == vs[i+1] for i in range(4))
    normal_straight = (distinct_vals ==5 and is_straight(sorted_vals))
    royal = set([10,11,12,13,1])
    royal_straight = set(vals) == royal
    # Determine rank index for multipliers
    # Rankings: 0=1 pair,1=2 pair,2=3 of a kind,3=straight,4=flush,5=full house,6=4 of a kind,7=straight flush,8=royal flush
    rank = -1
    if royal_straight and is_flush:
        rank = 8
    elif normal_straight and is_flush:
        rank = 7
    elif counts[0] == 4:
        rank = 6
    elif counts[0] == 3 and counts[1] == 2:
        rank = 5
    elif is_flush:
        rank = 4
    elif normal_straight:
        rank = 3
    elif counts[0] == 3:
        rank = 2
    elif counts[0] == 2 and counts[1] == 2:
        rank = 1
    elif counts[0] == 2:
        rank = 0
    else:
        return 0
    return base_sum * multipliers[rank]

first = True
lines = sys.stdin.read().strip().split('\n')
i=0
while i < len(lines):
    if lines[i].strip()=='':
        i+=1
        continue
    N = int(lines[i])
    i+=1
    if i+4+1+N-1>len(lines):
        break
    base_points=[]
    for _ in range(4):
        base_points.append(list(map(int,lines[i].split())))
        i+=1
    multipliers = list(map(int,lines[i].split()))
    i+=1
    if not first:
        print()
    first=False
    for _ in range(N):
        hand = lines[i].split()
        i+=1
        print(hand_score(hand, base_points, multipliers))