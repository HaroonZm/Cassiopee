L,S=input().split()
L=int(L)
def find_chains(S):
    chains=[]
    i=0
    while i<L:
        if S[i] in 'BW':
            c=S[i]
            start=i
            while i+1<L and S[i+1]==c:
                i+=1
            chains.append((start,i,c))
        i+=1
    return chains

def surrounded(S,start,end,color):
    opp={'B':'W','W':'B'}
    if start==0 or end==L-1:
        return False
    return S[start-1]==opp[color] and S[end+1]==opp[color]

def count_captured(S):
    chains=find_chains(S)
    captured=0
    for start,end,color in chains:
        if surrounded(S,start,end,color):
            captured+=end-start+1
    return captured

max_capt=0
for i,c in enumerate(S):
    if c=='.':
        new_S=S[:i]+'W'+S[i+1:]
        chains=find_chains(new_S)
        white_surrounded=False
        for start,end,color in chains:
            if color=='W' and surrounded(new_S,start,end,color):
                white_surrounded=True
                break
        if white_surrounded:
            continue
        cap=count_captured(new_S)
        if cap>max_capt:
            max_capt=cap
print(max_capt)