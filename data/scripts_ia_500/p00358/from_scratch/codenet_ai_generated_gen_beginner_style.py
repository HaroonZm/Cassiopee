H, N = map(int, input().split())
blocked = set()
for _ in range(N):
    x, y = map(int, input().split())
    blocked.add((x, y))

count = 0
for y in range(H - 1):
    for x in range(3):
        # Vérifier les 4 partitions 2x2 carrées: (x,y), (x+1,y), (x,y+1), (x+1,y+1)
        if ((x, y) not in blocked and 
            (x + 1, y) not in blocked and 
            (x, y + 1) not in blocked and 
            (x + 1, y + 1) not in blocked):
            count += 1
print(count)