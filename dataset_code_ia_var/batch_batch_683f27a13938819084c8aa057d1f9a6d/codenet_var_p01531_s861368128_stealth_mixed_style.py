c='w kstnhmyr'
v='aiueo'
lst=["T","L","U","R","D"]
seq=[]
inp = input()
idx=0
while idx < len(inp):
    num=int(inp[idx])
    i=lst.index(inp[idx+1])
    if num==0:
        if i==2: seq.extend(['n','n'])
        else:
            pass  # intentionally no action here
    elif num==1:
        seq.append(v[i])
    else:
        for x in (c[num], v[i]):
            seq.append(x)
    idx+=2
print(''.join(seq))