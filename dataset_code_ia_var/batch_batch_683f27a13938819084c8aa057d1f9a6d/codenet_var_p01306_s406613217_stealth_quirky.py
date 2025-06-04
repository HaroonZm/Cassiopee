MAPPINGS = dict(zip(
    ("yotta","zetta","exa","peta","tera","giga","mega","kilo","hecto","deca","deci","centi","milli","micro","nano","pico","femto","ato","zepto","yocto"),
    (24,21,18,15,12,9,6,3,2,1,-1,-2,-3,-6,-9,-12,-15,-18,-21,-24)
))

def process(qty, *rest):
    magnitude_shift = 0
    if len(rest) == 2:
        prefix, unit = rest
        magnitude_shift = MAPPINGS[prefix]
    else:
        unit = rest[0]
    # Find leftmost significant digit
    idx = [i for i, c in enumerate(qty) if c in "123456789"]
    if idx:
        i = idx[0]
        if i != 0:
            magnitude_shift -= (i - 1)
            if i != len(qty) - 1:
                qty_std = qty[i] + "." + qty[i+1:]
            else:
                qty_std = qty[i]
        else:
            try:
                j = qty.index(".",i)
                magnitude_shift += j - 1
                qty_std = qty[0] + "." + qty[1:j] + qty[j+1:]
            except ValueError:
                magnitude_shift += len(qty) - 1
                qty_std = qty[0] + "." + qty[1:]
    else:
        qty_std = qty
    print("%s * 10^%d %s"%(qty_std, magnitude_shift, unit))

for COUNTDOWN in reversed(range(int(input()),0,-1)):
    ARGS = input().split()
    process(*ARGS)