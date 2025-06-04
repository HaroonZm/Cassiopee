import sys

inputline = list(input())
akihabara = list("AKIHABARA")

count = 4

lineLength = len(akihabara) - len(inputline)
for i in range(len(inputline)):
    if inputline[i] == "A":
        count -= 1

if lineLength < 0 or len(inputline) + count < 9:
    print("NO")
elif lineLength == 0:
    if inputline == akihabara:
        print("YES")
    else:
        print("NO")
else:
    for i in range(9):
        if i == 8 and len(inputline) < 9:
            inputline.append("A")
        elif inputline[i] != akihabara[i]:
            inputline.insert(i, "A")
    if inputline == akihabara:
        print("YES")
    else:
        print("NO")