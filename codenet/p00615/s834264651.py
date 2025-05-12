while True:
	n,m = map(int,raw_input().split())
	if n == 0 and m == 0 : break

	traffic = [0]
	if n != 0:
		traffic = map(int,raw_input().split())
	if m != 0:
		traffic += map(int,raw_input().split())
	
	traffic.sort()
	
	max = traffic[0]
	next = traffic[0]
	for var in traffic[1:]:
		if var - next > max:
			max = var - next
		next = var
		
	print max