import sys
import bisect

MAX = 1299710
prime = [-1] * MAX
prime_list = []
i = 2
while MAX > i:
	if prime[i - 1] == -1:
		prime[i - 1] = 0
		temp = i * 2
		prime_list.append(i)
		while temp < MAX:
			prime[temp - 1] = 1
			temp += i
	if i == 2:
		i += 1
	else:
		i += 2

while True:
    n = int(sys.stdin.readline())
    
    if n == 0:
        break
    
    start = bisect.bisect_left(prime_list, n)
    end = bisect.bisect_right(prime_list, n)
    if prime_list[start] == n:
        print 0
    else:
        print prime_list[end] - prime_list[start - 1]