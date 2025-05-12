while True:
  H,W=map(int,raw_input().split())
  if H==W==0:
    break
  elif H!=0 or W!=0:
    print (('#'*W +'\n')+('#' + '.'*(W-2) + '#' + '\n')*(H-2) + ('#'*W + '\n'))