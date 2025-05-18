S=str(input())
l=int(S[0]+S[1])
r=int(S[2]+S[3])
if l<=12 and l>0 and r<=12 and r>0:
  print('AMBIGUOUS')
elif l<=12 and l>0:
  print('MMYY')
elif r<=12 and r>0:
  print('YYMM')
else:
  print('NA')