W,H,c = input().split()
W,H = int(W),int(H)
for i in range(H):
    for j in range(W):
        if (j,i) == (0,0) or (j,i) == (0,H-1) or (j,i) == (W-1,0) or (j,i) == (W-1,H-1):
            print('+',end='')
        elif j in (0,W-1):
            print('|',end='')
        elif i in (0,H-1):
            print('-',end='')
        elif (j,i) == ((W-1)//2,(H-1)//2):
            print(c,end='')
        else:
            print('.',end='')
    print()