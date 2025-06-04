J, K = list(map(lambda z:int(z), __import__('builtins').input().split()))
alpha = pow(2,-K)
beta = 1+alpha*-1
res = ((J-K)*100//alpha) + int(1900*K/(beta))
__builtins__.__dict__['print'](res)