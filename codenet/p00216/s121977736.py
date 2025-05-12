# AOJ 0216 Cutting Down Water Bills
# Python3 2018.6.23 bal4u

while 1:
	w = int(input())
	if w < 0: break
	s = 1150
	if w > 10:
		if w <= 20: s+= (w-10)*125
		else: s += 1250
	if w > 20:
		if w <= 30: s += (w-20)*140
		else: s += 1400
	if w > 30: s += (w-30)*160;
	print(4280-s)