import sys
import math

def solve():
    input = sys.stdin.readline
    while True:
        N = int(input())
        if N == 0:
            break
        HP = list(map(int, input().split()))
        M = int(input())
        spells = []
        for _ in range(M):
            parts = input().split()
            name = parts[0]
            MP = int(parts[1])
            target = parts[2]
            dmg = int(parts[3])
            spells.append((MP, target, dmg))

        # We want minimal magic power used
        # Two types of spells:
        # - Single target: damage applies to one monster
        # - All target: damage applies to all monsters simultaneously

        # Approach:
        # Use binary search on total magic power cost to find minimal cost to kill all monsters
        # For a given magic power limit, check if it's possible to kill all monsters

        # But since spell consumption is small (max MP<=99), and monsters HP upto 1e5, DP on states is impossible.

        # Alternative approach:
        # For each monster, compute the minimal MP needed to kill it with single-target spells only
        # For all-target spells, their effect is global, we can apply them multiple times and sum cost

        # Let's define:
        # - best_single_mp[i]: minimal MP to kill monster i using only single-target spells
        # - We'll try all combinations of number of times to cast each 'All' spell (can be from 0 to max times)
        # For each combination of "All" spells usage, monsters HP get reduced accordingly
        # Remaining HP to kill (all monsters that survive) must be killed by single target spells.

        # Since number of 'All' spells M ≤ 100, but their usage count can be large, we cannot try all

        # Another idea:
        # Use formula and optimization:
        # Since 'All' spells impact all monsters, we can try to combine them in any way:
        # The damage of "All" spells sum up linearly, cost sums up linearly.
        # So, we want to find the minimal total MP for sum of "All" spells usages to reduce all monsters HP as much as possible.

        # Let's try with the linear programming approach simplified:
        # We only need to find min sum of (all_spells_usage_j * MP_j) such that for each monster:
        # HP[i] - sum(all_spells_usage_j * damage_j) ≤ 0 or ≤ residual to be killed by single-target spells with cost best_single_mp[i]
        # So, after applying all-spells usages, residual HP[i]_left = max(0, HP[i] - sum_all_spells_damage)
        # Then sum over i best_single_mp[i] to kill remains
        # The total cost = sum_all_spells_usages_MP + sum residual single-target cost

        # Thus, try all combinations of "all" spells usages? impossible

        # Because all spells are integer cost and damage, and all spells usage counts must be integers,
        # and damages and costs arbitrary.

        # We'll use a knapsack-like approach for all-spells:
        # Since MP_j ≤99, max damage can be high (up to 999999).
        # But number of monsters ≤100 and their HP ≤100000.

        # Let's consider only the "All" spells, we'll try all possible sums of damage and corresponding minimal MP cost.

        # For each possible total damage D (applied to all monsters), minimal cost is computed.

        # Then for given D, the residual HP[i] are HP[i]-D (min 0), sum single cost accordingly.
        # We take minimal MP cost over all possible D.

        # To limit the search space, we note the maximum HP maxHP = max(HP)
        maxHP = max(HP)
        all_spells = [s for s in spells if s[1] == "All" and s[2] > 0]
        single_spells = [s for s in spells if s[1] == "Single" and s[2] > 0]

        # Precompute best_single_mp[i]: minimal MP to kill monster i with single spells
        INF = 10**15
        best_single_mp = [INF]*N
        for mp, _, dmg in single_spells:
            for i, hp in enumerate(HP):
                # Number of hits needed is ceil(hp/dmg)
                hits = (hp + dmg -1)//dmg
                cost = hits * mp
                if cost < best_single_mp[i]:
                    best_single_mp[i] = cost

        # If no single spells, best_single_mp might remain INF, but problem states at least one spell >0 damage.
        # So single spells may all be "All" spells only, need to check.

        # If no single spells, best_single_mp[i] = INF, then all monsters must be killed by All spells only.

        if not all_spells:
            # Only single spells: sum best_single_mp[i]
            # but if some best_single_mp[i] is INF, print INF?
            # Problem guaranteed at least one spell with damage >0, so pass
            print(sum(best_single_mp))
            continue

        # DP for all_spells:
        # We want minimal cost to get total damage D (applied to all monsters)
        # D can go max to maxHP (no need above maxHP)
        dp = [INF]*(maxHP+1)
        dp[0] = 0
        for mp, _, dmg in all_spells:
            for d in range(dmg, maxHP+1):
                if dp[d - dmg] + mp < dp[d]:
                    dp[d] = dp[d - dmg] + mp
            # Because multiple usage allowed, unbounded knapsack
            # Do unbounded knapsack:
            # Repeat enough times:
            # We'll implement optimized unbounded knapsack
            # Actually above is 0/1 knapsack, need unbounded:
            # So unbounded knapsack: for d in [dmg..maxHP]: dp[d] = min(dp[d], dp[d - dmg] + mp)
            for d in range(dmg, maxHP+1):
                if dp[d - dmg] + mp < dp[d]:
                    dp[d] = dp[d - dmg] + mp

        # However, above code runs dp update twice (waste), fix to one:
        # Let's redo dp:
        dp = [INF]*(maxHP+1)
        dp[0] = 0
        for mp, _, dmg in all_spells:
            for d in range(dmg, maxHP+1):
                if dp[d - dmg] + mp < dp[d]:
                    dp[d] = dp[d - dmg] + mp
            # But this is 0/1 knapsack, we need unbounded knapsack correctly:
            # For unbounded knapsack:
            # For each spell
            # for d in range(dmg,maxHP+1):
            #      dp[d] = min(dp[d], dp[d-dmg] + mp)
            # We must do for d in dmg..maxHP for each spell:
        # Re-implement unbounded knapsack properly:
        dp = [INF]*(maxHP+1)
        dp[0] = 0
        for mp, _, dmg in all_spells:
            for d in range(dmg, maxHP+1):
                if dp[d-dmg] + mp < dp[d]:
                    dp[d] = dp[d-dmg] + mp
            # We need multiple passes because of dp dependencies:
            # For unbounded knapsack, process from dmg to maxHP, single pass is enough:
            # But spells can be used unlimited times

        # Because we modified dp on the fly, need to do repeated until no changes? 
        # Normally unbounded knapsack single pass suffices if we process d from dmg to maxHP:
        # Let's do as usual:
        for mp, _, dmg in all_spells:
            for d in range(dmg, maxHP+1):
                if dp[d-dmg] + mp < dp[d]:
                    dp[d] = dp[d-dmg] + mp

        # Now dp[d] = minimal all-target spells MP cost to do damage d to all monsters

        # For each possible damage d, compute total cost = dp[d] + sum over monsters max(0, best_single_mp after reducing HP by d)

        # For best_single_mp[i], we precompute per monster and damage d, the minimal cost to kill residual HP: HP[i]-d
        # Because single spells usage count can vary, and best_single_mp[i] was precomputed for HP[i], 
        # but for residual HP[i]-d (could be 0 or less), need to recompute cost.

        # But single spells cost is linear in hits:
        # For each single spell, cost to reduce h HP is ceil(h/dmg) * mp

        # For all monsters, for each d in 0..maxHP:

        # For each monster i, residual = max(0, HP[i] - d)

        # For each monster i, cost to kill residual with single spells is min over all single spells of ceil(residual/dmg)*mp

        # We'll precompute for all monsters, for each residual HP from 0..maxHP, minimal cost

        # First precompute single spell damages and MPs arrays

        single_dmg_mp = [(mp, dmg) for mp, _, dmg in single_spells]
        # For any monster, best cost for HP h is min of ceil(h/dmg)*mp over single spells

        # Precompute for residual HP 0..maxHP for all monsters individually is expensive (N max 100 * maxHP 1e5 = 1e7)

        # Instead, since all monsters have HP ≤ maxHP ≤ 1e5, and number of monsters max 100, in total 1e7 operations may be possible but tight.

        # Alternatively optimize:
        # For each single spell, their cost function is linear and piecewise:

        # ceil(h/dmg)*mp = ((h + dmg -1)//dmg)*mp

        # For residual h, minimal over all spells

        # We'll precompute minimal single_spell cost per HP 0..maxHP once

        min_single_cost_for_HP = [INF]*(maxHP+1)
        for h in range(maxHP+1):
            c = INF
            for mp, dmg in single_dmg_mp:
                hits = (h + dmg -1)//dmg if h > 0 else 0
                cost = hits * mp
                if cost < c:
                    c = cost
            min_single_cost_for_HP[h] = c

        # For each possible d (damage from all spells), total cost = dp[d] + sum over i min_single_cost_for_HP[max(0, HP[i]-d)]

        ans = INF
        for d in range(maxHP+1):
            if dp[d] == INF:
                continue
            total = dp[d]
            for hp in HP:
                residual = hp - d
                if residual < 0:
                    residual = 0
                total += min_single_cost_for_HP[residual]
                if total >= ans:  # early stop
                    break
            if total < ans:
                ans = total
        print(ans)

if __name__ == "__main__":
    solve()