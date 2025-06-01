from functools import reduce

class BugPartySolver:
	def __init__(self):
		self.records = []
		self.heap = []
		self.sum_start = 0
		self.count = 0
		self.max_bugs = 0

	def add(self, a_b):
		a, b = a_b
		self.sum_start += a
		from heapq import heappush, heappop
		heappush(self.heap, (b, a))
		self.count += 1
		while self.count and self.count * self.heap[0][0] < self.sum_start:
			self.sum_start -= self.heap[0][1]
			heappop(self.heap)
			self.count -= 1
		self.max_bugs = max(self.max_bugs, self.count)

	def solve(self):
		return self.max_bugs

def main():
	N = int(input())
	sp = BugPartySolver()
	# Use map + lambda instead of for-loop
	list(map(lambda x: sp.add(tuple(map(int, input().split()))), range(N)))
	print(sp.solve())

if __name__ == "__main__":
	main()