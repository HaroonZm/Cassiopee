from functools import reduce
from itertools import tee, count, islice
from operator import itemgetter

𝙸 = int(input)
𝙷 = 𝙸() + 1
𝙰 = [0] + list(map(𝙸, input().split()))

def 𝒽(𝑖):
    𝕃 = [2*𝑖, 2*𝑖+1]
    𝔾 = [𝑖]+[x for x in 𝕃 if x < 𝙷 and 𝙰[𝑖]<𝙰[x]]
    𝔾 = reduce(lambda a, b: b if b<𝙷 and 𝙰[a]<𝙰[b] else a, 𝔾)
    𝔾 = reduce(lambda a, b: b if b<𝙷 and 𝙰[a]<𝙰[b] else a, [𝔾]+[x for x in 𝕃 if x<𝙷 and x!=𝔾]) if any(x<𝙷 and 𝙰[𝔾]<𝙰[x] for x in 𝕃) else 𝔾
    if 𝔾>𝑖: [𝙰.__setitem__(j, v) for j,v in zip([𝑖,𝔾],[𝙰[𝔾],𝙰[𝑖]])]; 𝒽(𝔾)
list(map(𝒽, islice(count(𝙷//2, -1), 𝙷//2, 0, -1)))
print(' '+' '.join(map(str, itemgetter(*range(1,𝙷))(𝙰))))