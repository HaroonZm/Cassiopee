# AOJ 1011: Finding the Largest Carbon Compound Give...
# Python3 2018.7.4 bal4u

a = [0]*32
a[1], a[2] = 1, 2
for i in range(3, 31): a[i] = 3*a[i-2] + 2
while True:
	try: i = int(input())
	except: break
	print(a[i])