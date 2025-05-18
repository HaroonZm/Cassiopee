import sys
a = 'abcdefghijklmnopqrstuvwxyz'
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in sys.stdin:
	t= s[:-1].translate(str.maketrans(a,b))
	print(t)