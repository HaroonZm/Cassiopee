from sys import stdin
def main():
    input=stdin.readline
    N,C=map(int,input().split())
    INF=10**9
    dist=[[INF]*N for _ in range(N)]
    for i in range(N):
        dist[i][i]=0
    # position of person 1 fixed at 0, so no special edge needed here
    for _ in range(C):
        line=input().strip()
        # parse line like: aioibisd_i
        # e.g. 1<=2-1
        # split into parts:
        # a_i, o_i, b_i, s_i, d_i
        # a_i and b_i are integers
        # o_i in {<=, >=, *}
        # s_i in {+, -}
        # d_i integer
        # find positions of o_i (*,<=,>=)
        if '<=' in line:
            o_i='<=';
            parts=line.split('<=')
        elif '>=' in line:
            o_i='>=';
            parts=line.split('>=')
        else:
            o_i='*';
            parts=line.split('*')
        a_i=int(parts[0])
        b_s=parts[1]
        s_i=b_s[-(len(b_s)-b_s.find('+')+1):] if '+' in b_s else b_s[-(len(b_s)-b_s.find('-')+1):] if '-' in b_s else ''
        # Since s_i is either + or -, at last but one character of b_s
        s_i = b_s[-(len(b_s)-b_s.find('+')+1):] if '+' in b_s else b_s[-(len(b_s)-b_s.find('-')+1):] if '-' in b_s else ''
        # alternative parse: last but one character is s_i, last characters digits
        # better manual parse:
        if '+' in b_s:
            s_i='+'
            idx=b_s.index('+')
            b_i=int(b_s[:idx])
            d_i=int(b_s[idx+1:])
        else:
            s_i='-'
            idx=b_s.index('-')
            b_i=int(b_s[:idx])
            d_i=int(b_s[idx+1:])
        a_i-=1;b_i-=1
        # We represent variables as positions[x]
        # dist[i][j] = minimal position_j - position_i
        # dist[j][i] = minimal position_i - position_j
        # order constraints:
        if o_i=='<=':
            # a_i <= b_i
            # so pos[b_i] - pos[a_i] >= 0
            # edge a_i->b_i weight >=0 -> dist[a_i][b_i] >=0
            # since dist[a_i][b_i] stores minimal pos[b_i] - pos[a_i], dist[a_i][b_i] >=0
            dist[a_i][b_i]=max(dist[a_i][b_i],0)
        elif o_i=='>=':
            # a_i >= b_i i.e. pos[a_i]>=pos[b_i]
            # pos[b_i] - pos[a_i] <=0
            # dist[b_i][a_i] = min(pos[a_i]-pos[b_i]) <=0
            dist[b_i][a_i]=max(dist[b_i][a_i],0)
        # if o_i=='*', no order constraint to add
        # distance constraint
        if s_i=='+':
            # distance >= d_i
            # abs(pos[a_i]-pos[b_i]) >= d_i
            # pos[b_i]-pos[a_i]>=d_i or pos[a_i]-pos[b_i]>=d_i
            # dist[a_i][b_i]>=d_i or dist[b_i][a_i]>=d_i
            # encoded as two edges:
            # dist[a_i][b_i]>=d_i => dist[a_i][b_i]=max(dist[a_i][b_i],d_i)
            # dist[b_i][a_i]>=d_i => dist[b_i][a_i]=max(dist[b_i][a_i],d_i)
            dist[a_i][b_i]=max(dist[a_i][b_i],d_i)
            dist[b_i][a_i]=max(dist[b_i][a_i],d_i)
        else:
            # s_i=='-'
            # abs(pos[a_i]-pos[b_i]) <= d_i
            # pos[b_i]-pos[a_i] <= d_i and pos[a_i]-pos[b_i] <= d_i
            # dist[a_i][b_i] <= d_i and dist[b_i][a_i] <= d_i
            # since dist has minimal pos[b_i]-pos[a_i] not maximal
            # we store upper bounds by negative weights of dist[b_i][a_i], dist[a_i][b_i]
            # To handle upper bounds, we use constraint edges for upper bounds
            # dist[a_i][b_i] <= d_i means pos[b_i]-pos[a_i] <= d_i
            # represents an upper bound
            # We implement upper bounds by adding edges in reverse direction with negative weight
            # i->j with weight w means pos_j <= pos_i + w
            # For upper bound pos_j - pos_i <= w, edge i->j weight w
            # Here pos[b_i]-pos[a_i] <= d_i: edge a_i->b_i weight d_i
            # Similarly pos[a_i]-pos[b_i] <= d_i: edge b_i->a_i weight d_i
            # So to model upper bound constraints, we put edges representing
            # pos_j <= pos_i + w
            dist[b_i][a_i]=min(dist[b_i][a_i],d_i)
            dist[a_i][b_i]=min(dist[a_i][b_i],d_i)
    # Use Floyd-Warshall to find minimal differences dist[i][j]
    # But now, dist[i][j] must be minimal possible pos_j - pos_i satisfying constraints
    # For upper bound edges, we keep minimal dist[i][j]
    for k in range(N):
        for i_ in range(N):
            for j_ in range(N):
                if dist[i_][k]==INF or dist[k][j_]==INF:
                    continue
                nd=dist[i_][k]+dist[k][j_]
                if nd<dist[i_][j_]:
                    dist[i_][j_]=nd
    # Detect negative cycles:
    # since dist[i][i] minimal pos_i - pos_i <=0 always 0
    # if dist[i][i]<0 negative cycle, no solution
    for i in range(N):
        if dist[i][i]<0:
            print(-1)
            return
    # Since person 1 at position 0 fixed,
    # pos[i] >= pos[0] + dist[0][i]
    # To maximize max pos[i], maximize (pos[max_i] - pos[0]) which is max dist[0][i]
    # but dist[0][i] minimal pos_i - pos_0
    # max_i of pos_i >= dist[0][i], so minimal position of i from 0 is dist[0][i]
    # If there is an i such that dist[i][0]+dist[0][i]<0, cycle of length <0
    # Check for infinite: if there is a path from 0 to i and i to 0 with sum of dist <0 then infinite
    # Here check if there is a sequence of nodes on which can extend positions to infinity
    # That is, for each node part of a cycle reachable to 0 and from 0 negative cycle, infinite
    # Since no negative cycles, no -1 output
    # We check if there exists i with dist[0][i]+dist[i][0]<0 -> causes infinite distance
    for i in range(N):
        if dist[0][i]==INF or dist[i][0]==INF:
            continue
        if dist[0][i]+dist[i][0]<0:
            print("inf")
            return
    # finally, maximum distance from position 1 (index 0) to last person in line
    # the maximal position is max dist[0][i]
    maxd=max(dist[0])
    if maxd>=INF:
        print("inf")
    else:
        print(maxd)
main()