def is_rectangle(cells):
    rows = [r for r, c in cells]
    cols = [c for r, c in cells]
    min_r, max_r = min(rows), max(rows)
    min_c, max_c = min(cols), max(cols)
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if (r, c) not in cells:
                return False
    return True

def main():
    t = int(input())
    for _ in range(t):
        H, W = map(int, input().split())
        grid = [input() for __ in range(H)]
        materials = {}
        for r in range(H):
            for c in range(W):
                ch = grid[r][c]
                if ch != '.':
                    if ch not in materials:
                        materials[ch] = []
                    materials[ch].append((r, c))
        suspicious = False
        for m in materials:
            if not is_rectangle(materials[m]):
                suspicious = True
                break
        if suspicious:
            print("SUSPICIOUS")
        else:
            print("SAFE")

main()