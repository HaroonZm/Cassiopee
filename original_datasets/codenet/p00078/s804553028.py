def print_board(A,n):
	for i in range(n):
		s = ""
		for j in range(n):
			st = str(A[i][j])
			if len(st) == 1:
				s += "   "
			elif len(st) == 2:
				s += "  "
			elif len(st) == 3:
				s += " "

			s += str(st)
		print(s)

def check_leftdown(A,h,w,n):
	if h + 1 > n - 1:
		#下に抜けるならば,左に-1してその列に値が入っていない箇所を探す
		w -= 1

		for x in range(n):
			if A[x][w] == 0:
				h = x
				break

	else:
		#左に抜けるならば
		if w - 1 < 0:
			w = n
			h += 1
		else:
			h += 1
			w -= 1

	return h,w

def check_rightdown(A,h,w,n):
	if h + 1 > n - 1:

		#下にも右にも抜ける場合
		if w + 1 > n - 1:
			None
		else:
			#下に抜けるならば,右に＋1してその列に値が入っていない箇所を探す
			w += 1

		for x in range(n):
			if A[x][w] == 0:
				h = x
				break

	else:
		if w + 1 > n - 1:
		#右に抜けるならば
			w = 0
			h += 1
		else:
			#通常パターン
			h += 1
			w += 1
			if A[h][w] != 0:
				#値が既に埋まっている
				#左下をチェック
				h,w = check_leftdown(A,h,w,n)

	return h,w

if __name__ == '__main__':

	while True:
		try:
			n = int(input())

			if n == 0:
				break

			A = [[0 for i in range(n)] for j in range(n)]

			cnt = n * n
			for x in range(cnt):
				if x == 0:
					mid = n // 2
					h = mid + 1
					w = mid
					A[h][w] = x + 1
				else:
					h,w = check_rightdown(A,h,w,n)
					A[h][w] = x+1

			print_board(A,n)

		except EOFError:
			break