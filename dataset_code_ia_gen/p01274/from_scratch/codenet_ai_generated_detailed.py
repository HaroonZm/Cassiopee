import sys
import math
from collections import deque

def solve():
    input = sys.stdin.readline

    while True:
        # Read number of monsters
        N_line = input()
        if not N_line:
            break
        N_line = N_line.strip()
        if N_line == "0":
            break
        N = int(N_line)

        # Read HPs of monsters
        HPs_line = input().strip()
        HPs = list(map(int, HPs_line.split()))
        assert len(HPs) == N

        # Read number of spells
        M = int(input().strip())

        spells = []
        max_single_damage = 0  # Track max single-target damage for pruning
        max_all_damage = 0     # Track max all-target damage for pruning

        for _ in range(M):
            line = input().strip().split()
            Name = line[0]
            MP = int(line[1])
            Target = line[2]
            Damage = int(line[3])
            spells.append((Name, MP, Target, Damage))
            if Target == "Single" and Damage > max_single_damage:
                max_single_damage = Damage
            elif Target == "All" and Damage > max_all_damage:
                max_all_damage = Damage

        # To minimize MP used to reduce all monsters' HP to zero or below.

        # Approach:
        # Use BFS or Dijkstra over the state of monsters HP.
        # But monsters' HP can be large up to 100,000 each, which is too big for a direct BFS.
        # Alternative: Use a heuristic + DP over monster HP but that is too large.
        #
        # Observation:
        # Because spells can be used any number of times, and damage is fixed, and MP usage per spell is fixed,
        # We can consider this as a DP problem to reduce HP for monsters.
        #
        # Key is that single-target spells affect one monster, all-target spells affect all monsters.
        #
        # Important:
        # Since N ≤ 100 and HP_i up to 100000, direct state space is huge.
        #
        # Idea:
        # Because all-target spells reduce all monsters simultaneously,
        # we can consider the problem in phases:
        #
        # 1) Use all-target spells to reduce monsters' HP roughly.
        # 2) Use single-target spells to finish off monsters individually.
        #
        # We can try all combinations of number of uses of all-target spells
        # but max HP is large, so enumerate from 0 to max uses is impractical.
        #
        # Alternative approach: Binary search on minimum MP:
        # We binary search on answer for MP spent,
        # and check if with this MP we can defeat all monsters.
        #
        # For checking feasibility given MP limit:
        # - For all-target spells, number of times to use is limited by MP // spell.MP
        # - For single-target spells, similarly.
        #
        # But still hard.
        #
        # Alternative approach is:
        # Since each spell can be used multiple times,
        # and damage and MP are linear, we can consider:
        #
        # For each monster we want minimal MP to reduce its HP to 0 or less.
        # For single-target spells, per monster the cost to kill (HP_i, spells single-target)
        # - minimal MP cost to reduce HP_i to zero using single target spells.
        #
        # For all-target spells,
        # - if we use an all-target spell k times, it reduces HP of every monster by k*Damage.
        #   The total MP spent is k*MP_of_spell.
        #
        # We want to find the minimal total MP spent k1 * MP1 + k2 *MP2 + ... (all-target spells used)
        # plus sum over monsters of minimal MP needed to finish it from remaining HP after all-target damage.
        #
        # Because there can be multiple all-target spells, we must consider combinations of their uses.
        #
        # N=100 and M<=100, it's still large state space.
        #
        # Let's try this:
        # For each monster, precompute minimal MP to kill it using single-target spells only (which can be used multiple times).
        #
        # Then we consider all-target spells usage:
        # Because max HP ≤ 100000,
        # max damage per all-target spell ≤ 999999,
        # number of times to use an all-target spell to reduce HP by some amount is ceil(HP_i / Damage).
        #
        # But if we consider usage counts of all-target spells together,
        # the HP reduction is sum over spells (usage_j * damage_j)
        #
        # We want to find multiset {usage of all-target spells} to minimize total MP spent on all-target,
        # and sum over monsters minimal MP on single-target for their leftover HP.
        #
        # Since the number of all-target spells can be up to M,
        # but limited, we can try DP for total reduction d for all monsters:
        #
        # For all-target spells, max damage sum relevant is max HP among monsters,
        # because no need to reduce HP more than max(HP) by all-target, leftover can be finished by single-target.
        #
        # So we build a DP for minimal MP spent for each possible 'all-target damage' from 0 up to max_HP,
        # where 'all-target damage' is total damage applied to each monster by all-target spells.
        #
        # After considering all-target damage d, leftover HP of each monster is max(0, HP_i - d).
        #
        # Then for each monster with leftover HP, we add minimal MP to kill it using single-target spells alone.
        #
        # Finally, we take minimal value over 'all-target damage' of:
        #   DP[all-target damage] + sum over monsters of minimal MP to kill leftover HP with single-target spells.
        #
        # Implementation details:
        #
        # 1) Precompute min MP to kill HP h (0 <= h <= max_HP) for single-target spells.
        # Use DP for single-target spells only:
        # For h from 0 to max_HP:
        #    dp_single[h] = minimal MP to deal h damage with single-target spells (unbounded knapsack).
        # For h=0, dp_single[0] = 0.
        # Then can compute up to max_HP.
        #
        # 2) For all-target spells,
        #    We build dp_all[d] = minimal MP to do all-target damage d (unbounded knapsack).
        # For d from 0 to max_HP.
        #
        # 3) For each possible all-target damage d, compute total MP = dp_all[d] + sum over i dp_single[max(0, HP_i - d)].
        # Take the minimum.
        #
        # Note:
        # max_HP = max(HPs)
        # max_HP up to 100000, so DP arrays with 100000 size each.
        #
        # But this is a bit large for runtime and memory.
        #
        # Optimization possible:
        #
        # a) We only need dp_single for damage up to max_HP.
        # b) For dp_all also the same range.
        #
        # c) Use integer arrays and avoid slow methods.
        #
        # Implementation follows.

        max_HP = max(HPs)

        INF = 10**9

        # Precompute dp_single: minimal MP cost to do exactly h damage via single-target spells (unbounded knapsack)
        # or more damage (to kill monster).
        # Because spells do fixed damage, we want minimal MP to deal at least h damage.
        # But monsters are defeated when HP <=0, so we need at least HP damage.
        #
        # So dp_single[h] = minimal MP cost to deal exactly h damage (or we can try dp for at least h damage).
        # We'll compute minimal MP cost to deal exactly h damage, then for at least h we use min prefix.
        #
        # Because damage_j can be 0, skip zero damage spells for single-target in dp.
        single_spells = [(MP, Damage) for (_, MP, Target, Damage) in spells if Target == "Single" and Damage > 0]

        dp_single = [INF] * (max_HP + 1)
        dp_single[0] = 0

        for MP, Damage in single_spells:
            for damage in range(Damage, max_HP +1):
                if dp_single[damage - Damage] + MP < dp_single[damage]:
                    dp_single[damage] = dp_single[damage - Damage] + MP
        # Compute minimal cost for at least h damage:
        for h in range(max_HP - 1, -1, -1):
            if dp_single[h+1] < dp_single[h]:
                dp_single[h] = dp_single[h+1]

        # Precompute dp_all: minimal MP cost to deal exactly d damage to all monsters (unbounded knapsack)
        # with all-target spells.
        all_spells = [(MP, Damage) for (_, MP, Target, Damage) in spells if Target == "All" and Damage > 0]

        # If no all-target spells, dp_all[d] = INF for d>0, dp_all[0]=0
        dp_all = [INF] * (max_HP + 1)
        dp_all[0] = 0

        for MP, Damage in all_spells:
            for damage in range(Damage, max_HP +1):
                if dp_all[damage - Damage] + MP < dp_all[damage]:
                    dp_all[damage] = dp_all[damage - Damage] + MP
        # For at least d damage:
        for d in range(max_HP -1, -1, -1):
            if dp_all[d+1] < dp_all[d]:
                dp_all[d] = dp_all[d+1]

        # Now try all possible all-target damage values from 0 to max_HP
        # Calculate total cost = dp_all[d] + sum over monsters dp_single[max(0, HP_i - d)]
        ans = INF
        for d in range(max_HP + 1):
            cost_all = dp_all[d]
            if cost_all == INF:
                continue
            cost_single = 0
            for hp in HPs:
                leftover = hp - d
                if leftover > 0:
                    c = dp_single[leftover]
                    if c == INF:
                        cost_single = INF
                        break
                    cost_single += c
            total_cost = cost_all + cost_single
            if total_cost < ans:
                ans = total_cost

        print(ans)

if __name__ == "__main__":
    solve()