def BubbleSort(C,N):
    for i in range(N):
        for j in range(i+1, N)[::-1]:
            if int(C[j][1]) < int(C[j - 1][1]):
                C[j],C[j-1] = C[j-1],C[j]

def SelectionSort(C,N):
    for i in range(N):
        minj = i
        for j in range(i,N):
            if int(C[j][1]) < int(C[minj][1]):
                minj = j
        C[i],C[minj] = C[minj],C[i]

N = int(input())
C = (input()).split()
ORG = C[:]
BubbleSort(C,N)
print (" ".join(C))
print ("Stable")
C2=ORG
SelectionSort(C2,N)
print(" ".join(C2))
if C == C2:
    print ("Stable")
else:
    print ("Not stable")