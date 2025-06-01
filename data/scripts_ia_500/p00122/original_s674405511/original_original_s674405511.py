dX = [2,2,2,1,0,-1,-2,-2,-2,-1,0,1]
dY = [-1,0,1,2,2,2,1,0,-1,-2,-2,-2]
def solve(x,y,i):
	if i == 2*n: return True
	sx,sy = xy[i],xy[i+1]
	for dx,dy in zip(dX,dY):
		if doa(x+dx,y+dy,sx,sy): 
			r = solve(x+dx,y+dy,i+2)
			if r: return r

def doa(x,y,sx,sy):
	if not (0 <= x <= 9 and 0 <= y <= 9): return False
	return True if abs(x-sx) < 2 and abs(y-sy) < 2 else False

while 1:
	x,y = map(int,raw_input().split())
	if x == y == 0: break
	n = input()
	xy = map(int,raw_input().split())
	print "OK" if solve(x,y,0) else "NA"