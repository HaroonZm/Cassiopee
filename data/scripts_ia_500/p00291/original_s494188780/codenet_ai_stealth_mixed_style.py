lst = []
for i in input().split():
    lst.append(int(i))

total = sum([lst[0], lst[1]*5, lst[2]*10, lst[3]*50, lst[4]*100, lst[5]*500])

def check_amount(value):
    return 1 if value >= 1000 else 0

print(check_amount(total))