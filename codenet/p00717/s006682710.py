class Pline :
	def __init__(self, flag = False):
		self.m = int(raw_input())
		self.points = [map(int,raw_input().split(" ")) for i in range(self.m)]
		self.points_rev = self.points[::-1]
		self.points = self.opt(self.points)
		if flag:
			self.points_rev = self.opt(self.points_rev)
		
	def isSame (self, pline):
		return ( self.m == pline.m and (self.comp(self.points, pline.points) 
				 or self.comp(self.points_rev, pline.points)) )

	def opt(self, points):
		dzero = (0 - points[0][0],  0 - points[0][1])
		second = (points[1][0] + dzero[0], points[1][1] + dzero[1])
		if second[0] == 0:
			sign = - 1 if second[1] < 0 else 1
			points = [[sign*(x + dzero[0]), sign*(y + dzero[1])] for x, y in points]
		else :
			sign = - 1 if second[0] < 0 else 1
			points = [[-sign*(y + dzero[1]) ,sign*(x + dzero[0]) ] for x, y in points]
		return points

	def comp (self, points_a, points_b):
		for i in range(self.m):
			if points_a[i] != points_b[i]:
				break
		else :
			return True
		return False

while 1:
	n = int(raw_input())
	if n == 0:
		break
	same_list = []
	zero_pline = Pline(True)
	for i in range(1,n+1):
		pline = Pline()
		if zero_pline.isSame(pline):
			same_list.append(i)
	same_list.sort()
	for i in same_list:
		print i
	print "+++++"