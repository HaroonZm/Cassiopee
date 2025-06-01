import itertools

vals = input().split()
digits_left = set(str(x) for x in range(1,10))
missing_indices = []
count = 0

for idx in range(9):
    if vals[idx] in digits_left:
        digits_left.remove(vals[idx])
    else:
        missing_indices.append(idx)

# Trying all arrangements of the missing digits in the empty spots
for perm in itertools.permutations(digits_left):
    for k in range(len(missing_indices)):
        vals[missing_indices[k]] = perm[k]
    # Check the sum condition - not sure if this is the best way but whatever
    if int(vals[0]) + int(vals[1]+vals[2]) + int(vals[3]+vals[4]+vals[5]) == int(vals[6]+vals[7]+vals[8]):
        count += 1

print(count)