class T:
	def __init__(self, h, w):
		self.h = h
		self.w = w
		self.d = w*w + h*h
	def __lt__(self, other):
		return (self.d < other.d) or ((self.d == other.d) and self.h < other.h)
	def __gt__(self, other):
		return (self.d > other.d) or ((self.d == other.d) and self.h > other.h)

t = []
for i in range(1, 151):
	for j in range(i+1, 151):
		t.append(T(i, j))
t = sorted(t)

while True:
	h, w = map(int, input().split())
	if (h, w) == (0, 0):
		break
	hw = T(h, w)
	for i in range(len(t)):
		if hw < t[i]:
			print('{} {}'.format(t[i].h, t[i].w))
			break