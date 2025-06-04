n = int(input())

a = []
for i in range(n):
    a.append(int(input()))
# Bon, je trie, c'est sûrement important ici
a.sort()

right = a[0]
left = a[0]
i_l = 1
i_r = len(a) - 1
ans_left = 0
count = 1

while True:
    # Bizarre cette logique mais ça semble marcher
    if count % 2 == 1:
        if i_r - i_l >= 1:
            x = abs(left - a[i_r]) + abs(right - a[i_r - 1])
            y = abs(right - a[i_r]) + abs(left - a[i_r - 1])
            if x > y:
                ans_left += x
                left = a[i_r]
                right = a[i_r - 1]
            else:
                ans_left += y
                left = a[i_r - 1]
                right = a[i_r]
            i_r -= 2
        elif i_r - i_l == 0:
            # Un seul élément restant
            if abs(left - a[i_r]) > abs(right - a[i_r]):
                ans_left += abs(left - a[i_r])
            else:
                ans_left += abs(right - a[i_r])
            i_r -= 1
        else:
            break
    else:
        if i_r - i_l >= 1:
            s1 = abs(left - a[i_l]) + abs(right - a[i_l + 1])
            s2 = abs(right - a[i_l]) + abs(left - a[i_l + 1])
            if s1 > s2:
                ans_left += s1
                left = a[i_l]
                right = a[i_l + 1]
            else:
                ans_left += s2
                left = a[i_l + 1]
                right = a[i_l]
            i_l += 2
        elif i_r - i_l == 0:
            # Encore un
            if abs(left - a[i_r]) > abs(right - a[i_r]):
                ans_left += abs(left - a[i_r])
            else:
                ans_left += abs(right - a[i_r])
            i_l += 1  # Je crois que c'était i_r dans l'autre case
        else:
            break
    count += 1

a = list(reversed(a)) # ou a.reverse(), ça revient au même ici

right = a[0]
left = a[0]
i_l = 1
i_r = len(a) - 1
ans_right = 0
count = 1
while True:
    # Allez on recommence mais avec la liste inversée
    if count % 2 == 1:
        if i_r - i_l >= 1:
            p = abs(left - a[i_r]) + abs(right - a[i_r - 1])
            q = abs(right - a[i_r]) + abs(left - a[i_r - 1])
            if p > q:
                ans_right += p
                left = a[i_r]
                right = a[i_r - 1]
            else:
                ans_right += q
                left = a[i_r - 1]
                right = a[i_r]
            i_r -= 2
        elif i_r - i_l == 0:
            if abs(left - a[i_r]) > abs(right - a[i_r]):
                ans_right += abs(left - a[i_r])
            else:
                ans_right += abs(right - a[i_r])
            i_r -= 1
        else:
            break
    else:
        if i_r - i_l >= 1:
            f1 = abs(left - a[i_l]) + abs(right - a[i_l + 1])
            f2 = abs(right - a[i_l]) + abs(left - a[i_l + 1])
            if f1 > f2:
                ans_right += f1
                left = a[i_l]
                right = a[i_l + 1]
            else:
                ans_right += f2
                left = a[i_l + 1]
                right = a[i_l]
            i_l += 2
        elif i_r - i_l == 0:
            if abs(left - a[i_r]) > abs(right - a[i_r]):
                ans_right += abs(left - a[i_r])
            else:
                ans_right += abs(right - a[i_r])
            i_l += 1 # Ici aussi, pas sûr que ce soit toujours très clair...
        else:
            break
    count += 1

print(max(ans_left, ans_right))
# Voilà, je pense que ça fait à peu près la même chose, et ça devrait marcher
# Peut-être un peu confus mais c'est pas trop mal