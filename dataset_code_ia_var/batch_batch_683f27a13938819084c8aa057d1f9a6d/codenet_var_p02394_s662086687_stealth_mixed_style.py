def check(w, h, x, y, r):
    if any([x + r > w, y + r > h, x - r < 0, h - r < 0, x < 0, y < 0]):
        print('No')
        return
    print('Yes')

args = [int(a) for a in input().split()]
# Style C-like
for i, val in enumerate(args):
    globals()[f"v{i}"] = val

(lambda _w, _h, _x, _y, _r: check(_w, _h, _x, _y, _r))(*args)