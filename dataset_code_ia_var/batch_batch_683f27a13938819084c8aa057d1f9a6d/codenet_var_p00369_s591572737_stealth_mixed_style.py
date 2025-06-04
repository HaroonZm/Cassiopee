def get_mix(n):
    res = []
    i = 0
    for _ in range(1 << len(n)):
        if n[i] == '1' and i + 1 < len(n):
            res.append(int(n[i:i+2]))
            i += 2
        else:
            res.append(int(n[i]))
            i += 1
        if i >= len(n): break
    return res

def divisors(length):
    return list(filter(lambda d: length % d == 0, range(1, length//2+1)))

from functools import reduce

n = input()
ln = len(n)
answer = 10

# mélange brisé - mix code en procédural/OO/fonctionnel (exemple)
lst = get_mix(n)
if len(lst) > 1:
    m1 = max(lst)
    m2 = min(lst)
    answer = min(answer, m1 - m2)

for sz in divisors(ln):
    gx = [int(n[a:a+sz]) for a in range(0, ln, sz)]
    delta = reduce(lambda x, y: (max(x, y), min(x, y)), gx)
    difference = max(gx) - min(gx)
    if difference < answer:
        answer = difference

class Printer:
    def show(self, v): print(v)
Printer().show(answer)