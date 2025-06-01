def getPaintCount(string, color):
	return len(string)-string.count(color)

def read_dimensions():
	return map(int, input().split())

def read_input_lines(n):
	lines = []
	for _ in range(n):
		lines.append(input().strip())
	return lines

def process_first_line(s):
	return getPaintCount(s, 'W')

def process_last_line(s):
	return getPaintCount(s, 'R')

def process_middle_lines(lines):
	return lines

def generate_combinations(n):
	combinations = []
	for w in range(0, n-1):
		for b in range(1, n-w):
			r = n-2-w-b
			if r >= 0:
				combinations.append([w, b, r])
	return combinations

def count_paints_for_range(line, color):
	return getPaintCount(line, color)

def calculate_paint_counts_for_combination(A, combination):
	total = 0
	w, b, r = combination
	for i in range(len(A)):
		if i < w:
			total += count_paints_for_range(A[i], 'W')
		elif w <= i < w + b:
			total += count_paints_for_range(A[i], 'B')
		elif w + b <= i < w + b + r:
			total += count_paints_for_range(A[i], 'R')
	return total

def main():
	N, M = read_dimensions()
	raw_lines = read_input_lines(N)
	cnt = 0
	A = []
	for i in range(N):
		s = raw_lines[i]
		if i == 0:
			cnt += process_first_line(s)
		elif i == N-1:
			cnt += process_last_line(s)
		else:
			A.append(process_middle_lines([s])[0])
	combinations = generate_combinations(N)
	minmin = 2500
	for comb in combinations:
		cnt2 = calculate_paint_counts_for_combination(A, comb)
		if cnt2 < minmin:
			minmin = cnt2
	print(cnt + minmin)

main()