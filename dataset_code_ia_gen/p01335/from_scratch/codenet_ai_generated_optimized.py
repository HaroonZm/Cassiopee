import sys
ranks_map = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13}
def is_straight(rs):
    sr=sorted(rs)
    if all(sr[i]+1==sr[i+1] for i in range(4)):
        return True
    if set(sr)=={1,10,11,12,13}:
        return True
    return False
def hand_rank(cards):
    #cards: list of (rank,suit)
    ranks=[c[0] for c in cards]
    suits=[c[1] for c in cards]
    counts={}
    for r in ranks:counts[r]=counts.get(r,0)+1
    vals=sorted(counts.values(),reverse=True)
    uniq_ranks=sorted(counts.items(),key=lambda x:(-x[1],-x[0]))
    flush=len(set(suits))==1
    straight=is_straight(ranks)
    if straight and flush and set(ranks)=={1,10,11,12,13}:
        return 8 #'Royal Straight Flush'
    if straight and flush:
        return 7 #'Straight Flush'
    if vals[0]==4:
        return 6 #'Four of a kind'
    if vals==[3,2]:
        return 5 #'Full house'
    if flush:
        return 4 #'Flush'
    if straight:
        return 3 #'Straight'
    if vals[0]==3:
        return 2 #'Three of a kind'
    if vals==[2,2,1]:
        return 1 #'Two pairs'
    if vals==[2,1,1,1]:
        return 0 #'One pair'
    return -1 #No pair

first=True
lines=sys.stdin.read().rstrip('\n ').split('\n')
i=0
while i<len(lines):
    if not lines[i].strip():
        i+=1
        continue
    N=int(lines[i]); i+=1
    base_points=[] #4x13
    for _ in range(4):
        base_points.append(list(map(int,lines[i].split())))
        i+=1
    multipliers=list(map(int,lines[i].split()))
    i+=1
    if not first:
        print()
    first=False
    for _ in range(N):
        hand=lines[i].split()
        i+=1
        cards=[]
        total_base=0
        ranklist=[]
        suitlist=[]
        for c in hand:
            r,s=c[0],c[1]
            rv=ranks_map[r]
            sv={'S':0,'C':1,'H':2,'D':3}[s]
            cards.append((rv,sv))
            total_base+=base_points[sv][rv-1]
            ranklist.append(rv)
            suitlist.append(sv)
        ranklist.sort()
        rnk=hand_rank(cards)
        #rnk index: -1:nopair,0:one pair,1:two pairs,2:three,3:straight,4:flush,5:fullhouse,6:four,7:straightflush,8:royal straight flush
        if rnk==-1:
            score=0
        else:
            score=total_base*multipliers[rnk]
        print(score)