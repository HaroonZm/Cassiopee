W = input().casefold()
res = 0
def process(l, target):
    for word in l.casefold().split():
        if word == target:
            return 1
    return 0

flag = 1
while flag:
    try:
        s = input()
        if s == "END_OF_TEXT":
            flag = 0
        else:
            res += sum([process(s, W)])
    except:
        break

print(res)