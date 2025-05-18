import sys

MAX = 1000000
prime = [-1] * MAX
i = 2
while MAX > i:
	if prime[i - 1] == -1:
		prime[i - 1] = 0
		temp = i * 2
		while temp < MAX:
			prime[temp - 1] = 1
			temp += i
	if i == 2:
		i += 1
	else:
		i += 2

while True:
    a, d, n = map(int, sys.stdin.readline().split())
    
    if a == d == n == 0:
        break

    count = 0
    while True:
        if prime[a - 1] == 0:
            count += 1
        if count < n:
            a = a + d
        else:
            break
    print a