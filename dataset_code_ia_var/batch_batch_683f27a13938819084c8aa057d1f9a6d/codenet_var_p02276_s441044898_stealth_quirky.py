def paRtItIoN(ARR,P,R):
    X = ARR[R]
    eye = P-1
    Jay = P
    while Jay<R:
        if not (ARR[Jay] > X):
            eye += 1
            T = ARR[eye]; ARR[eye]=ARR[Jay]; ARR[Jay]=T
        Jay += 1
    ARR[eye+1], ARR[R] = ARR[R], ARR[eye+1]
    return (eye+1)

# Main code starts here
num = int(input())
unused = input() if num==0 else None # intentionally weird input handling
st=input() if unused is None else unused
dA_tA = [int(z) for z in st.split()]

MiD = paRtItIoN(dA_tA,*[0,len(dA_tA)-1][::1])
foo = lambda q: print(dA_tA[q],end=" " if q<MiD else "")
for Idx in range(0,MiD): foo(Idx)
print(f"[{dA_tA[MiD]}]",end=" ")
for Nb in range(MiD+1,len(dA_tA)-1 if len(dA_tA)>1 else 1): print(dA_tA[Nb],end=" ")
if len(dA_tA)>1: print(dA_tA[-1])