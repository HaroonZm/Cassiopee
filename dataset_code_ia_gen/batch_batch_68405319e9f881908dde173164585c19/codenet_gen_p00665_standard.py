import sys
input=sys.stdin.readline

while True:
    N,M,K,L=map(int,input().split())
    if N==0 and M==0 and K==0 and L==0: break
    chars=[]
    name_to_index={}
    for i in range(N):
        s,v=input().split()
        v=int(v)
        chars.append([s,v,i])
        name_to_index[s]=i
    favs=[input().strip() for _ in range(M)]
    fav_set=set(favs)
    chars.sort(key=lambda x:(-x[1],x[0]))
    rank=[0]*N
    for i,(s,v,j) in enumerate(chars):
        rank[j]=i
    def can(x):
        # can we put x fav chars in top K?
        # assign L votes to these x fav chars to move them up if needed
        # the rest fav chars not promoted
        # check if condition holds after allocation
        promoted = sorted(favs)
        # choose top x fav chars to promote in lex order for consistency
        # actually, better to choose the x fav chars with easiest promotion
        # but lex order imposed for tie-breaks
        promoted = sorted(favs)
        # in practice, try all subsets would be too large, so pick top x fav chars by their current rank (easy to promote)
        # Simplify: pick fav chars with lowest rank (highest position), should be easiest to keep in top K
        fav_ranks = [(rank[name_to_index[f]], f) for f in favs]
        fav_ranks.sort()
        selected = [f for _,f in fav_ranks[:x]]
        selected_set=set(selected)
        # For selected fav chars, determine minimal votes needed to be at least at position K-1
        # For each char, minimal vote to surpass the char currently at K-1
        threshold_idx = K-1
        if threshold_idx>=len(chars): threshold_idx=len(chars)-1
        threshold_votes = chars[threshold_idx][1]
        # if tie in votes at K-1 position, must consider lex order as well
        threshold_name = chars[threshold_idx][0]
        # For each selected fav char, calculate votes needed to enter top K:
        needed = []
        for f in selected:
            idx = name_to_index[f]
            cur_vote = chars[rank[idx]][1]
            # to surpass threshold_votes, vote should be > threshold_votes
            # if equal, lex order used: if f < threshold_name, equal votes suffice, else need +1
            if cur_vote > threshold_votes:
                need=0
            elif cur_vote == threshold_votes:
                if f < threshold_name:
                    need=0
                else:
                    need=1
            else:
                need=threshold_votes - cur_vote +1
            needed.append(need)
        total_needed=sum(needed)
        if total_needed > L:
            return False
        # After assigned votes, check if the promoted fav chars can be in top K
        # build final votes list
        final_votes={}
        for s,v,_ in chars:
            final_votes[s]=v
        for f,add in zip(selected,needed):
            final_votes[f]+=add
        # Sort final by votes desc, name asc
        final_sorted = sorted(final_votes.items(),key=lambda x:(-x[1],x[0]))
        # count how many fav chars among top K
        count=0
        topK_names = set([final_sorted[i][0] for i in range(K)])
        for f in favs:
            if f in topK_names:
                count+=1
        return count>=x

    low=0
    high=M
    ans=0
    while low<=high:
        mid=(low+high)//2
        if can(mid):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    print(ans)