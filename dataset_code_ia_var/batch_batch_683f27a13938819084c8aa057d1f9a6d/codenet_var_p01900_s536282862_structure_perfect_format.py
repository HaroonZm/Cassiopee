n = input()
An = [int(x) for x in input().split()]
mod0 = 0
mod1 = 0
mod2 = 0
for x in An:
    if x % 3 == 0:
        mod0 += 1
    if x % 3 == 1:
        mod1 += 1
    if x % 3 == 2:
        mod2 += 1
if mod1 == 0 and mod2 == 0:
    print("1")
elif abs(mod1 - mod2) <= 3:
    print(mod0 + mod1 + mod2)
else:
    if mod1 > mod2:
        print(mod0 + mod2 + mod2 + 3)
    if mod1 < mod2:
        print(mod0 + mod1 + mod1 + 3)