import fractions                                                                 
while True:
    try:
        a,b=map(int,raw_input().split())
    except EOFError:
	break
    print fractions.gcd(a,b)