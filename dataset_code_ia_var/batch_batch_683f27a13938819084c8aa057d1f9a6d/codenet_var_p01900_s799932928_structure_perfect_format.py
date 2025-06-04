n = int(input())
alst = list(map(int, input().split()))
mod_cnt = [0, 0, 0]
for a in alst:
    mod_cnt[a % 3] += 1
if mod_cnt[1] == 0 and mod_cnt[2] == 0:
    print(1)
elif mod_cnt[1] == mod_cnt[2]:
    print(mod_cnt[0] + mod_cnt[1] + mod_cnt[2])
elif mod_cnt[1] < mod_cnt[2]:
    print(mod_cnt[0] + mod_cnt[1] + min(mod_cnt[1] + 3, mod_cnt[2]))
elif mod_cnt[1] > mod_cnt[2]:
    print(mod_cnt[0] + min(mod_cnt[1], mod_cnt[2] + 3) + mod_cnt[2])