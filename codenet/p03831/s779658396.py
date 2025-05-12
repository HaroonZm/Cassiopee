S1=input()
S1=S1.split()
S2=input()
S2=S2.split()
move=0
N=int(S1[0])
A=int(S1[1])
B=int(S1[2])
for i in range(N-1):
    div=int(S2[i+1])-int(S2[i])
    if (div)*A>=B:
        move+=B
    else:
        move+=A*(div)
print(move)