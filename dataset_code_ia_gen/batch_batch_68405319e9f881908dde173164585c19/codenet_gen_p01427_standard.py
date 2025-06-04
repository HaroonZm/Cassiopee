import sys
sys.setrecursionlimit(10**7)
H,W=map(int,input().split())
G=[input() for _ in range(H)]

# Convert to coordinates: origin at bottom-left
# Mami shoots from bottom-left corner (0,0)
# Let's collect the edges of '#' blocks and find unique lines from (0,0) to block corners

points=set()
for i in range(H):
    for j in range(W):
        if G[i][j]=='#':
            # Coordinates: x=j,y=H-1 - i (y=0 bottom row)
            x,y = j,H-1 - i
            # Add all four corners of the block
            points.add((x,y))
            points.add((x+1,y))
            points.add((x,y+1))
            points.add((x+1,y+1))

# Remove the origin if present
if (0,0) in points:
    points.remove((0,0))

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

directions=set()
for x,y in points:
    dx,dy = x,y
    if dx==0 and dy==0:
        continue
    g = gcd(abs(dx),abs(dy))
    dx//=g
    dy//=g
    directions.add((dx,dy))

print(len(directions)+1)