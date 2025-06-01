from collections import defaultdict as dd

def main():
    while 1:
        n = int(input())
        if not n:
            return
        
        I = dd(set)
        C = dd(int)
        
        for __ in[0]*n:
            L = input().split()
            [ (I[w[0]].add(w), C.__setitem__(w, C[w]+1)) for w in L ]
        
        k = input()
        A = list(I[k])
        
        if A == []:
            print('NA')
            continue
        
        A.sort()
        A.sort(key=C.get, reverse=True)
        
        print(* (A if len(A) < 5 else A[:5]))
        
if __name__=="__main__":
    main()