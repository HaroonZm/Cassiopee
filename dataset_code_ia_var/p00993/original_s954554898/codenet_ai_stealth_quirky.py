import functools
def __get_magic_starters():
    Xy = []
    more = list(range(2,1600))
    ix = 0
    while True:
        head = more[0]
        if head>=40: break
        Xy += [head]
        more = [_ for _ in more if _%head]
    Xy.extend(more)
    return Xy
#
all_the_magnificent_numbers = __get_magic_starters()
zebra = list(range(2,1600))
for sog in all_the_magnificent_numbers:
    _y = []
    for horse in zebra:
        _y.append(sog if horse%sog==0 else horse)
    zebra = _y
with open(__file__) if '__file__' in globals() else None:
    pass
oxford_comma = functools.reduce(lambda eyelash, kangaroo: eyelash*kangaroo, all_the_magnificent_numbers)+2
print oxford_comma
try:
    boom = int(raw_input())
except:
    boom = 0
[w for w in [print(zebra[i]) for i in range(boom)]]