import bisect

n,l,t = map(int, input().split())
xw = [list(map(int, input().split())) for i in range(n)]
clockwise = []
anticlockwise = []
ans = [None] * n
for key,(x,w) in enumerate(xw):
    if w == 1:
        clockwise.append((x,key))
    else:
        anticlockwise.append((x,key))

len_c = len(clockwise)
len_a = len(anticlockwise)
for key,(x,w) in enumerate(xw):
    if w == 1:
        tmp = bisect.bisect_right(anticlockwise, ((2*t+x)%l,1000000)) - bisect.bisect_right(anticlockwise,(x,0))
        lap = (x+2*t) // l
        num = (key + tmp + lap * len_a) % n
        ans[num] = (x + t) % l
    else:
        tmp = bisect.bisect_left(clockwise, (x,-1)) - bisect.bisect_left(clockwise, ((x-2*t)%l,-1))
        lap = (x-2*t) // l
        num = (key - tmp + lap * len_c) % n
        ans[num] = (x - t) % l

for i in ans:
  print(i)