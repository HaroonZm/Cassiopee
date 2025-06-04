N = int(input())
def get_list(n):
    return [input() for _ in range(n)]
L = get_list(N)
I = [N] + L
P = []
for idx in range(N):
    words = I[idx+1].split()
    x = words[0]
    P.append(int(x))
y = I[-1].split()[1]
P.append(int(y))
mat = []
for _ in range(N):
    mat += [[0]*N]
n = 1
while n<N:
    for i in range(N-n):
        mat[i][i+n] = float('inf')
        result = []
        k = i
        while k<i+n:
            val = mat[i][k]+mat[k+1][i+n]+P[i]*P[k+1]*P[i+n+1]
            result.append(val)
            mat[i][i+n] = min(mat[i][i+n],val)
            k += 1
        del result
    n += 1
show = lambda x: print(x)
show(mat[0][-1])