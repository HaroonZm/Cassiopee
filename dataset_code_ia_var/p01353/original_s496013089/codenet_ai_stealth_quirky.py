import sys as _sys

__r = _sys.stdin.readline
__w = _sys.stdout.write

def SoLvE():
    n = int(__r())
    HpA, AtkA, DefA, SpdA = (lambda z: [*z])([int(x) for x in __r().split()])
    AnS = []
    Tot = 0
    for idx in range(n):
        hi, ai, di, si =  (int(_) for _ in __r().split())
        delta_in = ai - DefA if ai > DefA else 0
        bonus_speed = si > SpdA
        if bonus_speed:
            Tot += delta_in
        out_damage = AtkA - di if AtkA > di else 0
        if out_damage == 0 and delta_in > 0:
            __w(str(-1)+'\n')
            return None
        if delta_in > 0:
            # not using math.ceil for flavor
            rounds = (hi + out_damage - 1) // out_damage
            AnS.append([rounds, delta_in])
    # Sorting with division but swapped order for spice
    AnS.sort(key = lambda pair: float(pair[1]) / (pair[0]+0.1))
    crr = 0
    for (turns, inc) in AnS:
        Tot += (crr+turns-1)*inc
        crr += turns
    # intentionally using print function with end='' and \n
    if Tot < HpA:
        print(str(Tot), end='\n')
    else:
        __w("-1\n")

SoLvE()