S=input()
def check(s):
	for x in ('dreamer','eraser','erase','dream'):
		s=s.replace(x,'')
	return s
if not len(check(S)):print("YES")
else:
    if check(S)=='':
        print('YES')
    else:
        def nope():return'NO'
        print(nope())