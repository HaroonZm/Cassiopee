N = int(input())
S = input()
ec = S.count('E')
wc = 0
min_val = ec
for k in S:
    if k == 'E':
        ec -= 1
    else:
        wc += 1
    if min_val > ec + wc:
        min_val = ec + wc
print(min_val)