n,k = map(int, input().split())
square = [[0 for i in range(k*2)] for j in range(k*2)]
 
for i in range(n):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    if c=='W':
        y += k
    x = x%(k*2)
    y = y%(k*2)
    square[x][y] += 1
 
class CumulativeSum2d():
    def __init__(self, collection_2d):
        yl = len(collection_2d)
        xl = len(collection_2d[0])
        self.data = [[0] * (xl+1) for _ in range(yl+1)]
        for y in range(1, yl+1):
            for x in range(1, xl+1):
                top_sum         = self.data[y-1][x]
                left_sum        = self.data[y][x-1]
                dup_sum         = self.data[y-1][x-1]
                self.data[y][x] = top_sum + left_sum - dup_sum
                self.data[y][x] += collection_2d[y-1][x-1]
 
    def query(self, x, y, x1, y1):
        return self.data[y1][x1] - self.data[y-1][x1] - self.data[y1][x-1] + self.data[y-1][x-1]
 
cs = CumulativeSum2d(square)
 
"""
xxxxxx
xxxxxx
xxxxxx
xxxxxx
xxxxxx
xxxxxx
 
oxxxoo
oxxxoo
oxxxoo
xoooxx
xoooxx
xoooxx
 
0xxxoo
x000xx
x000xx
x000xx
0xxxoo
0xxxoo
 
xoooxx
oxxxoo
oxxxoo
oxxxoo
xoooxx
xoooxx
 
1 k  2k
xxxooo
xxxooo
xxxooo
000xxx
000xxx
000xxx
 
          1xk  2k
         10xxxoo
         yx000xx
         kx000xx
          x000xx
          0xxxoo
        2k0xxxoo
 
left top position determine everything
"""
ans = 0
for x in range(1,k*2+1):
    for y in range(1,k*2+1):
        sumd = 0
        # main_area
        sumd += cs.query(x, y, min(k*2, x+k-1), min(k*2, y+k-1))
        """
        """
        if x-k>1:
            # left_area
            sumd += cs.query(1, y, x-k-1, min(k*2, y+k-1))
        if y-k>1:
            # top_area
            sumd += cs.query(x, 1, min(k*2, x+k-1), y-k-1)
        if x>1 and y>1:
            # left_top_area
            sumd += cs.query(max(1, x-k), max(1, y-k), x-1, y-1)
        if x>1 and y-k<1:
            # left_bottom_area
            sumd += cs.query(max(1, x-k), y+k, x-1, k*2)
        if x-k<1 and y>1:
            # right_top_area
            sumd += cs.query(x+k, max(1, y-k), k*2, y-1)
        if x-k<1 and y-k<1:
            # right_bottom_area
            sumd += cs.query(x+k, y+k, k*2, k*2)
        ans = max(sumd, ans)
 
print(ans , flush=True)