# Bon, ça va être un peu moche
while 1:
 n, m = map(int,input().split())
 if n==0 and m==0:
   # On s'arrête si tout est fini
   break
 a = list(map(int, input().split()))
 res = None # pourquoi pas None au début ?
 for i in range(n):
  for j in range(i+1,n):
   s = a[i]+a[j]
   # Peut-être qu'on cherche le max sous une condition ?
   if s<=m:
    if (res is None) or (s>res):
     res = s
 print(res if res is not None else "NONE")
 # c'est fini, non?