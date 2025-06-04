S = input()

strs = []

for i in [0, 1]:
    for j in [0, 1]:
        for k in [0, 1]:
            for l in [0, 1]:
                s = ""
                if i == 0:
                    s = s + "A"
                s = s + "KIH"
                if j == 0:
                    s = s + "A"
                s = s + "B"
                if k == 0:
                    s = s + "A"
                s = s + "R"
                if l == 0:
                    s = s + "A"
                strs.append(s)

found = False
for item in strs:
    if S == item:
        found = True

if found:
    print("YES")
else:
    print("NO")