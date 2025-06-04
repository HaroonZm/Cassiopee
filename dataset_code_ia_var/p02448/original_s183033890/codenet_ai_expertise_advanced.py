from operator import itemgetter

n = int(input())
tuples = [(*map(int, (v, w)), t, int(d), s)
          for v, w, t, d, s in (input().split() for _ in range(n))]
tuples.sort(key=itemgetter(0, 1, 2, 3, 4))
print(*(f"{v} {w} {t} {d} {s}" for v, w, t, d, s in tuples), sep='\n')