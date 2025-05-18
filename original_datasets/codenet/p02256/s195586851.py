def gcd(a,b):
	if a%b==0:
		return b
	else :
		return gcd(b,a%b)

def main():
	a,b=map(int,raw_input().split())
	print(gcd(a,b))

if __name__=='__main__':
	main()