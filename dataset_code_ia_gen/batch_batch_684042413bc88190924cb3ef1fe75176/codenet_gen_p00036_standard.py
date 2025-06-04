import sys

shapes = {
    'A': {(0,0),(0,1),(0,2),(0,3)},
    'B': {(0,0),(1,0),(2,0),(3,0)},
    'C': {(0,0),(0,1),(1,0),(1,1)},
    'D': {(0,0),(0,1),(1,1),(1,2)},
    'E': {(1,0),(2,0),(0,1),(1,1)},
    'F': {(0,0),(1,0),(1,1),(2,1)},
    'G': {(1,0),(2,0),(1,1),(0,1)}
}

def normalize(positions):
    min_r = min(p[0] for p in positions)
    min_c = min(p[1] for p in positions)
    return {(r - min_r, c - min_c) for r, c in positions}

def main():
    input_lines = [line.rstrip('\n') for line in sys.stdin if line.strip() != '']
    for i in range(0, len(input_lines), 8):
        grid = input_lines[i:i+8]
        positions = {(r,c) for r in range(8) for c in range(8) if grid[r][c] == '1'}
        norm = normalize(positions)
        for k,v in shapes.items():
            if norm == v:
                print(k)
                break

if __name__ == "__main__":
    main()