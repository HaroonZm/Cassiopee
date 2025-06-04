L,S,C=[*input()],1,0
while L:
 W=L.pop(0)
 ((lambda:globals().update(S=0))() if W=='A' and S else
  (lambda:globals().update(S=1,C=C+1))() if W=='Z' and not S else None)
print(''.join(['A','Z']*C) if C else (0-1))