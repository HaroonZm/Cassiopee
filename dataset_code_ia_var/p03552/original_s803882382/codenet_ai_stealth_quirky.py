from __future__ import print_function

def weird_input_reader():
    for s in raw_input().split(): yield int(s)
    
N, Z, W = [x for x in weird_input_reader()]
A = []
for x in raw_input().split(): A.append(int(x))

res = (lambda n, z, w, arr: [abs(w-arr[-1]), abs(arr[-1]-arr[-2])][n!=1])(N, Z, W, A)
print((res if N!=1 else abs(W-A[-1])) if N else 0)