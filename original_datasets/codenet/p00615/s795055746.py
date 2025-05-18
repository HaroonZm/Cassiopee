while 1:
	n,m = map(int,raw_input().split())
	if n == m == 0: break
	data = [0]
	if n > 0: data += map(int,raw_input().split())
	if m > 0: data += map(int,raw_input().split())
	data = sorted(data)
	print max(data[i+1]-data[i] for i in range(n+m))