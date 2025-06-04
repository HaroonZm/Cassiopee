import sys
sys.setrecursionlimit(10**7)

def parse(s, i=0):
    if s[i].islower():
        return s[i], i+1
    assert s[i] == '['
    left, ni = parse(s, i+1)
    assert s[ni] == '-'
    right, ni2 = parse(s, ni+1)
    assert s[ni2] == ']'
    return (left, right), ni2+1

def count_wins(tree, wins):
    if isinstance(tree, str):
        return [tree]
    left, right = tree
    l_contestants = count_wins(left, wins)
    r_contestants = count_wins(right, wins)
    # winner wins one more match than sub-winners
    # We try to assign winner from left or right subtree
    # The winner must have wins = sum of wins of children + 1
    # Check all possible winners (only one winner per match)
    # We know total players are all leaves under this tree
    leaves = l_contestants + r_contestants
    # The winner is the one whose wins = sum of wins of children +1
    # Others wins remain same
    
    # Actually winner node corresponds to one of the contestants
    # But we don't know which subtree is winner, only that winner wins one more match.
    # Recursively, we can check if choosing left or right as winner validates counts.
    
    # So try left as winner:
    # sum all child's wins +1 must equal winner's wins
    
    # We'll define a helper that returns True if subtree is consistent and updates wins left for rest
    
    # Instead, use a function that returns number of matches won per leaf under subtree, including the current match
    
    # So leaves are known, we want to check if wins dict matches
    
    # We'll try to assign winner to left or right subtree:
    
    # try left winner
    left_results = collect_results(left)
    right_results = collect_results(right)
    # winner must have +1 from their subtree wins (total matches in subtree)
    
    # Number of matches is number of leaves -1, so for this subtree total matches = len(leaves)-1
    # wins of winner = wins in subtree + 1 (current match)
    
    # Actually, from definition the winner's total wins is sum of wins in subtree + 1
    # So need to verify wins dictionary accordingly
    
    # A better approach: define a recursive function validate(tree) returns total matches in subtree and checks wins:
    
    # So we implement validate() below
    return leaves

def validate(tree):
    if isinstance(tree, str):
        # leaf node
        if tree not in wins:
            return False, 0, {tree:0}
        return True, 0, {tree:0}
    left, right = tree
    valid_l, cnt_l, map_l = validate(left)
    if not valid_l:
        return False,0,{}
    valid_r, cnt_r, map_r = validate(right)
    if not valid_r:
        return False,0,{}
    # total matches in this subtree
    total = cnt_l + cnt_r + 1
    # Combine maps
    combined = {**map_l}
    for k,v in map_r.items():
        combined[k] = v
    # The winner of this match gets +1 win, that is the only unknown
    # try left winner:
    left_winner = None
    if isinstance(left, str):
        left_winner = left
    else:
        # winner is winner of left subtree, we need to know which one
        # but we don't know!
        # However, the leaf nodes are always distinct
        # In this recursive approach, winner is the winner of the subtree root
        # We must process bottom-up, ensuring the winner's wins is one more than sum of children's
        pass
    # Actually, the winner must be one of the contestants in the subtree
    # The winner's wins = sum of wins in children + 1
    # We can test both possibilities: left or right subtree winner
    
    d_left = combined.copy()
    d_left[left_winner] += 1
    if d_left == wins:
        return True, total, combined
    # try right winner
    right_winner = None
    if isinstance(right, str):
        right_winner = right
    else:
        pass
    d_right = combined.copy()
    d_right[right_winner] = d_right.get(right_winner,0) + 1
    if d_right == wins:
        return True, total, combined
    return False, total, combined

# The above is complex, replan with a better approach.

# New approach:
# The total matches = N-1
# Each internal node corresponds to one match; the winner wins 1 more than the sum of wins of their subtree.
# So each internal node is a match, winner is either left or right subtree's winner.
# We'll return all possible winners from each subtree with their wins count.
# The root node must have a unique winner matching wins dictionary.

def dfs(tree):
    if isinstance(tree,str):
        # leaf: unique winner with 0 wins in this subtree
        return {tree:0}
    left,right=tree
    left_winners=dfs(left)
    right_winners=dfs(right)
    res={}
    for lw in left_winners:
        for rw in right_winners:
            # match between lw and rw
            # winner is lw or rw
            # winner's wins = wins in subtree +1
            # other is unchanged
            # wins sum in subtree = sum of left + sum of right + 1 matches = (len(left leaves)-1)+(len(right leaves)-1)+1 = total leaves -1
            # but we focus on number of wins per contestant
            
            # winner lw:
            d = dict()
            for k,v in left_winners.items():
                d[k]=v
            for k,v in right_winners.items():
                d[k]=v
            d[lw]+=1
            # Verify if d is consistent with final wins or save
            key = tuple(sorted(d.items()))
            res[key] = d
            # similarly winner rw:
            d2 = dict()
            for k,v in left_winners.items():
                d2[k]=v
            for k,v in right_winners.items():
                d2[k]=v
            d2[rw]+=1
            key2 = tuple(sorted(d2.items()))
            res[key2]=d2
    # find unique dictionaries and return merged dict with min wins for pruning
    # To avoid memory blow-up, just return the dicts:
    return list(res.values())

S=sys.stdin.readline().rstrip('\n')
tree,_=parse(S,0)
N=len({c for c in S if c.islower()})
wins=dict()
for _ in range(N):
    a,v=sys.stdin.readline().split()
    wins[a]=int(v)

def dfs2(tree):
    if isinstance(tree,str):
        return [{tree:0}]
    left,right=tree
    left_list=dfs2(left)
    right_list=dfs2(right)
    res=[]
    for lw in left_list:
        for rw in right_list:
            # two winner options
            # winner left subtree winner
            merged = dict()
            for k,v in lw.items():
                merged[k]=v
            for k,v in rw.items():
                merged[k]=v
            # winner left subtree winner. Identify winner candidate: max win in left subtree
            # but subtree can't guarantee, winner is unknown
            # Actually, winner must be one of the keys in left subtree
            # So iterate over possible candidates
            for winner in lw:
                d=merged.copy()
                d[winner]+=1
                # Make sure all keys included
                res.append(d)
            # winner right subtree winner
            for winner in rw:
                d=merged.copy()
                d[winner]+=1
                res.append(d)
    # remove duplicates by str keys
    uniq = dict()
    for d in res:
        key = tuple(sorted(d.items()))
        uniq[key] = d
    return list(uniq.values())

results = dfs2(tree)
for r in results:
    if all(r.get(k,0)==wins[k] for k in wins):
        print("Yes")
        break
else:
    print("No")