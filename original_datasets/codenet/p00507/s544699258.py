import itertools
print(sorted([int(f'{c}{d}')for c,d in itertools.permutations(sorted([int(input())for _ in[0]*int(input())])[:4],2)])[2])