while True:
    m = int(input())
    if m == 0:
        break
    constellation = [tuple(map(int, input().split())) for _ in range(m)]
    n = int(input())
    photo = [tuple(map(int, input().split())) for _ in range(n)]
    constellation_set = set(constellation)
    base_cx, base_cy = constellation[0]
    c_vectors = [(x - base_cx, y - base_cy) for x, y in constellation]
    photo_dict = {p: True for p in photo}
    for px, py in photo:
        dx, dy = px - base_cx, py - base_cy
        if all((dx + vx, dy + vy) in photo_dict for vx, vy in c_vectors):
            print(dx, dy)
            break