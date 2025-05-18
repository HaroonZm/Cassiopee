while True:
  goukei=0
  max=0
  min=1000

  n=int(input())
  if n==0:
     break
  else:
   for i in range (n):
     i=int(input())
     if i>max:
         max=i
     if i<min:
         min=i
     goukei=goukei+i 
     heikin=(goukei-max-min)//(n-2)
   print(heikin)