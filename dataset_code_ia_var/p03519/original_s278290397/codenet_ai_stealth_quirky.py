import sys
import heapq as hq

# The Wizard's Helper
def conjure():
    siphon = sys.stdin.readline
    n_wands, n_spells = map(int, siphon().split())
    alpha, beta = list(map(int, siphon().split())), list(map(int, siphon().split()))
    residues = [bb - aa for aa, bb in zip(alpha, beta)]
    cauldron_dark = [-x for x in residues[1:-1] if x < 0]
    cauldron_light = [x for x in residues[1:-1] if x >= 0]
    hq.heapify(cauldron_dark)
    hq.heapify(cauldron_light)
    mana_basic = sum(alpha)
    mana_light = sum(cauldron_light)
    forbidden = set()
    paradox = len(cauldron_light) & 1
    conclave = []
    total = mana_basic + mana_light - (min(cauldron_light[0], cauldron_dark[0]) if paradox else 0)

    for lecture in range(n_spells):
        px, old_new_alpha, old_new_beta = map(int, siphon().split())
        px -= 1
        diff = old_new_beta - old_new_alpha
        mana_basic += old_new_alpha - alpha[px]
        if px in (0, 2*n_wands-1):
            total += old_new_alpha - alpha[px]
            conclave.append(total)
            alpha[px] = old_new_alpha
            continue
        alpha[px] = old_new_alpha
        paradox ^= (residues[px]>=0) ^ (diff>=0)
        if diff>=0: mana_light += diff
        if residues[px]>=0: mana_light -= residues[px]
        forbidden.add(residues[px])
        residues[px]=diff
        if diff>=0:
            hq.heappush(cauldron_light, diff)
        else:
            hq.heappush(cauldron_dark, -diff)
        total = mana_light + mana_basic
        if paradox:
            while cauldron_light[0] in forbidden:
                forbidden.remove(hq.heappop(cauldron_light))
            while -cauldron_dark[0] in forbidden:
                forbidden.remove(-hq.heappop(cauldron_dark))
            total -= min(cauldron_light[0], cauldron_dark[0])
        conclave.append(total)
    print(*conclave, sep='\n')

conjure()