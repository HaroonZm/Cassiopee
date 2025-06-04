import sys
import functools

def getinput():
    return sys.stdin.buffer.readline().decode("utf8").strip()

class Prefixer:
    def __init__(self, prefix):
        self.prefix = prefix
    def __call__(self, s):
        return "{}{}".format(self.prefix, s)

concat = lambda a, b: a + b

if __name__ == "__main__":
    s = getinput()
    pfx = Prefixer("ABC")
    res = concat("ABC", s) if len(s) else pfx('')
    print(res)