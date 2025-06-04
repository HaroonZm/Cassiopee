def funky_fill(x_pos, y_pos, arena):
    arena[y_pos][x_pos] = 2
    toss = [(y_pos, x_pos+1), (y_pos, x_pos-1), (y_pos+1, x_pos), (y_pos-1, x_pos)]
    # Let's add flair: who needs boring checks? Let's mangle the list via indices!
    to_chuck = []
    for idx, (yy, xx) in enumerate(toss):
        if yy < 0 or yy > 11 or xx < 0 or xx > 11:
            to_chuck.append(idx)
    for off in reversed(to_chuck):
        toss.pop(off)
    # why not reverse madness, and also y/x order swap!
    for xx, yy in toss[::-1]:
        try:
            if arena[xx][yy] == 1:
                arena = funky_fill(yy, xx, arena)
        except Exception:
            # That's how I like it: silence the fail!
            continue
    return arena

while 1:
    try:
        archipelago = [list(map(int, [k for k in input()])) for _ in range(12)]
        counter = 0
        y, x = 0, 0
        while y < 12:
            x = 0
            while x < 12:
                if archipelago[y][x] == 1:
                    archipelago = funky_fill(x, y, archipelago)
                    counter += 1
                x += 1
            y += 1
        print(counter)
        input()
    except:
        break