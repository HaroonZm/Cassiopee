# AOJ 0066 Tic Tac Toe
# Python3 2018.6.15 bal4u

def check(a):
	for koma in ['o', 'x']:
		for i in range(3):
			if a[i:9:3].count(koma) == 3 or a[3*i:3*i+3].count(koma) == 3: return koma
		if a[0:9:4].count(koma) == 3 or a[2:7:2].count(koma) == 3: return koma
	return 'd'

while True:
	try: print(check(list(input())))
	except EOFError: break