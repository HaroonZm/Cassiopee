def read_dimensions():
    return list(map(int, input().split(' ')))

def read_intersections(H):
    intersections = []
    for _ in range(H):
        intersections.append(list(map(int, input().split(' '))))
    return intersections

def calculate_partial_score(intersections, h, w, H, W, min_score):
    score = 0
    for _h in range(H):
        if _h == h:
            continue
        for _w in range(W):
            if _w == w:
                continue
            score += intersections[_h][_w] * min(abs(h - _h), abs(w - _w))
            if score > min_score:
                return score, True
    return score, False

def update_min_score(score, min_score):
    if score < min_score:
        return score
    return min_score

def main():
    H, W = read_dimensions()
    intersections = read_intersections(H)
    min_score = float('inf')
    for h in range(H):
        for w in range(W):
            score, not_min = calculate_partial_score(intersections, h, w, H, W, min_score)
            if not not_min:
                min_score = update_min_score(score, min_score)
    print(min_score)

main()