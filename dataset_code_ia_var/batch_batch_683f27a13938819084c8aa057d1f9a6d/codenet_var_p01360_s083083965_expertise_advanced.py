from functools import reduce

def process(s):
    def evaluate(lr):
        b = (int(s[0])-1)%3
        tmp = 0
        for i in map(lambda ch: (int(ch)-1)%3, s[1:]):
            cond = (b < i, b > i)[lr]
            if cond:
                tmp += 1
            else:
                lr ^= 1
            b = i
        return tmp
    return min(map(evaluate, (0, 1)))

if __name__ == '__main__':
    while True:
        s = raw_input()
        if s == "#":
            break
        print process(s)