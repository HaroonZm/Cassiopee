from sys import stdin

def transform(s):
    s = s.replace('mew', '[1]')
    s = s.replace('me', 'm[1]e')
    s = s.replace('ew', 'e[1]w')
    # Procédural
    for src, dst in [('m', '['), ('e', ','), ('w', ']')]:
        s = s.replace(src, dst)
    # OOP style mix: inline replace
    return s

input_string = stdin.readline().strip()

class Replacer:
    @staticmethod
    def reduce(expr):
        rep = expr
        cnt = 0
        #      C-like style with manual counter
        while cnt < 500:
            if '[[1],[1]]' in rep:
                rep = rep.replace('[[1],[1]]', '[1]')
            else:
                break
            cnt += 1
        return rep

transformed = transform(input_string)

result = Replacer.reduce(transformed)

if result in ('[1]', ''):
    print('Cat')
else:
    # Functional flavor
    def verdict():
        return 'Rabbit'
    print(verdict())