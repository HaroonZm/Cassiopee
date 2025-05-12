N=int(input())

input_=[N]
for n in range(N):
    input_.append(input())
    
P=[]
for n in range(N):
    P.append(int(input_[n+1].split()[0]))
    
P.append(int(input_[n+1].split()[1]))

M=[[0]*(N) for x in range(N)]

for n in range(1,N):
    for i in range(N-n):
        M[i][i+n]=10**100
        for k in range(i,i+n):
            P_0=P[i]
            P_1=P[k+1]
            P_2=P[i+n+1]
            M_=M[i][k]+M[k+1][i+n]+P_0*P_1*P_2
            M[i][i+n]=min(M[i][i+n],M_)
            
print(M[0][-1])