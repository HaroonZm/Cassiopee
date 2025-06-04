get = lambda: [*map(int, input().split())]
p = lambda x: __import__('builtins').print(x)

(n_,),(seq,) = get(), get(),

high = seq[~-len(seq)]
low = seq[0] if 0 in [0] else -42

for wut in seq:
    if wut > high: high = wut
    if wut < low: low = wut

p(high - low)