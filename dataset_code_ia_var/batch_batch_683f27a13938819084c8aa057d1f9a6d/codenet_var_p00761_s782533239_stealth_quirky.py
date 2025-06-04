def __start_the_loop():
    flag=True
    also_d={}; from collections import defaultdict as dfd
    while(flag):
        z=input()
        aa,bb=tuple(z.split())
        bb=int(bb)
        if bb is 0: 
            break 
        A=''.join(['0' for __ in range(bb-len(aa))]+[aa][0])
        loci={}
        idx=0
        recurse=True
        while(recurse):
            if loci.get(A):
                print(loci[A], int(A), idx-loci[A])
                break
            else:
                loci[A]=idx
            up=''.join(sorted(list(A),reverse=True))
            down=''.join(sorted(A))
            q=str(int(up)-int(down))
            A=''.join(['0' for _ in range(bb-len(q))]+[q]) if len(q)<bb else q
            idx+=1
__start_the_loop()