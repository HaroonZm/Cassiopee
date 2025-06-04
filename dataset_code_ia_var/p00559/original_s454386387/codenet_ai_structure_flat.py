n, q, s, t = map(int, input().split())
a_lst = [int(input()) for _ in range(n + 1)]
diff = []
i = 0
while i < n:
    diff.append(a_lst[i + 1] - a_lst[i])
    i += 1
temp = 0
for d in diff:
    if d > 0:
        temp += -d * s
    else:
        temp += -d * t
j = 0
while j < q:
    lrt = input().split()
    l = int(lrt[0])
    r = int(lrt[1])
    x = int(lrt[2])
    a = diff[l - 1]
    diff[l - 1] += x
    d_now = diff[l - 1]
    if d_now > 0:
        now_score = -s * d_now
    else:
        now_score = -t * d_now
    if a > 0:
        prev_score = -s * a
    else:
        prev_score = -t * a
    temp += now_score - prev_score
    if r < n:
        b = diff[r]
        diff[r] -= x
        d2_now = diff[r]
        if d2_now > 0:
            now_score2 = -s * d2_now
        else:
            now_score2 = -t * d2_now
        if b > 0:
            prev_score2 = -s * b
        else:
            prev_score2 = -t * b
        temp += now_score2 - prev_score2
    print(temp)
    j += 1