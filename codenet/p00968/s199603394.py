N = int(input())
S = [input() for _ in range(N + 1)]

def convert(s):
    l = []
    for i in range(len(s)):
        if s[i].isdigit():
            if len(l) != 0 and isinstance(l[-1], list):
                l[-1].append(s[i])
            else:
                l.append([s[i]])
        else:
            l.append(s[i])

    return [int(''.join(e)) if isinstance(e, list) else e for e in l]

S = [convert(e) for e in S]
t = S[0]

def compare(s):
    for i in range(min([len(s), len(t)])):
        if type(s[i]) == type(t[i]):
            if s[i] < t[i]:
                return '-'
            elif s[i] > t[i]:
                return '+'
        else:
            if type(s[i]) == int:
                return '-'
            else:
                return '+'
    if len(t) <= len(s):
        return '+'
    else:
        return '-'

for s in S[1:]:
    print(compare(s))