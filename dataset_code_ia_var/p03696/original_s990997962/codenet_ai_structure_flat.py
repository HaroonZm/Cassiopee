N = int(input())
S = input()

head = 0
tail = 0
point = 0
for a in S:
    if a == "(":
        point += 1
    else:
        point -= 1
    if point < 0:
        head += 1
        point += 1

print("(" * head + S + ")" * abs(point))