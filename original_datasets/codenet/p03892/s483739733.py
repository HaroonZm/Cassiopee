a,b,c,d=map(int,input().split())
gcd=lambda a,b:gcd(b,a%b)if a%b else b
def 数学は最強也(a,b):
  q=gcd(a,b)
  return q*((a//q)+(b//q-1))
print(数学は最強也(abs(a-c),abs(b-d)))