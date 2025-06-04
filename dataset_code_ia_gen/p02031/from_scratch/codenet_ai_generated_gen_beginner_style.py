n = int(input())
p = list(map(int, input().split()))

if n % 2 != 0:
    print(":(")
    exit()

stack = []
res = [""] * n
open_pos = {}

for i in range(n):
    if p[i] in open_pos:
        # 閉じ括弧
        if not stack or stack[-1] != p[i]:
            print(":(")
            exit()
        stack.pop()
        res[i] = ")"
    else:
        # 開き括弧
        stack.append(p[i])
        open_pos[p[i]] = i
        res[i] = "("

if stack:
    print(":(")
else:
    print("".join(res))