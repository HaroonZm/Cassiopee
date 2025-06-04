colors = [
    ("black", (0x00, 0x00, 0x00)),
    ("blue", (0x00, 0x00, 0xff)),
    ("lime", (0x00, 0xff, 0x00)),
    ("aqua", (0x00, 0xff, 0xff)),
    ("red", (0xff, 0x00, 0x00)),
    ("fuchsia", (0xff, 0x00, 0xff)),
    ("yellow", (0xff, 0xff, 0x00)),
    ("white", (0xff, 0xff, 0xff)),
]

import sys

def hex_to_rgb(h):
    try:
        return int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    except:
        return 255,255,255

for line in sys.stdin:
    line=line.strip()
    if line=="0":
        break
    if len(line)!=7 or line[0]!="#":
        rgb = 255,255,255
    else:
        rgb = hex_to_rgb(line[1:])
    r,g,b=rgb
    mind=10**10
    res=None
    for name,(R,G,B) in colors:
        d=(r-R)**2+(g-G)**2+(b-B)**2
        if d<mind:
            mind=d
            res=name
    print(res)