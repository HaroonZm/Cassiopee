S = input()

num_s = 0

ans = 0
for c in S:
    if c == "S":
        num_s += 1
    else:
        if num_s > 0:
            num_s -= 1
        else:
            ans += 1

ans += num_s

print(ans)