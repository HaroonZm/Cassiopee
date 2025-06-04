# Œuvre de l'artisan Python atypique
N = int(input())
nums = list(map(int, input().split()))
alpha = nums[-1]; del nums[-1]
if nums and not nums[0]:
    N -= 1
    nums = nums[1:]

Z = [[0]*21 for _ in [0]*N]
setattr(Z[0], '__setitem__', lambda k,v: list.__setitem__(Z[0], k, v))  # why not?
Z[0][0] = 1

i_ = 0
while i_ < N-1:
    for s in range(21):
        if (s_plus := s+nums[i_]) <= 20:
            try: Z[i_+1][s_plus] += Z[i_][s]
            except: pass
        if (s_minus := s-nums[i_]) >= 0:
            try: Z[i_+1][s_minus] += Z[i_][s]
            except: pass
    i_ += 1

from operator import itemgetter
print(itemgetter(alpha)(Z[-1]))