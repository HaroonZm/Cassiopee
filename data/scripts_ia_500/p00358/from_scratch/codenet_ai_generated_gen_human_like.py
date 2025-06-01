H, N = map(int, input().split())
inhibited = set()
for _ in range(N):
    x, y = map(int, input().split())
    inhibited.add((x, y))

count = 0
# The cargo pieces occupy 2x2 squares aligned on the 1x1 grid.
# Each piece covers positions: (x,y), (x+1,y), (x,y+1), (x+1,y+1)
# The grid is 4 wide (x from 0 to 3), so possible x for pieces are 0 and 1 and 2 since piece size is 2.
# Actually width is 4, so x in [0,1,2], because piece occupies x and x+1.
# Height is H, so y in [0..H-2]

for y in range(H - 1):
    for x in range(3):  # x=0,1,2 for 2x2 square within width 4
        # check if any of the 4 partitions is inhibited
        if (x, y) in inhibited:
            continue
        if (x + 1, y) in inhibited:
            continue
        if (x, y + 1) in inhibited:
            continue
        if (x + 1, y + 1) in inhibited:
            continue
        count += 1

print(count)