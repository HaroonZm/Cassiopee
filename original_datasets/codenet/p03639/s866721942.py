N = int(input())
a = list(map(int, input().split()))

mod_4 = 0
mod_2 = 0
for a_i in a:
    if a_i % 4 == 0:
        mod_4 += 1
    elif a_i % 2 == 0:
        mod_2 += 1

if mod_2 == 0:
    m = 2 * mod_4 + 1
else:
    m = 2 * mod_4 + mod_2

if m >= N:
    print('Yes')
else:
    print('No')