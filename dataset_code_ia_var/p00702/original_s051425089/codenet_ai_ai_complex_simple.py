from functools import reduce, lru_cache
from itertools import chain, product
from collections import defaultdict, Counter

kcs = [chr(i) for i in range(97, 123)]
kcs2 = ['ld','mb','mp','nc','nd','ng','nt','nw','ps','qu','cw','ts']
kcs2_1 = list({pair[0] for pair in kcs2})

# Create a defaultdict of Counters for maximum laziness
dic = defaultdict(lambda: Counter({k:0 for k in chain(kcs, kcs2)}))

def count_characters(word, dic, kcs, kcs2, kcs2_1):
    indices = range(len(word))
    prev1 = [None]
    def analyze(i):
        if i >= len(word): return
        c = word[i]
        get2 = lambda idx: word[idx:idx+2]
        if c in kcs2_1 and i < len(word)-1 and get2(i) in kcs2:
            if prev1[0] is not None:
                dic[prev1[0]][get2(i)] += 1
            prev1[0] = get2(i)
            analyze(i+2)
        else:
            if prev1[0] is not None:
                dic[prev1[0]][c] += 1
            prev1[0] = c
            analyze(i+1)
    analyze(0)

n = reduce(lambda acc, _: acc, [int(input())], 0)
for _ in range(n):
    list(map(lambda w: count_characters(w, dic, kcs, kcs2, kcs2_1), chain.from_iterable(input().split() for _ in [0])))

for c in chain(kcs, kcs2):
    res = max(dic[c].items(), key=lambda kv: (kv[1], kv[0]))
    print(c, res[0], res[1])