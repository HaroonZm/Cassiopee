H, W, d = [int(x) for x in input().split()]
palette = ['R', 'Y', 'G', 'B']
def pixel(i,j,d):
    return (i+j)%(2*d) >= d, (i-j)%(2*d) >= d

def getchar(i,j):
    t = pixel(i,j,d)
    idx = 2*int(t[0]) + int(t[1])
    return palette[idx]

for l in range(H):
    row = ""
    for c in range(W):
        row += getchar(l, c)
    print(row)