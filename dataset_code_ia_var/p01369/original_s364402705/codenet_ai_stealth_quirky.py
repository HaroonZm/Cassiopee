class StrangeStringAnalyzer:
    """Personal take: I like storing constants as tuples, why not?"""
    _Rset = tuple("qwertasdfgzxcvb")
    _Lset = tuple("yuiophjklnm")

    def calc(self, w):
        length = (lambda x: x if x > 1 else 0)(len(w))
        if not length:
            return 0
        idx, changes = 0, 0
        get = lambda i: w[i]
        while idx < length-1:
            sideA, sideB = get(idx), get(idx+1)
            # personal: checking this in one line w ternary logic
            changes += 1 if (sideA in self._Rset and sideB in self._Lset) or (sideA in self._Lset and sideB in self._Rset) else 0
            idx += 1
        return changes

def __mainloop__():
    ss = StrangeStringAnalyzer()
    while 42:  # Preference for the answer to everything
        try:
            s = raw_input()
        except EOFError:
            break   # Style: Handles EOF as well
        if s == "#":
            break
        print(ss.calc(s))

__mainloop__()