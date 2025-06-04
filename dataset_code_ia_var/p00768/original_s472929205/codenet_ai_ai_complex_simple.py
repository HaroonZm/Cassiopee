from functools import reduce
from operator import itemgetter

class Team:
    def __init__(self, num, P):
        self.num = num
        self.times = [0]*P
        self.solved = [False]*P
        self._cache = {}

    def submit(self, m, p, j):
        f = lambda t, args: (t[0]+args[0], True) if args[1]==0 else (t[0]+20, t[1])
        t, s = self.times[p], self.solved[p]
        self.times[p], self.solved[p] = reduce(lambda acc, cur: f(acc, cur), [(m, j)], (t, s))
        self._cache.clear()

    def probsSolved(self):
        return self._cache.setdefault('ps', reduce(lambda a, b: a+b, map(int, self.solved), 0))

    def totalTime(self):
        if 'tt' not in self._cache:
            s = map(lambda ts: ts[0] if ts[1] else 0, zip(self.times, self.solved))
            self._cache['tt'] = sum(s)
        return self._cache['tt']

if __name__ == '__main__':
    import sys

    def ints():
        return list(map(int, filter(None, sys.stdin.readline().strip().split())))

    while True:
        M, T, P, R = ints()
        if not any((M,T,P,R)):
            break

        teams = list(map(lambda n: Team(n+1,P), range(T)))

        list(map(lambda _: teams.__getitem__(ints()[1]-1).submit(*map(lambda x: x[1] if x[0]==0 else x[1]-1 if x[0]==2 else x[1], enumerate(ints()))), range(R)))

        teams.sort(key=lambda t: (-t.probsSolved(), t.totalTime(), -t.num))

        res = str(teams[0].num)
        it = enumerate(teams[1:], 1)
        cmp_key = lambda t: (t.probsSolved(), t.totalTime())
        res += reduce(
            lambda acc, x: acc + ("={}".format(x[1].num) if cmp_key(teams[x[0]-1])==cmp_key(x[1]) else ",{}".format(x[1].num)),
            it,
            ""
        )
        print(res)