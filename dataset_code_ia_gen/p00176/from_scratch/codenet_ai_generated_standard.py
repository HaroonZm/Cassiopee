def hex_to_rgb(s):
    return tuple(int(s[i:i+2],16) for i in (0,2,4))

colors = [
    ("black","000000"),
    ("blue","0000ff"),
    ("lime","00ff00"),
    ("aqua","00ffff"),
    ("red","ff0000"),
    ("fuchsia","ff00ff"),
    ("yellow","ffff00"),
    ("white","ffffff"),
]

colors_rgb = [(name, hex_to_rgb(code)) for name,code in colors]

while True:
    line = input().strip()
    if line == '0':
        break
    if len(line) != 7 or line[0] != '#':
        print("white")
        continue
    try:
        r,g,b = hex_to_rgb(line[1:])
    except:
        print("white")
        continue
    best_name = None
    best_dist = None
    for name, (rr,gg,bb) in colors_rgb:
        dist = (r - rr)**2 + (g - gg)**2 + (b - bb)**2
        if best_dist is None or dist < best_dist:
            best_dist = dist
            best_name = name
    print(best_name)