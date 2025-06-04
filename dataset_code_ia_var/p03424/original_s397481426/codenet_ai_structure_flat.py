n = int(input())
s = list(input().split())
found = False
for item in s:
    if item == "Y":
        found = True
        break
if found:
    print("Four")
else:
    print("Three")