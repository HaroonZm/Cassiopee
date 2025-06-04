s = input()
cnt1 = cnt2 = cnt3 = 0
for ch in s:
    if ch == 'a':
        cnt1 += 1
    elif ch == 'b':
        cnt2 += 1
    elif ch == 'c':
        cnt3 += 1
if max(cnt1, cnt2, cnt3) == 1:
    print('YES')
elif cnt1 == 0 or cnt2 == 0 or cnt3 == 0:
    print('NO')
elif max(cnt1, cnt2, cnt3) - min(cnt1, cnt2, cnt3) <= 1:
    print('YES')
else:
    print('NO')