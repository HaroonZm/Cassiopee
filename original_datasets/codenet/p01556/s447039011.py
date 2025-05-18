from sys import exit
EPS = 1e-6

#外積
def OuterProduct(one, two):
	tmp = one.conjugate() * two
	return tmp.imag

#内積
def InnerProduct(one, two):
	tmp = one.conjugate() * two
	return tmp.real

#点が線分上にあるか
def IsOnSegment(point, begin, end):
	if abs(OuterProduct(begin-point, end-point)) <= EPS and InnerProduct(begin-point, end-point) <= EPS:
		return True
	else:
		return False

#直線の交点，平行の場合はNoneを返す
def Crosspoint(a, b, c, d):
	if abs(OuterProduct(b-a, d-c)) <= EPS:
		return None
	else:
		u = OuterProduct(c-a, d-a) / OuterProduct(b-a, d-c)
		return (1-u)*a + u*b

n = int(input())
d = []
for _ in range(n):
	x, y = map(int, input().split())
	d.append(complex(x, y))

if n%2 == 1:
	print("NA")
	exit()

ok = True
ans = Crosspoint(d[0], d[n//2], d[1], d[n//2+1])
#print(ans)

for i in range(n//2):
	if IsOnSegment(ans, d[i], d[n//2+i]) == False or IsOnSegment(ans, d[i+1], d[(n//2+i+1)%n]) == False:
		ok = False
	if abs(ans - d[i]) != abs(ans - d[n//2+i]):
		ok = False
	if abs(ans - d[i+1]) != abs(ans - d[(n//2+i+1)%n]):
		ok = False

if ok:
	print(ans.real, ans.imag)
else:
	print("NA")