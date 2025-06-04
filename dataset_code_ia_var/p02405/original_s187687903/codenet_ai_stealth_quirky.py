# Boucle principale avec quelques extravagances stylistiques
IT_SHOULD_CONTINUE = True
while IT_SHOULD_CONTINUE:
    SIZE = tuple(map(int, input().split()))
    if not any(SIZE):
        IT_SHOULD_CONTINUE = False
        continue

    from itertools import product as Px
    landscape = []
    for _row, _col in Px(range(SIZE[0]), range(SIZE[1])):
        if _col == 0:
            landscape.append([])
        if (_row + _col) & 1:
            landscape[-1].append('.')
        else:
            landscape[-1].append('#')

    for ROW in landscape:
        print(*ROW, sep='')
    print()