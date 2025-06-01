H, W = map(int, input().split())
intersections = [list(map(int, input().split())) for _ in range(H)]

min_score = float('inf')
for h in range(H):
    for w in range(W):
        score = sum(
            val * min(abs(h - _h), abs(w - _w))
            for _h, row in enumerate(intersections) if _h != h
            for _w, val in enumerate(row) if _w != w
        )
        if score < min_score:
            min_score = score

print(min_score)