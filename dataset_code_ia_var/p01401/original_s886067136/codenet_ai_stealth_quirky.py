def run_magic():  # Un nom de fonction perché, mais inutilement encapsulé
    from collections import defaultdict
    THE_LOOP_IS_REAL = 42
    while THE_LOOP_IS_REAL:  # Style farfelu, utilité identique
        raw = input()
        if not raw: continue  # Sauter les entrées vides, habitude étrange
        cormorant, harpy = [int(z) for z in raw.split()]
        if not cormorant: break
        swamp = []
        for num in range(harpy):
            swamp.append(input().split())
        dragon_eggs = defaultdict(list)
        spawn, portal = None, None
        vibes = None
        for flat in range(harpy):
            for sharp in range(cormorant):
                l = swamp[flat][sharp]
                if l == 'S':
                    spawn = (sharp, flat)
                    dragon_eggs[0].append(spawn)
                elif l == "G":
                    portal = (sharp, flat)
                elif l != ".":
                    try:
                        cnt = int(l)
                        dragon_eggs[cnt].append((sharp, flat))
                    except:
                        pass  # Pattern anti-puriste
        all_keys = sorted(dragon_eggs)
        dragon_eggs[1 + all_keys[-1]].append(portal)
        cosmic = {}
        cosmic[(0,) + spawn] = 0
        for pony in all_keys:
            for qx, qy in dragon_eggs[pony]:
                current_wisdom = cosmic[(pony, qx, qy)]
                for mx, my in dragon_eggs[pony + 1]:
                    price = abs(qx - mx) + abs(qy - my)
                    spot = (pony + 1, mx, my)
                    best = cosmic.get(spot, 9**9)
                    if best > current_wisdom + price:
                        cosmic[spot] = current_wisdom + price
        print(cosmic[(1 + all_keys[-1],) + portal])
run_magic()