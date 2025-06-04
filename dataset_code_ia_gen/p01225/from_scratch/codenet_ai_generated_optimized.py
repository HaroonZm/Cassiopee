from sys import stdin
from collections import Counter

def can_form_sets(cards):
    # cards: list of (num,color)
    # goal: partition cards into 3 sets, each set is 3 cards
    # each set: same color, and numbers either all same OR consecutive
    cards.sort(key=lambda x: (x[1], x[0]))
    # group cards by color
    color_groups = {'R': [], 'G': [], 'B': []}
    for n,c in cards:
        color_groups[c].append(n)

    # for each color try to form sets
    # total sets must be 3
    # we try all partitions of triple sets to colors summing up to 9 cards (3*3)
    # since only 3 sets possible, and each color group len<=9,
    # try all ways to pick sets from group
    # backtracking per color group is easier.

    # For all colors, get all possible sets (triplets) that are valid.
    # Each set is indices in that group's list.
    # Then search for 3 sets that cover all cards.

    sets_by_color = {}
    for c in 'RGB':
        arr = color_groups[c]
        n = len(arr)
        sets_c = []
        # find all valid triplets (i<j<k)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    triple = [arr[i], arr[j], arr[k]]
                    triple.sort()
                    # all same number?
                    if triple[0]==triple[1]==triple[2]:
                        sets_c.append((i,j,k))
                    else:
                        # consecutive numbers?
                        if triple[1]==triple[0]+1 and triple[2]==triple[1]+1:
                            sets_c.append((i,j,k))
        sets_by_color[c] = sets_c

    # Now we have sets by color as indices. Need to pick 3 sets total that cover all cards 0..8 exactly once.
    # The cards are split in groups by color (lengths: len(color_groups[c]) <=9)

    # We know total cards=9
    # We want to select three sets total
    # The sets come from the three colors groups, disjoint in card indices within group

    # Since cards are split, their indices are local to each color group.
    # We'll do backtracking: For each color c, try all combinations of 0 to 3 sets from sets_by_color[c] without overlap.
    # Then combine per color the number of sets (total of 3), and cards covered sum to 9.

    # Precompute all subsets of sets_by_color[c] with no overlapping index
    # Store them as list of (set of indices used, number of sets chosen)
    def gen_subsets(sets_list):
        res = []
        def backtrack(i, used, chosen):
            res.append((used, chosen))
            for idx in range(i, len(sets_list)):
                s = sets_list[idx]
                # check overlap
                if any(x in used for x in s):
                    continue
                backtrack(idx+1, used.union(s), chosen+1)
        backtrack(0, set(), 0)
        return res

    subsets = {}
    for c in 'RGB':
        ssets = [set(tpl) for tpl in sets_by_color[c]]
        subsets[c] = gen_subsets(ssets)

    # Try all triples (a,b,c) from subsets['R'], subsets['G'], subsets['B'] such that:
    # a[1]+b[1]+c[1]==3 (3 sets total)
    # len(a[0])+len(b[0])+len(c[0])==9 (cover all cards)
    # Because each card in all cards is unique and assigned to only one color,
    # coverage of 9 is sum of coverage per color.

    card_count = sum(len(color_groups[c]) for c in 'RGB')
    if card_count !=9:
        return 0

    # We want to cover all cards, so the union of all card indices used in the 3 color groups must cover all card indices.
    # But since each color group only knew its local indices (0..len-1),
    # coverage sum is sum(len(a[0]) + len(b[0]) + len(c[0])) ==9

    for ru, rnum in subsets['R']:
        for gu, gnum in subsets['G']:
            for bu, bnum in subsets['B']:
                if rnum+gnum+bnum==3:
                    if len(ru)+len(gu)+len(bu)==9:
                        return 1
    return 0

input=stdin.readline
T=int(input())
for _ in range(T):
    ns=list(map(int,input().split()))
    cs=input().split()
    cards = list(zip(ns, cs))
    print(can_form_sets(cards))