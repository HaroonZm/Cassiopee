s=input()
sy=int(s[:2])
sm=int(s[2:])

if 1<=sy<=12 and 1<=sm<=12:
    print('AMBIGUOUS')
elif 1<=sy<=12:
    print('MMYY')
elif 1<=sm<=12:
    print('YYMM')
else:
    print('NA')