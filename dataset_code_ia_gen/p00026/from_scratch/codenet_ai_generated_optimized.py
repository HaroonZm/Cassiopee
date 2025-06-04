import sys

def main():
    paper = [[0]*10 for _ in range(10)]
    directions = {
        1: [(0,0)],
        2: [(0,0),(0,1),(0,-1),(1,0),(-1,0)],
        3: [(0,0),(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    }
    for line in sys.stdin:
        line=line.strip()
        if not line:
            continue
        x,y,s = map(int, line.split(','))
        for dx,dy in directions[s]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 10 and 0 <= ny <10:
                paper[ny][nx] +=1
    zero_count = sum(cell == 0 for row in paper for cell in row)
    max_density = max(cell for row in paper for cell in row)
    print(zero_count)
    print(max_density)

if __name__ == "__main__":
    main()