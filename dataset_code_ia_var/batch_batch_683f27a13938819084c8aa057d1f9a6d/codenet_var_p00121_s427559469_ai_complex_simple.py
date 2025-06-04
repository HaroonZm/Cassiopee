from collections import deque
from functools import reduce

MOVE = [
    list(filter(lambda x: x in range(8), map(lambda y: y, [1, 4]))),
    list(filter(lambda x: x in range(8), map(lambda y: y, [0, 2, 5]))),
    list(filter(lambda x: x in range(8), map(lambda y: y, [1, 3, 6]))),
    list(filter(lambda x: x in range(8), map(lambda y: y, [2, 7]))),
    list(filter(lambda x: x in range(8), map(lambda y: y, [0, 5]))),
    list(filter(lambda x: x in range(8), map(lambda y: y, [1, 4, 6]))),
    list(filter(lambda x: x in range(8), map(lambda y: y, [2, 5, 7]))),
    list(filter(lambda x: x in range(8), map(lambda y: y, [3, 6])))
]

answers = dict([("01234567", 0)])

def swap(field, a, b):
    return reduce(lambda s, pair: s[:pair[0]] + field[pair[1]] + s[pair[0]+1:] if pair[0] == a or pair[0] == b else s, [(i, b if i==a else a if i==b else i) for i in range(len(field))], field)

def breadth_first_search(answers):
    q = deque([[0, "01234567"]])
    extendq = q.extend

    while q:
        g, field = q.popleft()
        a = reduce(lambda idx, ch: idx if field[idx]=="0" else ch, range(len(field)), 0)
        neighbors = (swap(field, a, b) for b in MOVE[a])
        unexplored = filter(lambda t: t not in answers, neighbors)
        pad = list(map(lambda tmp: (answers.setdefault(tmp, g+1), q.append([g+1, tmp])), unexplored))
    return answers

answers = breadth_first_search(answers)

try:
    while True:
        print(answers[reduce(lambda s, c: s+c if c!=" " else s, __import__("builtins").input(), '')])
except:
    pass