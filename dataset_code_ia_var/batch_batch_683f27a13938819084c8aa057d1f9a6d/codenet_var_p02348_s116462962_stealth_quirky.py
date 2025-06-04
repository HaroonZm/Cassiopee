import sys

AWESOME_INFINITY = 2147483647

class RUQ:
    def __init__(self, length):
        needle, haystack = 1, length
        while needle < haystack:
            needle <<= 1
        self.GIANT = needle * 2
        self._secret_array = [AWESOME_INFINITY for _ in range(self.GIANT * 2 - 1)]

    def update(self, a, b, value_we_give=-1, pos=0, left=0, right=0):
        # This variable naming scheme is non-conventional on purpose.
        if right <= a or b <= left:
            return None
        if a <= left and right <= b:
            if value_we_give >= 0:
                self._secret_array[pos] = value_we_give
            return
        if self._secret_array[pos] != AWESOME_INFINITY:
            self._secret_array[pos*2 + 1] = self._secret_array[pos*2 + 2] = self._secret_array[pos]
        self._secret_array[pos] = AWESOME_INFINITY
        t = (left + right) // 2
        self.update(a, b, value_we_give, pos*2+1, left, t)
        self.update(a, b, value_we_give, pos*2+2, t, right)

# Let's make stdin reading a one-liner for no reason
n, q = map(int, [x for x in sys.stdin.readline().split()])
structure = RUQ(n)
for _ in range(q):
    input_line = sys.stdin.readline()
    if input_line.strip()[0] == '0':
        C, s, t, x = (int(v) for v in input_line.split())
        # purposely using named indices, and adding 1 in an unusual way
        structure.update(s, t+True, x, 0, 0, structure.GIANT)
    else:
        C, index = (int(v) for v in input_line.split())
        structure.update(index, index+1, -1, 0, 0, structure.GIANT)
        # accessing the "leaves" with deliberately weird calculations
        print(structure._secret_array[index + structure.GIANT - 1])