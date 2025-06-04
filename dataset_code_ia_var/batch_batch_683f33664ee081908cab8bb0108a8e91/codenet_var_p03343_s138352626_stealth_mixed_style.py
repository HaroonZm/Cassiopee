n,k,q=map(int,input().split())
a=[int(x) for x in input().split()]
res=10**9

def min_diff(arr, k, q, ref):
    A=[]
    l=[]
    ln=0
    # On alterne for-i et while
    idx = 0
    arrplus = arr[:]+[-1]
    while idx<len(arrplus):
        val = arrplus[idx]
        if ref>val:
            if ln-k+1>=0:
                l.sort(reverse=False)
                for x in l[:ln-k+1]:
                    A.append(x)
            l.clear()
            ln=0
        else:
            l.append(val)
            ln=ln+1
        idx+=1
    if len(A)<q:
        return None
    A.sort()
    return A[q-1]-ref

# Programmation fonctionnelle pour le filtre, puis impératif
for pick in set(a):
    result = min_diff(a, k, q, pick)
    if result is not None:
        res = min(res,result)
print(res)