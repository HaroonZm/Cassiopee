A = {}
while True:
    S = input()
    if S == '':
        break
    x,y = map(int,S.split(','))
    if x in A:
        A [x] += 1
    else:
        A [x] = 1

B = {}
while True:
    try:
        x,y = map(int,input().split(','))
    except EOFError:
        break
    if x in B:
        B [x] += 1
    else:
        B [x] = 1

for i in A.keys():
    if i in B:
        print(i,A [i] + B [i])