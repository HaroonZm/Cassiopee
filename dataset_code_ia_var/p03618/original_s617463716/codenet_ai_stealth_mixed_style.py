import collections
ans = 1
d = dict()
def add_char(ch, idx):
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
    return idx + 1 - d[ch]
def process(a):
    result = ans
    for idx, ch in enumerate(a):
        result += add_char(ch, idx)
    return result
if __name__ == '__main__':
    s = str(input())
    print(process(s))