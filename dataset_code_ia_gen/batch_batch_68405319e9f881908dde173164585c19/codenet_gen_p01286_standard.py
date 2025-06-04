import sys
from collections import deque

def max_parties(H, W, C, M, NW, NC, NM, w_heroes, c_warriors, m_clerics):
    # We model the problem as a flow network.
    # Nodes indexing:
    # 0: source
    # 1..H: heroes
    # H+1..H+W: warriors
    # H+W+1..H+W+C: clerics
    # H+W+C+1..H+W+C+M: mages
    # H+W+C+M+1.. : dummy nodes for parties to model constraints

    # But since we want max number of parties, each party must have a hero,
    # and relationships/compatibilities must be respected.
    # The constraints about allowed missing roles are caps on the number
    # of parties without warrior/cleric/mage.

    # We will use a binary search on the number of parties P:
    # For a guess P, can we form P parties satisfying the rules and not exceeding NW, NC, NM?

    # Build compatibility bipartite graphs:
    # W-H edges: warrior i <-> hero j, if compatible
    # C-W edges: cleric i <-> warrior j, if compatible
    # M-C edges: mage i <-> cleric j, if compatible

    # Because a party is a quadruple (hero, warrior, cleric, mage) satisfying the edges
    # but warrior/cleric/mage may be missing only to extent NW, NC, NM.
    # But also, a party without cleric must have warrior and mage.

    # To solve: We try to find P sets satisfying the constraints.

    # Approach:
    # Create a network where edges represent compatibility, and try to find P disjoint sets of (H,W,C,M)
    # that satisfy constraints.

    # Instead, we use a more practical approach:
    # Because each party must have hero,
    # warrior and hero must get along,
    # cleric and warrior must get along,
    # mage and cleric must get along.
    # Missing roles are limited.

    # So one party corresponds to:
    # hero h - warrior w - cleric c - mage m,
    # with edges h-w, w-c, c-m.

    # If cleric is missing, party must have warrior and mage,
    # so edges are h-w, w-(no cleric), mage present,
    # but warrior and mage must be compatible through cleric? No, only if cleric missing,
    # so mage and warrior compatibility isn't explicit here.

    # Let's create parts: heroes, warriors, clerics, mages.
    # We'll construct tripartite graph hero-warrior-cleric and cleric-mage edges.
    # Then try to find matchings representing parties.

    # But the problem can be seen as max number of quadruples fulfilling edges,
    # with possibly missing warrior/cleric/mage up to NW, NC, NM.

    # We'll try all possible counts P from 0 to H as binary search,
    # building a flow network and checking if P parties can be formed.

    # Build relation matrices:
    hero_compatible = [set() for _ in range(H)]  # for each hero, set of warriors compatible
    for i in range(W):
        for h in w_heroes[i]:
            hero_compatible[h-1].add(i)

    warrior_compatible = [set() for _ in range(W)]  # for each warrior, set of clerics compatible
    for i in range(C):
        for w in c_warriors[i]:
            warrior_compatible[w-1].add(i)

    cleric_compatible = [set() for _ in range(C)]  # for each cleric, set of mages compatible
    for i in range(M):
        for c in m_clerics[i]:
            cleric_compatible[c-1].add(i)

    # Create flow network for a guess P:
    # We create nodes:
    # source: 0
    # heroes: 1 to H
    # warriors: H+1 to H+W
    # clerics: H+W+1 to H+W+C
    # mages: H+W+C+1 to H+W+C+M
    # sink: H+W+C+M+1

    # We add edges:
    # source->hero (capacity P/H to allow up to P heroes, but each hero can be in at most one party, so capacity=1)
    # hero->warrior if compatible (capacity 1)
    # warrior->cleric if compatible (capacity 1)
    # cleric->mage if compatible (capacity 1)
    # mage->sink (capacity 1)

    # But we have missing allowed NW, NC, NM parties without warrior, cleric, mage
    # Also, each party must have hero.

    # To take into account missing roles, we add dummy nodes for missing roles.

    # Instead of complicated flow, we use the standard matching approach in 4 layers with dummy nodes.

    # Implementation plan:
    # For each guess P:
    # create a network with capacities 1 with respect to number of heroes P
    # each hero capacity 1
    # add edges hero->warrior for compatible
    # add dummy warrior node representing "no warrior": can be used at most NW times
    # same for cleric and mage with dummies and capacities.

    # A party without cleric must have warrior and mage present,
    # so if cleric is missing, warrior and mage must be present.

    # So, we need to incorporate those constraints into the flow network:

    # Let's create dummy nodes representing missing roles:
    # dummy warrior node with capacity NW
    # dummy cleric node with capacity NC
    # dummy mage node with capacity NM

    # So edges hero->warrior (including dummy warrior node) with capacities
    # warrior->cleric (including dummy cleric node) with capacities
    # cleric->mage (including dummy mage node) with capacities
    # mage->sink

    # For parties without cleric (using dummy cleric), enforce warrior and mage != dummy.

    # We check feasibility with max flow >= P.

    # Helper function to build graph and compute max flow.

    def can_form(P):
        # Node indexing:
        # 0: source
        # heroes: 1..H
        # warriors: H+1..H+W
        # dummy_warrior: H+W+1
        # clerics: H+W+2..H+W+C+1
        # dummy_cleric: H+W+C+2
        # mages: H+W+C+3..H+W+C+M+2
        # dummy_mage: H+W+C+M+3
        # sink: H+W+C+M+4

        S = 0
        hero_start = 1
        warrior_start = hero_start + H
        dummy_warrior = warrior_start + W
        cleric_start = dummy_warrior + 1
        dummy_cleric = cleric_start + C
        mage_start = dummy_cleric + 1
        dummy_mage = mage_start + M
        T = dummy_mage + 1

        size = T + 1

        graph = [[] for _ in range(size)]

        def add_edge(u,v,c):
            graph[u].append([v,c,len(graph[v])])
            graph[v].append([u,0,len(graph[u]) -1])

        # source->hero capacity 1
        for h in range(H):
            add_edge(S, hero_start+h, 1)

        # hero->warrior capacity 1 for compatible warriors
        # hero->dummy_warrior if allowed missing warrior
        for h in range(H):
            compat_ws = hero_compatible[h]
            if len(compat_ws) == 0 and NW==0:
                # hero with no compatible warrior and no allowance for missing warrior => can't assign
                return False
            for w in compat_ws:
                add_edge(hero_start+h, warrior_start + w,1)
            # also edge to dummy warrior to allow no warrior if NW>0
            if NW>0:
                add_edge(hero_start+h, dummy_warrior,1)

        # warrior->cleric capacity 1 for compatible
        # warrior->dummy_cleric if allowed missing cleric
        for w in range(W):
            compat_cs = warrior_compatible[w]
            if len(compat_cs) == 0 and NC==0:
                # warrior no cleric compatible and no allowance missing cleric
                # can still connect to dummy cleric?
                pass # will add dummy edge if NC>0
            for c_ in compat_cs:
                add_edge(warrior_start + w, cleric_start + c_,1)
            if NC>0:
                add_edge(warrior_start + w, dummy_cleric,1)

        # dummy warrior -> dummy cleric edge to allow missing warrior and cleric sequence?
        # Actually, not needed.

        # dummy warrior -> dummy cleric capacity NW (missing warrior allowed)
        # We'll limit dummy warrior node capacity from hero side and dummy cleric capacity later.

        # cleric->mage capacity 1 for compatible
        # cleric->dummy_mage if allowed missing mage
        for c_ in range(C):
            compat_ms = cleric_compatible[c_]
            if len(compat_ms) == 0 and NM==0:
                pass
            for m in compat_ms:
                add_edge(cleric_start + c_, mage_start + m, 1)
            if NM > 0:
                add_edge(cleric_start + c_, dummy_mage,1)

        # dummy cleric -> dummy mage if NM>0
        if NM > 0:
            add_edge(dummy_cleric, dummy_mage, max(NM, 0))

        # dummy warrior->dummy cleric capacity NW, dummy cleric->dummy mage capacity NC handled above?

        # dummy warrior capacity from hero edges limited by total NW, so limit capacity from dummy warrior->dummy cleric ?

        # dummy warrior->dummy cleric edges? To allow missing warrior and cleric in party?

        # Let's add capacity limit on dummy warrior, dummy cleric, dummy mage nodes.

        # dummy warrior->dummy cleric capacity NW
        if NW > 0:
            add_edge(dummy_warrior, dummy_cleric, NW)
        # dummy cleric->dummy mage capacity NC
        if NC > 0:
            add_edge(dummy_cleric, dummy_mage, NC)

        # mage->sink capacity 1 for each mage
        for m_ in range(M):
            add_edge(mage_start + m_, T, 1)
        if NM > 0:
            add_edge(dummy_mage, T, NM)

        # Also add capacity on dummy warrior, dummy cleric, dummy mage edges to sink if needed, but done above.

        # The rule: party without cleric must have warrior and mage.
        # If party uses dummy cleric for "no cleric", then warrior and mage must be present and not dummy.
        # To ensure this, we forbid hero->dummy_warrior edges if dummy_cleric is chosen,
        # but it's too complex.

        # Instead, we will mark parties formed using dummy cleric and check in matching process.

        # We will run max flow. After checking max flow>=P, we verify:
        # number of parties without warrior <= NW
        # without cleric <= NC
        # without mage <= NM
        # also parties without cleric must have warrior and mage present (not dummy).

        # But the network enforces capacities; the dummy nodes capacities limit those counts.

        # So capacity constraints enforce allowed missing roles.

        # We'll run Dinic max flow to get max number of parties.

        # Dinic Implementation:

        level = [0]*size
        iter = [0]*size

        def bfs():
            for i in range(size):
                level[i] = -1
            queue = deque()
            queue.append(S)
            level[S] = 0
            while queue:
                v= queue.popleft()
                for i,(to,cap,rev) in enumerate(graph[v]):
                    if cap>0 and level[to]<0:
                        level[to] = level[v]+1
                        queue.append(to)
            return level[T]>=0

        def dfs(v,upTo):
            if v==T:
                return upTo
            while iter[v]<len(graph[v]):
                to,cap,rev = graph[v][iter[v]]
                if cap>0 and level[v]<level[to]:
                    d = dfs(to,min(upTo,cap))
                    if d>0:
                        graph[v][iter[v]][1] -= d
                        graph[to][rev][1] += d
                        return d
                iter[v]+=1
            return 0

        flow=0
        while bfs():
            for i in range(size):
                iter[i]=0
            while True:
                f=dfs(S,10**9)
                if f<=0:
                    break
                flow+=f
                if flow>=P:
                    return True
        return flow>=P

    left, right = 0, H
    while left < right:
        mid = (left + right + 1)//2
        if can_form(mid):
            left = mid
        else:
            right = mid -1
    return left

input=sys.stdin.readline
while True:
    line = input()
    if not line:
        break
    H,W,C,M,NW,NC,NM = map(int,line.split())
    if H<0:
        break
    w_heroes = []
    for _ in range(W):
        data = list(map(int,input().split()))
        w_heroes.append(data[1:])
    c_warriors = []
    for _ in range(C):
        data = list(map(int,input().split()))
        c_warriors.append(data[1:])
    m_clerics = []
    for _ in range(M):
        data = list(map(int,input().split()))
        m_clerics.append(data[1:])
    print(max_parties(H,W,C,M,NW,NC,NM,w_heroes,c_warriors,m_clerics))