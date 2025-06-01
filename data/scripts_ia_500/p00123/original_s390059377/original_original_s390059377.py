import sys

for line in sys.stdin:
	[p, q] = line.split();
	a = float(p);
	b = float(q);
	
	if (a < 35.5) & (b < 71.0):
		print('AAA');
	elif (a < 37.5) & (b < 77.0):
		print('AA');
	elif (a < 40.0) & (b < 83.0):
		print('A');
	elif (a < 43.0) & (b < 89.0):
		print('B');
	elif (a < 50.0) & (b < 105.0):
		print('C');
	elif (a < 55.0) & (b < 116.0):
		print('D');
	elif (a < 70.0) & (b < 148.0):
		print('E');
	else:
		print('NA');