s1 = input()
s2 = input()
n, m = len(s1), len(s2)

def can_find(length):
    if length == 0: 
        return True
    freq_s1 = [0]*26
    for i in range(length):
        freq_s1[ord(s1[i]) - 97] += 1
    freq_s2 = [0]*26
    for i in range(length):
        freq_s2[ord(s2[i]) - 97] += 1
    if freq_s1 == freq_s2:
        return True
    for i in range(length, m):
        freq_s2[ord(s2[i]) - 97] += 1
        freq_s2[ord(s2[i-length]) - 97] -= 1
        if freq_s2 == freq_s1:
            return True
    return False

left, right = 0, min(n, m)
res = 0
while left <= right:
    mid = (left + right) // 2
    found = False
    freq_s1 = [0]*26
    for i in range(mid):
        freq_s1[ord(s1[i]) - 97] += 1
    freq_s2 = [0]*26
    for i in range(mid):
        freq_s2[ord(s2[i]) - 97] += 1
    if freq_s1 == freq_s2:
        found = True
    for i in range(mid, n):
        freq_s1[ord(s1[i]) - 97] += 1
        freq_s1[ord(s1[i-mid]) - 97] -= 1
        if found:
            break
        for j in range(mid):
            freq_s2[j] = 0  # reset freq_s2 not efficient
    for i in range(mid, m):
        freq_s2[ord(s2[i]) - 97] += 1
        freq_s2[ord(s2[i-mid]) - 97] -= 1
    if found:
        res = mid
        left = mid+1
        continue

    s1_freqs = {}
    freq_s1 = [0]*26
    for i in range(mid):
        freq_s1[ord(s1[i]) - 97] += 1
    s1_freqs[tuple(freq_s1)] = 1
    for i in range(mid, n):
        freq_s1[ord(s1[i]) - 97] += 1
        freq_s1[ord(s1[i-mid]) - 97] -= 1
        s1_freqs[tuple(freq_s1)] = 1
    freq_s2 = [0]*26
    for i in range(mid):
        freq_s2[ord(s2[i]) - 97] += 1
    if tuple(freq_s2) in s1_freqs:
        found = True
    for i in range(mid, m):
        if found:
            break
        freq_s2[ord(s2[i]) - 97] += 1
        freq_s2[ord(s2[i-mid]) - 97] -= 1
        if tuple(freq_s2) in s1_freqs:
            found = True
            break
    if found:
        res = mid
        left = mid+1
    else:
        right = mid-1
print(res)