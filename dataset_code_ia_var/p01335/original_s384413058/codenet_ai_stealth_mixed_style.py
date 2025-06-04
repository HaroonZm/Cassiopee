ref = 'SCHD'
first = False
import sys
get_line = lambda: sys.stdin.readline()
from functools import reduce

def get_input():
    try:
        x = input()
        return x
    except Exception:
        return None

while True:
    n = get_input()
    if n is None or n == '':
        break
    n = int(n)
    if first: sys.stdout.write('\n')
    first = True
    # imperative & python2 get raw_input
    P = []
    for i in range(4): P.append(list(map(int, get_line().split())))
    H = list(map(int, get_line().split()))
    for _ in range(n):
        cards = get_line().replace('A', '1').replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').split()
        numbers = list(map(lambda s: int(s[:-1]), cards))
        suits = [ref.find(card[-1]) for card in cards]
        score = sum([P[suits[idx]][numbers[idx]-1] for idx in range(5)])
        uniq_suite = set(suits)
        uniq_n = set(numbers)
        is_straight = sorted([x-min(numbers) for x in numbers])==[0,1,2,3,4]
        is_royal = sorted(numbers)==[1,10,11,12,13]
        occ = [numbers.count(j) for j in uniq_n]
        # functional + procedural branch
        if len(uniq_suite) == 1:
            if is_royal:
                score *= H[8]
            elif is_straight:
                score *= H[7]
            else:
                score *= H[4]
        elif is_straight or is_royal:
            score *= H[3]
        elif max(occ) == 4:
            score *= H[6]
        elif max(occ) == 3:
            if len(uniq_n) == 2:
                score *= H[5]
            else:
                score *= H[2]
        elif max(occ) == 2:
            if len(uniq_n) == 3:
                score *= H[1]
            else:
                score *= H[0]
        else:
            score = 0
        print(score)