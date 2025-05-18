#ABC 58, B - dot dot dot
O = input()
E = input()

S = ''
for o, e in zip(O, E):
    S = S + o + e
if len(O) > len(E):
    print(S + O[-1])
else:
    print(S)