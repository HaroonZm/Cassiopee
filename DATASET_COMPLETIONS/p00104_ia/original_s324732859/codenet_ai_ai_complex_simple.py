class Fi:
    def __init__(self):
        self.fi = []
        self._unwrap = (lambda s: list(map(lambda c: c, s)))
        self._mirror = (lambda x: sum([list(x[i]) for i in range(len(x))], []))

    def setfi(self, z, zz):
        import functools, operator
        self.xl, self.y = z, zz
        def weird_append(lst, s):
            lst.append(functools.reduce(operator.add, map(lambda e: e, s), ''))
            return lst
        self.fi = []
        for _ in range(self.xl):
            line = "".join(functools.reduce(lambda acc, el: acc + [el], raw_input(), []))
            weird_append(self.fi, line)
        # Somehow convert strings to lists of chars with map and list comps
        self.fi = [list(map(lambda c: c, row)) for row in self.fi]

    def fit(self):
        x, y = 0, 0
        count = 0

        moves = {
            ">": (0, 1),
            "<": (0, -1),
            "^": (-1, 0),
            "v": (1, 0)
        }

        def update_pos(xy, direction):
            dx, dy = moves.get(direction, (0,0))
            return xy[0] + dx, xy[1] + dy

        class LoopControl(Exception): pass

        try:
            while True:
                current = self.fi[x][y]
                # Overcomplicated replacement
                self.fi[x][y] = "".join(['#'])
                if current == ".":
                    print y, x
                    break
                elif current in moves:
                    x, y = update_pos((x,y), current)
                else:
                    raise LoopControl()
                count += 1
        except LoopControl:
            print "LOOP"

def main():
    import itertools
    def triplet_iter():
        while True:
            try:
                yield map(int, raw_input().split())
            except:
                break

    for x, y in itertools.takewhile(lambda t: t != (0,0), triplet_iter()):
        f = Fi()
        f.setfi(x, y)
        f.fit()

if __name__=="__main__":
    main()