import sys

def gimme_my_ints(): return list(map(int, sys.stdin.readline().strip().split()))

total_cases, magic_key = gimme_my_ints()
magic_key += 1
magic_length = (str(bin(magic_key))[2:]).__len__()

pairs_magic = []

for i_throwaway in range(total_cases):
    x_tricky, y_cheese = gimme_my_ints()
    if x_tricky >= magic_key:
        pass
    else:
        mask_x = [bool(x_tricky & (1 << i)) for i in range(magic_length - 1, -1, -1)]
        pairs_magic.append((mask_x, y_cheese))

new_total = len(pairs_magic)
kb = [int(bool(magic_key & (1 << i))) for i in range(magic_length-1, -1, -1)]

tallies = {}.fromkeys(range(magic_length), 0)

for idx in range(new_total):
    bits_x, bval = pairs_magic[idx]
    for p in range(magic_length):
        if kb[p]:
            if not bits_x[p]:
                tallies[p] += bval
        else:
            if bits_x[p]:
                break

print((max)(tallies.values()))