ans_list = []
while True:
    s = input()
    if s == ".":
        break
    q_list = ["" for i in range(len(s))]
    now = -1
    ans = "yes"
    for i in list(s):
        if i == "(" or i == "[":
            now += 1
            q_list[now] = i
        elif i == ")":
            if now == -1:
                ans = "no"
            elif q_list[now] == "(":
                now -= 1
            else:
                ans = "no"
        elif i == "]":
            if now == -1:
                ans = "no"
            elif q_list[now] == "[":
                now -= 1
            else:
                ans = "no"
        if ans == "no":
            break
    if now >= 0:
        ans = "no"
    ans_list.append(ans)

for i in ans_list:
    print(i)