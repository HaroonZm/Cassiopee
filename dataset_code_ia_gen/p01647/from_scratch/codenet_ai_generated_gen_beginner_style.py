def rank_to_value(rank):
    if rank == 'A':
        return 14
    if rank == 'K':
        return 13
    if rank == 'Q':
        return 12
    if rank == 'J':
        return 11
    if rank == 'T':
        return 10
    return int(rank)

def get_all_combinations(cards, n):
    # simple combinations without import
    result = []
    def backtrack(start, path):
        if len(path) == n:
            result.append(path[:])
            return
        for i in range(start, len(cards)):
            path.append(cards[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return result

def count_ranks(cards):
    counts = {}
    for card in cards:
        r = card[1]
        counts[r] = counts.get(r, 0) + 1
    return counts

def count_suits(cards):
    counts = {}
    for card in cards:
        s = card[0]
        counts[s] = counts.get(s, 0) + 1
    return counts

def is_straight(ranks):
    ranks = sorted(set(ranks), reverse=True)
    # normal straight
    for i in range(len(ranks)-4):
        if ranks[i] - ranks[i+4] == 4:
            return ranks[i]
    # special case A 5 4 3 2
    if set([14,5,4,3,2]).issubset(ranks):
        return 5
    return None

def hand_rank(cards):
    # cards: list of 5 cards
    # returns (score, tiebreak list)
    # higher score means stronger hand
    # scores: 9=Royal Flush,8=Straight Flush,7=Four Kind,6=Full House,5=Flush,
    # 4=Straight,3=Three Kind,2=Two Pairs,1=One Pair,0=High Card
    ranks_str = [c[1] for c in cards]
    suits = [c[0] for c in cards]
    ranks_val = [rank_to_value(r) for r in ranks_str]
    ranks_val.sort(reverse=True)

    # count suits and ranks
    suits_count = count_suits(cards)
    ranks_count = count_ranks(cards)

    flush = False
    flush_suit = None
    for s, cnt in suits_count.items():
        if cnt >= 5:
            flush = True
            flush_suit = s
            break

    ranks_val_set = sorted(set(ranks_val), reverse=True)
    straight_high = is_straight(ranks_val)
    # check for flush cards
    flush_cards = []
    if flush:
        flush_cards = [rank_to_value(c[1]) for c in cards if c[0] == flush_suit]
        flush_cards.sort(reverse=True)
    # straight flush
    if flush:
        flush_cards_unique = sorted(set(flush_cards), reverse=True)
        sf_high = is_straight(flush_cards_unique)
        if sf_high is not None:
            # royal flush
            if sf_high == 14:
                return (9, [])
            else:
                return (8, [sf_high])
    # Four of a kind
    quad = None
    for r, cnt in ranks_count.items():
        if cnt == 4:
            quad = rank_to_value(r)
            break
    if quad is not None:
        other = [rank_to_value(r) for r in ranks_str if rank_to_value(r) != quad]
        other.sort(reverse=True)
        return (7, [quad] + other[:1])
    # Full house
    trips = []
    pairs = []
    for r, cnt in ranks_count.items():
        if cnt == 3:
            trips.append(rank_to_value(r))
        elif cnt == 2:
            pairs.append(rank_to_value(r))
    trips.sort(reverse=True)
    pairs.sort(reverse=True)
    if len(trips) >= 1 and (len(pairs) >= 1 or len(trips) >= 2):
        if len(trips) >= 2:
            # use highest for trips, second highest for pairs
            return (6, [trips[0], trips[1]])
        else:
            return (6, [trips[0], pairs[0]])
    # flush
    if flush:
        return (5, flush_cards[:5])
    # straight
    if straight_high is not None:
        return (4, [straight_high])
    # three of a kind
    if len(trips) >= 1:
        rest = [rank_to_value(r) for r in ranks_str if rank_to_value(r) != trips[0]]
        rest.sort(reverse=True)
        return (3, [trips[0]] + rest[:2])
    # two pairs
    if len(pairs) >= 2:
        highpair = pairs[0]
        lowpair = pairs[1]
        rest = [rank_to_value(r) for r in ranks_str if rank_to_value(r) != highpair and rank_to_value(r) != lowpair]
        rest.sort(reverse=True)
        return (2, [highpair, lowpair] + rest[:1])
    # one pair
    if len(pairs) == 1:
        pair = pairs[0]
        rest = [rank_to_value(r) for r in ranks_str if rank_to_value(r) != pair]
        rest.sort(reverse=True)
        return (1, [pair] + rest[:3])
    # high card
    ranks_val.sort(reverse=True)
    return (0, ranks_val[:5])

def best_hand(cards):
    # from 7 cards choose best 5 cards
    best = (-1, [])
    combs = get_all_combinations(cards, 5)
    for comb in combs:
        r = hand_rank(comb)
        if r > best:
            best = r
    return best

def compare_hand(a, b):
    # a,b are tuples (score, list)
    if a[0] != b[0]:
        return 1 if a[0] > b[0] else -1
    # special case royal flush tie: considered tie always
    if a[0] == 9:
        return 0
    # compare tiebreak list one by one
    for i in range(min(len(a[1]), len(b[1]))):
        if a[1][i] > b[1][i]:
            return 1
        elif a[1][i] < b[1][i]:
            return -1
    if len(a[1]) > len(b[1]):
        return 1
    elif len(a[1]) < len(b[1]):
        return -1
    return 0

def all_cards():
    suits = ['S','H','D','C']
    ranks = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    cards = []
    for s in suits:
        for r in ranks:
            cards.append(s+r)
    return cards

def solve():
    import sys
    all_52 = all_cards()
    lines = sys.stdin.read().strip('\n').split('\n')
    i = 0
    while i < len(lines):
        if lines[i].startswith('#'):
            break
        you_cards = lines[i].split()
        i += 1
        opp_cards = lines[i].split()
        i += 1
        comm_cards = lines[i].split()
        i += 1
        known_cards = you_cards + opp_cards + comm_cards
        deck_left = [c for c in all_52 if c not in known_cards]
        wins = 0
        total = 0
        for j in range(len(deck_left)):
            for k in range(j+1, len(deck_left)):
                turn = deck_left[j]
                river = deck_left[k]
                board = comm_cards + [turn, river]
                you_best = best_hand(you_cards + board)
                opp_best = best_hand(opp_cards + board)
                cmp = compare_hand(you_best, opp_best)
                if cmp == 1:
                    wins += 1
                total += 1
        if total == 0:
            prob = 0.0
        else:
            prob = wins/total
        print(prob)

if __name__ == '__main__':
    solve()