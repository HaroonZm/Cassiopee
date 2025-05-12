pp = list(map(int, input().split()))
n = int(input())

def project(bb, p=pp):
    ans = []
    a = (p[2]-p[0], p[3]-p[1])
    b = (bb[0]-p[0], bb[1]-p[1])
    if dot(a,b)<0:
        a = (-a[0], -a[1])
    c = dot(a,b)/length(a)**2
    ans += [c*v+p[i] for i, v in enumerate(a)] 
    return ans
    
def length(vector):
    ans = 0
    for i in vector:
        ans += i**2
    return ans**(1/2)
    
def dot(a, b):
    n = len(a)
    if n != len(b):
        return None
    ans = 0
    for i, j in zip(a, b):
        ans += i*j
    return ans
    
def reflection(b, p = pp):
    a = project(b)
    ans = (b[0]+2*(a[0]-b[0]), b[1]+2*(a[1]-b[1]))
    print(f'{ans[0]:.8f} {ans[1]:.8f}')
    
for i in range(n):
    b = list(map(int, input().split()))
    reflection(b)