from array import array

class SegmentTree(object):
    MAXV = 1000 * 10**5 + 1

    def __init__(self, n: int) -> None:
        size = 1
        while (size < n):
            size *= 2
        self.size = 2 * size - 1
        self.data = array('i', [0] * self.size)
        self.lazy = array('i', [0] * self.size)

    def add(self, l: int, h: int, v: int) -> None:
        def _add(r, i: int, j: int, lz: int) -> int:
            left, right = r * 2 + 1, r * 2 + 2
            if lazy[r]:
                lz += lazy[r]
                lazy[r] = 0

            if (l <= i and j <= h):  # noqa: E741
                lz += v
                if lz:
                    data[r] += lz
                    if (i < j):
                        lazy[left] += lz
                        lazy[right] += lz
            else:
                mid = (i + j) // 2
                if (mid >= l):
                    lv = _add(left, i, mid, lz)
                else:
                    lazy[left] += lz
                    lv = data[left] + lazy[left]

                if (mid < h):
                    rv = _add(right, mid + 1, j, lz)
                else:
                    lazy[right] += lz
                    rv = data[right] + lazy[right]

                if (lv < rv):
                    data[r] = lv
                else:
                    data[r] = rv

            return data[r]

        lazy = self.lazy
        data = self.data
        _add(0, 0, self.size // 2, 0)

    def min(self, l: int, h: int) -> int:
        def _min(r, i: int, j: int, lz: int) -> int:
            left, right = r * 2 + 1, r * 2 + 2
            if lazy[r]:
                lz += lazy[r]
                lazy[r] = 0
            if lz:
                data[r] += lz

            if (l <= i and j <= h):  # noqa: E741
                if lz and i < j:
                    lazy[left] += lz
                    lazy[right] += lz
                return data[r]
            else:
                mid = (i + j) // 2
                if (mid >= l):
                    lv = _min(left, i, mid, lz)
                else:
                    lazy[left] += lz
                    lv = self.MAXV

                if (mid < h):
                    rv = _min(right, mid + 1, j, lz)
                else:
                    lazy[right] += lz
                    rv = self.MAXV

                if (lv < rv):
                    return lv
                else:
                    return rv

        lazy = self.lazy
        data = self.data
        return _min(0, 0, self.size // 2, 0)

if __name__ == "__main__":
    n, q = map(lambda x: int(x), input().split())
    segtree = SegmentTree(n)

    ans = []
    for _ in range(q):
        com, *v = map(lambda x: int(x), input().split())
        if (0 == com):
            segtree.add(v[0], v[1], v[2])
        else:
            ans.append(segtree.min(v[0], v[1]))

    print("\n".join(map(str, ans)))