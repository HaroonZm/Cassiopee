def main():
    while True:
        H, W, C, M, NW, NC, NM = map(int, input().split())
        if H < 0:
            break

        # read warriors' friendly heroes
        warrior_hero = []
        for _ in range(W):
            line = list(map(int, input().split()))
            ni = line[0]
            hero_list = line[1:] if ni > 0 else []
            warrior_hero.append(set(hero_list))

        # read clerics' friendly warriors
        cleric_warrior = []
        for _ in range(C):
            line = list(map(int, input().split()))
            ni = line[0]
            warrior_list = line[1:] if ni > 0 else []
            cleric_warrior.append(set(warrior_list))

        # read mages' friendly clerics
        mage_cleric = []
        for _ in range(M):
            line = list(map(int, input().split()))
            ni = line[0]
            cleric_list = line[1:] if ni > 0 else []
            mage_cleric.append(set(cleric_list))

        max_parties = 0

        # For each possible number of parties from 0 up to total number of heroes,
        # try to find if it's possible to form that many parties.
        # Since the problem states max 50, trying all is ok for a beginner approach.

        # We'll try all subsets of heroes of size p (from p = min(H, W+C+M+H) down to 0)
        # but searching all subsets is very big (2^H)
        # instead, we will try a simple greedy approach by enumerating possible parties.
        # Because groups depend on get along conditions, we check combinations.

        # We'll try all possible parties by enumerating number of parties
        # For each party, choose one hero, possibly one warrior, one cleric, one mage following rules
        # We'll generate all possible parties. Then, greedily pick disjoint parties to maximize count.

        # First, prepare friendly pairs between roles
        # warrior i gets along with hero h if h in warrior_hero[i]
        # cleric j gets along with warrior i if i in cleric_warrior[j]
        # mage k gets along with cleric j if j in mage_cleric[k]

        # We'll create lists of possible parties:
        # Each party: hero h, optional warrior w, optional cleric c, optional mage m
        # Ensure the get-along constraints are met.

        parties = []

        # We try all possible hero assignments since hero mandatory
        # For warrior, can be None or an index 0..W-1
        # Same for cleric and mage
        # But must meet constraints:

        # Conditions:
        # 1) party must have hero
        # 2) warrior and hero get along if warrior is present
        # 3) cleric and warrior get along if both present
        # 4) mage and cleric get along if both present
        # 5) party recommended to have warrior, cleric, mage but up to NW,NC,NM parties can lack them
        # 6) party without cleric should have warrior and mage
        #
        # Because the problem is complex, and beginner solution allowed,
        # we will just generate all possible groups that satisfy the conditions without limits on NW, NC, NM,
        # then later count how many groups can be formed minimizing missing warriors/clerics/mages.

        # For simplicity, we only consider parties with hero and optional warrior, cleric, mage
        # But to cover the tricky rules, we consider all combos and filter.

        # Because IDs of heroes, warriors, clerics, mages start from 1, but indices in lists start from 0,
        # pay attention to indexing.

        # We'll create a list of all parties:
        # for hero in 1..H
        # for warrior in [None] + 1..W
        # for cleric in [None] + 1..C
        # for mage in [None] + 1..M

        # Check constraints, if satisfied, add party as a tuple (h, w, c, m)

        # Because max is 50 for each, total combinations could be big but since beginner approach,
        # we'll prune to only possible combinations.

        for h in range(1, H+1):
            for w in [None] + list(range(1, W+1)):
                # if warrior is present, hero must be in warrior_hero[w-1]
                if w is not None:
                    if h not in warrior_hero[w-1]:
                        continue
                for c in [None] + list(range(1, C+1)):
                    if c is not None and w is not None:
                        # cleric and warrior must get along
                        if w not in cleric_warrior[c-1]:
                            continue
                    for m in [None] + list(range(1, M+1)):
                        if m is not None and c is not None:
                            # mage and cleric must get along
                            if c not in mage_cleric[m-1]:
                                continue
                        # Rule: party must have hero
                        # Already have h
                        # Rule: party without cleric should have warrior and mage
                        if c is None:
                            if w is None or m is None:
                                continue
                        # Rule: warrior and hero get along if warrior present done above
                        # Rule: cleric and warrior get along if both present done above
                        # Rule: mage and cleric get along if both present done above
                        # valid party
                        parties.append((h, w, c, m))

        # Now we want to select maximum number of disjoint parties
        # Disjoint means one adventurer can be in only one party
        # So no overlapping heroes, warriors, clerics, mages

        # We'll do a greedy approach:
        # sort parties by number of adventurers involved (more adventurers harder to overlap)
        # then pick parties if no conflict with already chosen parties

        chosen_heroes = set()
        chosen_warriors = set()
        chosen_clerics = set()
        chosen_mages = set()

        max_count = 0

        # Sort by number of roles used descending to pick bigger parties first
        def count_roles(p):
            return sum([1 if x is not None else 0 for x in p])

        parties_sorted = sorted(parties, key=count_roles, reverse=True)

        for p in parties_sorted:
            h, w, c, m = p
            if h in chosen_heroes:
                continue
            if w is not None and w in chosen_warriors:
                continue
            if c is not None and c in chosen_clerics:
                continue
            if m is not None and m in chosen_mages:
                continue
            chosen_heroes.add(h)
            if w is not None:
                chosen_warriors.add(w)
            if c is not None:
                chosen_clerics.add(c)
            if m is not None:
                chosen_mages.add(m)
            max_count += 1

        # Check how many parties missing warrior, cleric, mage
        missing_W = 0
        missing_C = 0
        missing_M = 0

        # We do not have direct list of parties chosen, but we can find that later if needed
        # For beginner solution, ignore constraints on NW, NC, NM, just print max_count

        # But problem says it's allowed that at most NW, NC, NM parties does not have warrior, cleric, mage respectively.

        # Because our selection greedily picks bigger parties first, usually minimal missing
        # But we do not distinguish missing counts and problem may require reducing count.

        # So as beginner approach, if missing counts exceed limits, reduce max_count by exceeding amount
        # approximately.

        # To count missing, we count parties lacking warrior, cleric, mage from chosen parties

        # For beginner approach, we can keep a list of chosen parties and count missing

        chosen_parties = []

        chosen_heroes = set()
        chosen_warriors = set()
        chosen_clerics = set()
        chosen_mages = set()
        max_count = 0

        for p in parties_sorted:
            h, w, c, m = p
            if h in chosen_heroes:
                continue
            if w is not None and w in chosen_warriors:
                continue
            if c is not None and c in chosen_clerics:
                continue
            if m is not None and m in chosen_mages:
                continue
            chosen_heroes.add(h)
            if w is not None:
                chosen_warriors.add(w)
            if c is not None:
                chosen_clerics.add(c)
            if m is not None:
                chosen_mages.add(m)
            chosen_parties.append(p)
            max_count += 1

        missing_w = sum(1 for p in chosen_parties if p[1] is None)
        missing_c = sum(1 for p in chosen_parties if p[2] is None)
        missing_m = sum(1 for p in chosen_parties if p[3] is None)

        # If missing > limits, reduce parties count
        # Each missing party over limit reduce max_count by 1 (simple)

        reduce = 0
        if missing_w > NW:
            reduce += missing_w - NW
        if missing_c > NC:
            reduce += missing_c - NC
        if missing_m > NM:
            reduce += missing_m - NM

        result = max_count - reduce
        if result < 0:
            result = 0

        print(result)

if __name__ == "__main__":
    main()