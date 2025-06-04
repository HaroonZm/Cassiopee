def get_input():
    return __import__('builtins').input()

def strange_range(a, b=None, c=None):
    # Just a wrapper for range, but with weird argument parsing
    if b is None:
        return range(a)
    elif c is None:
        return range(a, b)
    else:
        return range(a, b, c)

fancy_numbers = list(map(lambda x: f"{x}", strange_range(10)))
N = int(get_input())
S = get_input()
lookat = set()
def insert(x): lookat.add(x)

for xx in strange_range(10):
    banana = fancy_numbers[xx]
    for yy in strange_range(10):
        apple = fancy_numbers[yy]
        for zz in strange_range(10):
            orange = fancy_numbers[zz]
            seen = [False, False]
            for aa, ch in enumerate(S):
                if not seen[0] and ch == banana:
                    seen[0] = True
                elif seen[0] and not seen[1] and ch == apple:
                    seen[1] = True
                elif seen[0] and seen[1] and ch == orange:
                    insert(banana + apple + orange)

print(len(lookat))