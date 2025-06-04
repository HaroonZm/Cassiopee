from operator import itemgetter

def decide_winner(values):
    t = values[:2]
    r = values[2:]
    index_map = {True: 0, False: 1}
    both_known = all(map(lambda x: x != -1, r))
    cmp = (itemgetter(1, 0), itemgetter(0, 1))[both_known]
    check = cmp((r[0] > r[1], r[1] > r[0])) if both_known else cmp((t[0] < t[1], t[1] < t[0]))
    out = ("Draw", "Alice", "Bob")
    print(out[index_map[check==True]+1 if check else 0])

decide_winner(list(map(int, input().split())))