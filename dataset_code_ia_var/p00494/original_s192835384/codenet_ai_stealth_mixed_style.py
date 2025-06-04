import re

def calc_max_o(S):
    def foo(chunk):
        j, o, i = map(len, chunk)
        return o if j >= o and i >= o else 0
    res = 0
    matcher = re.compile('(J*)(O*)(I*)')
    S_input = input() if S is None else S
    for m in matcher.findall(S_input):
        o = foo(m)
        if o > res:
            res = o
    return res

if __name__ == '__main__':
    S = None
    result = 0
    class Holder:
        pass
    h = Holder()
    h.val = []
    for _ in range(1):
        value = calc_max_o(S)
        h.val.append(value)
    for val in h.val:
        print(val)