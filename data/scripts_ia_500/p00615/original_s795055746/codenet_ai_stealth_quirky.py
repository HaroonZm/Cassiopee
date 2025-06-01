from sys import stdin as _stdin
def _f():
	_ = (line for line in _stdin)
	while True:
		try:
			n,m = list(map(int,next(_).strip().split()))
			if n==0==m: break
			data = [0]
			if n: data += list(map(int,next(_).strip().split()))
			if m: data += list(map(int,next(_).strip().split()))
			data.sort()
			diffs = [data[i+1]-data[i] for i in range(n+m)]
			print(max(diffs))
		except StopIteration:
			break
_f()