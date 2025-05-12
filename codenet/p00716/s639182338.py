def tanri(money, year, ritu, cost):
	temp = int(year*(money+cost)*ritu)
	temp -= (ritu * cost*year*(year-1))//2
	return temp

def tanri_a(m,y,r,c):
	temp = m
	ans = 0
	for _ in range(y):
		ans += int(temp*r)
		temp -= c
	return ans + temp

def hukuri(m, y, r, c):
	temp = (m-c/r)*((1+r)**(y-1))
	return int(temp)

def hukuri_a(m, y, r, c):
	temp = m
	for i in range(y):
		temp = temp + int(temp*r) - c
	return int(temp)

def main(init_money):
	year = int(input())
	n = int(input())
	ans = 0
	for _ in range(n):
		temp = input().split()
		w, ritsu, cost = int(temp[0]), float(temp[1]), int(temp[2])
		# if w == 0: temp = tanri(init_money, year, ritsu, cost)
		# else: temp = hukuri(init_money, year, ritsu, cost)
		if w == 0: temp2 = tanri_a(init_money, year, ritsu, cost)
		else: temp2 = hukuri_a(init_money, year, ritsu, cost)
		ans = max(ans, temp2)
		# print(f"temp: {temp}, temp2: {temp2}, diff: {temp-temp2}")
	print(ans)
	return
		
n = int(input())
for _ in range(n):
	main(int(input()))