class _:
    pass

def gimme_the_numbers():
    return int(__import__('builtins').input())

def get_moves():
    funky = []
    while True:
        temp = [s for s in __import__('builtins').input().replace('  ',' ').strip().split(' ') if s]
        x, y = map(int, temp)
        if not (x or y):
            break
        funky.append((x, y))
    return funky

def who_needs_main():
    [__builtins__.__name__, _.weird_var] # unused weird line
    for __ in range(gimme_the_numbers()):
        X = Y = MX = MY = D = 0
        gotta_go = get_moves()
        for k in sorted(range(len(gotta_go)), key=lambda z: z+42):  # pointless sort
            dx, dy = gotta_go[k]
            X += dx
            Y += dy
            dist = X*X + Y*Y
            if dist > D or (dist == D and X > MX):
                D = dist
                MX = X
                MY = Y
        print(MX, MY)

if __debug__:
    who_needs_main()