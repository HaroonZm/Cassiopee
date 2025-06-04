N,M = map(int, input().split())
pots = []
for _ in range(N):
    data = list(map(int, input().split()))
    K = data[0]
    cylinders = []
    for i in range(K):
        S = data[1+2*i]
        H = data[2+2*i]
        cylinders.append((S, H))
    pots.append(cylinders)

max_heights = []
for pot in pots:
    heights_volumes = []
    total_height = 0
    cumulative_volume = 0
    for s,h in pot:
        total_height += h
    max_heights.append(total_height)

def volume_upto_height(pot, h):
    vol = 0
    height_accum = 0
    for s, H in pot:
        if h > height_accum + H:
            vol += s * H
            height_accum += H
        else:
            vol += s * (h - height_accum)
            break
    return vol

def height_for_volume(pot, v):
    height_accum = 0
    for s, H in pot:
        vol_block = s * H
        if v > vol_block:
            v -= vol_block
            height_accum += H
        else:
            height_accum += v / s
            return height_accum
    return height_accum

# Binary search for max sum of heights
low = 0.0
high = sum(max_heights)
for _ in range(100):
    mid = (low + high) / 2
    required_volume = 0.0
    for i in range(N):
        # For each pot find volume needed to reach height min(max_heights[i], mid)
        h = min(max_heights[i], mid)
        v = volume_upto_height(pots[i], h)
        required_volume += v
    if required_volume <= M:
        low = mid
    else:
        high = mid

print(low)