exec('k,F=map(int,input().split());x=[*range(1,F+1)];'
     'for _ in[0]*k:o=map(int,input().split());n=[*o][1:];x=list(set(x)&set(n));'
     'print(len(x))')