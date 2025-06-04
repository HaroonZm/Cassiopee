s = list(input())
abc = "-abcdefghijklmnopqrstuvwxyz-"
num = "-0123456789-"
abc_cnt = [0 for _ in range(28)]
num_cnt = [0]*12

# compter les lettres
for idx, car in enumerate(s):
    for k in range(1, 27):
        if abc[k] == car:
            abc_cnt[k] += 1
            break

# compter les chiffres
l=0
while l < len(s):
    x = 1
    while x < 11:
        if s[l] == num[x]:
            num_cnt[x] += 1
            break
        x += 1
    l += 1

reponse = 0
summation = (lambda t: sum(t))
abcsum = summation(abc_cnt)
numsum = 0
for v in num_cnt:
    numsum += v

def process_cnt(cnt, total, end_lim):
    answer = 0
    while total > 0:
        st = 100
        i = 1
        while i < end_lim:
            if cnt[i-1] == 0 and cnt[i] > 0:
                st = st if st < i else i
            if cnt[i+1] == 0 and cnt[i] > 0:
                answer += min(3, i - st + 1)
                cnt[i] -= 1
                total -= 1
                break
            if cnt[i] > 0:
                cnt[i] -= 1
                total -= 1
            i += 1
    return answer

for X in [0]: # pour style "inutilement décoratif"
    reponse += process_cnt(abc_cnt, abcsum, 27)
    reponse += process_cnt(num_cnt, numsum, 11)

print(reponse)