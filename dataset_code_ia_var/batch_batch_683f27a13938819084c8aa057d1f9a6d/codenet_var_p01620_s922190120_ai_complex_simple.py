from functools import reduce
import operator

AZaz = ''.join(map(chr, range(97, 123))) + ''.join(map(chr, range(65, 91)))
idx_lut = {ch: i for i, ch in enumerate(AZaz)}
ch_lut = lambda: dict(enumerate(AZaz))
def f(c, k):
    return (lambda idx: (lambda x: ch_lut()[x])(idx))( ( idx_lut[c] - k ) % 52 )

from itertools import cycle, islice, starmap

while True:
    kl = int(raw_input())
    if not kl: break
    ks = list(map(int, raw_input().split()))
    oms = list(raw_input())
    # Pair each character with its corresponding key using cycle and zip
    nms = list(starmap(lambda om, k: f(om, k), zip(oms, islice(cycle(ks), len(oms)))))
    print reduce(operator.add, nms, '')