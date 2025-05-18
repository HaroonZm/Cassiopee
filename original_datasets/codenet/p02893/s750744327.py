mod=998244353
import collections
n=int(input())
x=input()
ans=(2*n*(int(x,2)+1))%mod

def make_divisors(n):
  divisors=[]
  for i in range(1,int(n**0.5)+1):
    if n%i==0:
      divisors.append(i)
      if i!=n//i:
        divisors.append(n//i)

  divisors.sort(reverse=True)
  return divisors
D=make_divisors(n)
CT=collections.defaultdict(int)
for d in D:
  if d%2==0 or d==1:
    continue
  else:
    k=n//d
    #下から0がk個、1がk個、、、、を繰り返す数を求める、ｙとする。
    #その周期は2*k
    y=(2**n-2**k)//(2**k+1)

    #ｙ+（ｙ＋１）*yyも同じ周期をもつ
    #x以下の個数を数える
    ct=(int(x,2)-y)//(y+1)+1
    #重複分を差し引く
    Dk=make_divisors(k)
    for dk in Dk:
      if dk<k:
        ct-=CT[dk]
    CT[k]=ct

    #ansはすべてを2nで数えているのでそこから2(n-k)を引く
    ans-=ct*2*(n-k)

print(ans%mod)