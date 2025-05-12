N = int(input())
prime_number = [2, 3, 5, 7]
prim = [2, 3, 5, 7]

#素数作成
for i in range(2, 101):
	prime_flag = True
	for j in prim:
		if i % j == 0:
			prime_flag = False
			break
			
	if prime_flag:
		prime_number.append(i)
	
prime_factor = [0] * len(prime_number)

for i in range(2, N + 1):
	tmp = i
	for j in range(len(prime_number)):
		while tmp % prime_number[j] == 0:
			prime_factor[j] += 1
			tmp //= prime_number[j]
			
count2 = 0
count4 = 0
count14 = 0
count24 = 0
count74 = 0

for i in prime_factor:
	if i >= 2:
		count2 += 1
	if i >= 4:
		count4 += 1
	if i >= 14:
		count14 += 1
	if i >= 24:
		count24 += 1
	if i >= 74:
		count74 += 1

if count4 >= 2:		
	combination4 = count4 * (count4 - 1) // 2
else:
	combination4 = 0
	
ans = combination4 * (count2 - 2) + count14 * (count4 - 1) + count24 * (count2 - 1) + count74
print(ans)