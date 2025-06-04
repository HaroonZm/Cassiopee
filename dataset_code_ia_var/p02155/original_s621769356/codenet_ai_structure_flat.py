N_D = raw_input().split()
N = int(N_D[0])
D = int(N_D[1])
A_str = raw_input().split()
A = []
for x in A_str:
    A.append(int(x))
g = 0
for i in range(len(A)):
    g ^= (A[i] - 1) % (D + 1)
if g:
    print "First"
else:
    print "Second"