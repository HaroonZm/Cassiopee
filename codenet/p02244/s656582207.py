N = 8 # クイーンの数
n = int(input())

raw = [-1 for i in range(N)]
col = [0 for i in range(N)] # FREE: 0, NOT_FREE: 1
dpos = [0 for i in range(2*N-1)] # FREE: 0, NOT_FREE: 1
dneg = [0 for i in range(2*N-1)] # FREE: 0, NOT_FREE: 1

def put_queen(i):
	if i == N:
		return True
	elif raw[i] != -1:
		if put_queen(i+1):
			return True
		else :
			return False
	else:
		for j in range(N):
			if col[j] == 1 or dpos[i+j] == 1 or dneg[i-j+N-1] == 1:
				continue
			raw[i] = j
			col[j] = dpos[i+j] = dneg[i-j+N-1] = 1
			if put_queen(i+1):
				return True
			else :
				raw[i] = -1
				col[j] = dpos[i+j] = dneg[i-j+N-1] = 0
		return False

def output_result():
	for i in range(N):
		out_raw = ['.' for i in range(N)]
		out_raw[raw[i]] = 'Q'
		print(''.join(map(str, out_raw)))

for i in range(n):
	r, c = map(int, input().split())
	raw[r] = c
	col[c] = dpos[r+c] = dneg[r-c+N-1] = 1

put_queen(0)
output_result()