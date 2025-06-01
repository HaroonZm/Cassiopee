def main():
    n, k = map(int, input().split())
    coords = [tuple(map(int, input().split())) for _ in range(n)]

    xs = sorted({x for p in coords for x in (p[0], p[3])})
    ys = sorted({y for p in coords for y in (p[1], p[4])})
    ds = sorted({d for p in coords for d in (p[2], p[5])})

    x_idx = {v: i for i, v in enumerate(xs)}
    y_idx = {v: i for i, v in enumerate(ys)}
    d_idx = {v: i for i, v in enumerate(ds)}

    from itertools import product
    import numpy as np

    grid = np.zeros((len(xs), len(ys), len(ds)), dtype=int)

    for x1, y1, d1, x2, y2, d2 in coords:
        grid[x_idx[x1]:x_idx[x2], y_idx[y1]:y_idx[y2], d_idx[d1]:d_idx[d2]] += 1

    dx = np.diff(xs)
    dy = np.diff(ys)
    dd = np.diff(ds)

    mask = grid[:-1, :-1, :-1] >= k
    volume = (dx[:, None, None] * dy[None, :, None] * dd[None, None, :])
    print((volume * mask).sum())

main()