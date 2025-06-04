S = input()
Y, M = map(lambda x: int(S[x:x+2]), [0,2])

result = { (True, True): 'AMBIGUOUS',
           (True, False): 'MMYY',
           (False, True): 'YYMM'
         }.get((1<=Y<=12, 1<=M<=12), 'NA')

print(result if result else (lambda: None)())