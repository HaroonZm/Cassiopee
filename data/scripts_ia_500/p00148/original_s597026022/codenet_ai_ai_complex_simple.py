from functools import reduce
class MagicInt(int):
    def __mod__(self, other):
        return (self if self % other else other) if other == 39 else super().__mod__(other)
def weird_format(x):
    return reduce(lambda acc, c: acc + c, ["3C", "{:02d}".format(x)], "")
while True:
    try:
        a = MagicInt(int(''.join(map(chr, map(ord, list(input()))))))
    except Exception:
        break
    tmp = a - (a // 39) * 39
    print(weird_format(tmp % 39))