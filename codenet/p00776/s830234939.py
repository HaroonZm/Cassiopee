ans=[""]
ans.pop()
s=""
w=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","}"]
x=[0]
x.pop()
def uni(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def check(a):
	global s
	global w
	n=len(a)
	# print "before ",a
	for i in range(26):
		if i==0:
			continue
		a=a.replace(w[i],w[i-1],1);
	# print "after ",a
	if a==s[0:n]:
		return True
	else:
		return False

def foo(a,n):
	# print a
	global ans
	global x
	if n==len(a):
		if check(a):
			ans.append(a)
		return
	sz=len(a)
	t=a+s[sz]
	if check(t):
		foo(t,n)
	if w[x[sz]]=="z":
		return
	t=a+w[x[sz]+1]
	# print t
	if check(t):
		# print t
		foo(t,n)

while True:
	s = raw_input()
	if s=="#":
		break
	ans=[""]
	ans.pop()
	x=[0]
	x.pop()
	for i in range(len(s)):
		for j in range(26):
			if w[j]==s[i]:
				x.append(j)
	# print s
	foo("",len(s))
	# ans=uni(ans)
	ans.sort()
	if len(ans)<=10:
		print len(ans)
		for i in range(len(ans)):
			print ans[i]
	else:
		print len(ans)
		for i in range(5):
			print ans[i]
		for i in range(5):
			print ans[len(ans)-5+i]