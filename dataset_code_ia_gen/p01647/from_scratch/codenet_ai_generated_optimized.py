from sys import stdin
from math import comb

rank_str = '23456789TJQKA'
rank_val = {r: i for i, r in enumerate(rank_str, 2)}  # 2..14
# For sorting and ranking, Ace high is 14 and low is 1 in straights (special case)

def card_to_tuple(c):
    return (c[0], rank_val[c[1]])

def get_deck():
    suits = 'SHDC'
    ranks = rank_str
    return [(s,r) for s in suits for r in range(2,15)]

def hand_rank(cards):
    # cards is list of 5 (suit, rank_int)
    # returns (category_int, rank_key_tuple)
    # category_int: 9=Royal Flush, 8=Straight Flush, 7=Four,6=Full House,5=Flush,4=Straight,3=Three,2=Two Pairs,1=One Pair,0=High Card
    # rank_key_tuple used for tie breaking

    counts = {}
    suits = {}
    ranks = []
    for s,r in cards:
        counts[r] = counts.get(r,0)+1
        suits[s] = suits.get(s,0)+1
        ranks.append(r)
    ranks.sort(reverse=True)

    # Check flush
    flush = None
    for s in suits:
        if suits[s]>=5:
            flush = s
            break

    # Check straight
    # ranks distinct descending order
    distinct = sorted(set(ranks), reverse=True)
    straight_high = None
    # Special ace-low straight check: A-2-3-4-5 -> ranks 14,5,4,3,2 treat ace as 1
    vals = distinct[:]
    if 14 in vals:
        vals.append(1)
        vals = sorted(set(vals), reverse=True)
    for i in range(len(vals)-4):
        if vals[i] - vals[i+4] == 4:
            straight_high = vals[i]
            break

    # Check straight flush (and royal flush)
    if flush is not None:
        flush_ranks = sorted([r for (s,r) in cards if s==flush], reverse=True)
        flush_distinct = []
        last = -1
        for fr in flush_ranks:
            if fr != last:
                flush_distinct.append(fr)
                last = fr
        # ace-low for flush
        if 14 in flush_distinct:
            flush_distinct.append(1)
            flush_distinct = sorted(set(flush_distinct), reverse=True)
        for i in range(len(flush_distinct)-4):
            if flush_distinct[i]-flush_distinct[i+4]==4:
                if flush_distinct[i]==14:
                    # royal flush
                    return (9, ())
                else:
                    return (8, (flush_distinct[i],))
    # Four of a kind, full house, three, pairs detection
    count_values = sorted(counts.values(), reverse=True)
    sorted_by_count = sorted(((cnt,rk) for rk,cnt in counts.items()), reverse=True)
    # sorted_by_count ordered by count desc then rank desc
    # separated by counts for rank info:
    quads = [rk for cnt,rk in sorted_by_count if cnt==4]
    triples = [rk for cnt,rk in sorted_by_count if cnt==3]
    pairs = [rk for cnt,rk in sorted_by_count if cnt==2]
    singles = [rk for cnt,rk in sorted_by_count if cnt==1]

    if quads:
        # four of kind: compare quad rank then remaining card highest
        quad = quads[0]
        rest = sorted([r for r in ranks if r!=quad], reverse=True)
        return (7, (quad, rest[0]))
    if triples and pairs:
        # full house triple then pair
        triple = triples[0]
        pair = pairs[0]
        return (6, (triple, pair))
    if flush is not None:
        # flush: just sort flush cards descending
        flush_cards = sorted([r for s,r in cards if s==flush], reverse=True)
        return (5, tuple(flush_cards[:5]))
    if straight_high is not None:
        return (4, (straight_high,))
    if triples:
        triple = triples[0]
        rest = sorted([r for r in ranks if r!=triple], reverse=True)
        return (3, (triple, rest[0], rest[1]))
    if len(pairs)>=2:
        highp, lowp = pairs[0], pairs[1]
        rest = sorted([r for r in ranks if r!=highp and r!=lowp], reverse=True)
        return (2, (highp, lowp, rest[0]))
    if len(pairs)==1:
        pair = pairs[0]
        rest = sorted([r for r in ranks if r!=pair], reverse=True)
        return (1, (pair, rest[0], rest[1], rest[2]))
    return (0, tuple(ranks[:5]))

from itertools import combinations

def best_hand(cards7):
    best = None
    for combi in combinations(cards7,5):
        r = hand_rank(combi)
        if best is None or r>best:
            best = r
    return best

def read_cards(line):
    return [card_to_tuple(c) for c in line.strip().split()]

def main():
    lines = iter(stdin.read().strip().split('\n'))
    while True:
        try:
            yours_line = next(lines)
            if yours_line.strip() == '#':
                break
            mine = read_cards(yours_line)
            opponent = read_cards(next(lines))
            flop = read_cards(next(lines))
        except StopIteration:
            break
        known_cards = set(mine+opponent+flop)
        deck = get_deck()
        rem_cards = [c for c in deck if c not in known_cards]
        wins = 0
        total = 0
        for combi in combinations(rem_cards,2):
            community = flop + list(combi)
            my_best = best_hand(mine+community)
            opp_best = best_hand(opponent+community)
            if my_best > opp_best:
                wins += 1
            total += 1
        print(wins/total if total>0 else 0)

if __name__=="__main__":
    main()