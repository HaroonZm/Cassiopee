mod=10**9+7
N=int(input())
m=int(input())
s=input()
vars_=[None]*m
U=[0]*m
for i in range(m):
    v,u=input().split()
    vars_[i]=v
    U[i]=int(u)
idx={v:i for i,v in enumerate(vars_)}
assign=[-1]*m
def options(ch,leading,var_idx=-1):
    if ch.isdigit():
        return 0 if ch!=ch else 1
    if var_idx==-1:
        var_idx=idx[ch]
    u=U[var_idx]
    if leading:
        return u if u>0 else 0
    else:
        return u+1
def get_options(ch1,ch2,leading1,leading2):
    if ch1.isdigit() and ch2.isdigit():
        return 1 if ch1==ch2 else 0, -1, -1
    if ch1.isdigit():
        if ch2.isdigit():
            return (1 if ch1==ch2 else 0), -1, -1
        v2=idx[ch2]
        c=int(ch1)
        u=U[v2]
        if leading2 and c==0:
            return 0,-1,-1
        if c<=u:
            return 1,v2,c
        return 0,-1,-1
    if ch2.isdigit():
        v1=idx[ch1]
        c=int(ch2)
        u=U[v1]
        if leading1 and c==0:
            return 0,-1,-1
        if c<=u:
            return 1,v1,c
        return 0,-1,-1
    v1=idx[ch1]
    v2=idx[ch2]
    if v1==v2:
        # same var: assign once
        return 1,v1,-1
    else:
        # different vars must have same digit
        return 26,-1,-1
from collections import defaultdict
class UF:
    def __init__(self,n):
        self.p=list(range(n))
        self.rank=[0]*n
        self.assign=[-1]*n
    def find(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]
            x=self.p[x]
        return x
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return
        if self.rank[x]<self.rank[y]:
            self.p[x]=y
        else:
            self.p[y]=x
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1
def solve():
    # For palindrome, s[i] and s[N-1-i] same after replacement
    uf=UF(m)
    # assign digits for vars
    # For each i in [0..N//2]
    # merge vars appearing at s[i], s[N-1-i]
    # if both digits and differ => 0
    # if digit and var => restrict var to digit
    # if var and var => union sets, digits must be same
    fixed_digit=[-1]*m
    used_digit=[-1]*m
    for i in range(N//2):
        l=i
        r=N-1-i
        c1,c2=s[l],s[r]
        if c1.isdigit() and c2.isdigit():
            if c1!=c2:
                return 0
        elif c1.isdigit():
            if c2 in idx:
                v=idx[c2]
                d=int(c1)
                if fixed_digit[v]==-1:
                    fixed_digit[v]=d
                elif fixed_digit[v]!=d:
                    return 0
        elif c2.isdigit():
            if c1 in idx:
                v=idx[c1]
                d=int(c2)
                if fixed_digit[v]==-1:
                    fixed_digit[v]=d
                elif fixed_digit[v]!=d:
                    return 0
        else:
            if c1 in idx and c2 in idx:
                uf.union(idx[c1],idx[c2])
    # middle char if odd length
    if N%2==1:
        c=s[N//2]
        if c.isdigit():
            # nothing to do
            pass
        elif c in idx:
            pass
    # Now all variables connected must have same fixed digit or no digit
    group_vars=defaultdict(list)
    for v in range(m):
        group_vars[uf.find(v)].append(v)
    assign_group_digit=dict()
    for root,group in group_vars.items():
        digits=[fixed_digit[v] for v in group if fixed_digit[v]!=-1]
        if len(set(digits))>1:
            return 0
        d=digits[0] if digits else -1
        for v in group:
            fixed_digit[v]=d
        assign_group_digit[root]=d
    # Calculate answer
    res=1
    lead_positions=set()
    # leading zeros not allowed: var at position 0 must not be 0
    # also for palindrome, position 0 and N-1 are the same value.
    # gather positions of vars to consider leading zeros
    for i,v in enumerate(s):
        if v in idx:
            if i==0:
                lead_positions.add(uf.find(idx[v]))
            if N%2==1 and i==N//2:
                # middle pos; no leading zero constraint needed because no pos after
                pass
            if i==N-1:
                lead_positions.add(uf.find(idx[v]))
    # For each group with no assigned digit, multiply number of possible digits
    for root,group in group_vars.items():
        d=assign_group_digit[root]
        u=min(U[v] for v in group)
        if d!=-1:
            # assigned digit fixed; check leading zero rule
            if root in lead_positions and d==0:
                return 0
            continue
        # number of options for this group:
        # if leading zero forbidden => digits 1..u
        # else digits 0..u
        if root in lead_positions:
            cnt = max(0,u)
        else:
            cnt = u+1
        if cnt<=0:
            return 0
        res=(res*cnt)%mod
    # Validate fixed digits for variables at middle position if odd
    if N%2==1:
        c=s[N//2]
        if c in idx:
            v=idx[c]
            d=fixed_digit[v]
            if d==-1:
                u=U[v]
                if (uf.find(v) in lead_positions):
                    if u==0:
                        return 0
                # no leading zero in middle? no constraint to forbid zero in middle
                # so no special constraint needed
    return res%mod
print(solve())