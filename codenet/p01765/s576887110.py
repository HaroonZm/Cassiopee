def PointSegmentDistance(point, begin, end):
	point, begin, end = point-begin, 0, end-begin
	point = (point / end) * abs(end)
	end = abs(end)
	if 0 <= point.real <= abs(end):
		return abs(point.imag)
	else:
		return min(abs(point), abs(point - end))

n1 = int(input())
a = [0]
for _ in range(n1):
	x, y = map(int, input().split())
	a.append(complex(x, y))
a.append(1000)
n2 = int(input())
b = [1000j]
for _ in range(n2):
	x, y = map(int, input().split())
	b.append(complex(x, y))
b.append(1000+1000j)
#print(*a, sep="\n")
ans = 10**30
for p in range(n1+2):
	for q in range(n2+1):
		ans = min(ans, PointSegmentDistance(a[p], b[q], b[q+1]))
for q in range(n2+2):
	for p in range(n1+1):
		ans = min(ans, PointSegmentDistance(b[q], a[p], a[p+1]))
print(ans)