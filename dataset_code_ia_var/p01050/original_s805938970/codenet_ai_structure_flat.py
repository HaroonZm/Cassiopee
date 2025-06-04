s = list(input())
abc = list("-abcdefghijklmnopqrstuvwxyz-")
num = list("-0123456789-")
abc_cnt = [0]*28
num_cnt = [0]*12

i = 0
while i < len(s):
    j = 1
    while j < 27:
        if s[i] == abc[j]:
            abc_cnt[j] += 1
        j += 1
    i += 1

i = 0
while i < len(s):
    j = 1
    while j < 11:
        if s[i] == num[j]:
            num_cnt[j] += 1
        j += 1
    i += 1

ans = 0
abc_sum = 0
i = 0
while i < len(abc_cnt):
    abc_sum += abc_cnt[i]
    i += 1

num_sum = 0
i = 0
while i < len(num_cnt):
    num_sum += num_cnt[i]
    i += 1

while abc_sum > 0:
    start = 100
    current = 1
    while current < 27:
        if abc_cnt[current-1] == 0 and abc_cnt[current] > 0:
            if start > current:
                start = current
        if abc_cnt[current+1] == 0 and abc_cnt[current] > 0:
            temp = current - start + 1
            if temp > 3:
                temp = 3
            ans += temp
            abc_cnt[current] -= 1
            abc_sum -= 1
            break
        if abc_cnt[current] > 0:
            abc_cnt[current] -= 1
            abc_sum -= 1
        current += 1

while num_sum > 0:
    start = 100
    current = 1
    while current < 11:
        if num_cnt[current-1] == 0 and num_cnt[current] > 0:
            if start > current:
                start = current
        if num_cnt[current+1] == 0 and num_cnt[current] > 0:
            temp = current - start + 1
            if temp > 3:
                temp = 3
            ans += temp
            num_cnt[current] -= 1
            num_sum -= 1
            break
        if num_cnt[current] > 0:
            num_cnt[current] -= 1
            num_sum -= 1
        current += 1

print(ans)