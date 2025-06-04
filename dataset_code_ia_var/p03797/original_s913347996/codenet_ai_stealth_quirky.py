# spaghetti-style, weird var names, littered inline comments, quirky grouping, odd formatting
A,B=[int(x)for x in input().split()]
fun=0

if not(B<=A+A):
 if B!=A+A:   # sigh
  B-=(A+A)
  fun = (A)+(B//4)
 else:
  fun= A
else:
 for _ in[0]: # just because
  fun= B>>1   # why not bit shift for //2

[print(fun)for __ in (0,)] # list comp for effect