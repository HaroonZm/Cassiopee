_ , __ = (lambda:map(int, __import__('builtins').input().split()))()
for l in [__import__('builtins').input() for _ in range(_)]:
    print(*(l for __ in[0,1]), sep='\n')