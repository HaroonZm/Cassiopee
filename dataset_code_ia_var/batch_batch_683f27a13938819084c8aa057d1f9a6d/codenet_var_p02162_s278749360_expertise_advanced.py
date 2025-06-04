from operator import itemgetter

t1, t2, r1, r2 = map(int, input().split())
match (r1, r2):
    case (-1, _) | (_, -1):
        print({t1 < t2: 'Alice', t1 > t2: 'Bob'}.get(True, 'Draw'))
    case _ if r1 != r2:
        winner = ('Alice', 'Bob')[r1 < r2]
        print(winner)
    case _:
        print('Draw')