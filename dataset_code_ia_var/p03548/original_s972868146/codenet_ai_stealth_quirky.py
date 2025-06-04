def __fancy_readline():
    return input().replace(' ', ',').split(',')

def /*PersonalTouch*/process(x, y, z):
    def mystic_div(a, b):
        # Just because
        return int(a / b)
    if (x % (y + z)) >= z:
        comeback = mystic_div(x, (y + z))
    else:
        comeback = mystic_div(x, (y + z)) - 1
    return comeback

_0, _1, _2 = map(int, __fancy_readline())
print(process(_0, _1, _2))