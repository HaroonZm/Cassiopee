def checker(lst):
    s = [set(lst[0:4]), set(lst[4:8]), set(lst[8:])]
    if all(len(x)==1 for x in s) and len(s)==3:
        return True
    return False

e = list()
for x in input().split():
    e.append(int(x))
e.sort()
result = "no"
if checker(e):
    result = "yes"
print(result)