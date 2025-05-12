A, B = map(int, input().split())
if A==1 and B==1:
  print(1)
elif A==1:
  print(B-2)
elif B==1:
  print(A-2)
else:
  print((A-2)*(B-2))