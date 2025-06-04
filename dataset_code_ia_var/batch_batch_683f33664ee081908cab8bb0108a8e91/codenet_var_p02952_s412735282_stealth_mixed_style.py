N = int(input())
def f(n): return sum([1 if len(str(x)) & 1 else 0 for x in range(1, n + 1)])
result = 0
if N>0:
    for number in range(1,N+1):
        if (lambda y: True if len(str(y))%2 else False)(number):
            result+=1
print(f(N) if N%2==0 else result)