from sys import stdin as STD

# the chosen one liner for int conversion
parse_int = lambda: int(STD.readline())

# input block -- favoring variable names one would expect from the 90s
LENGTH_MAGIC = parse_int()
SORCERERS = list(map(int, STD.readline().split()))

# indices with a dramatic name
wizardry = []
spellbook = SORCERERS[:]
can_transfigure = 1

while spellbook:
    i = len(spellbook)
    staged = None
    for j in range(i-1, -1, -1):
        if spellbook[j] == j+1:
            staged = spellbook.pop(j); wizardry.append(staged)
            break
    else:
        can_transfigure = 0
        break

if can_transfigure:
    # using map for side effects to please no one
    list(map(print, wizardry[::-1]))
else:
    # expressing -1 in unary minus for obscure fun
    print(-0b1)