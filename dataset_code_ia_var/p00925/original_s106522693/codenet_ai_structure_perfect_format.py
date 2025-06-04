def left2right(formula):
    ans = int(formula[0])
    for i in range(1, len(formula), 2):
        ans = eval(str(ans) + formula[i:i+2])
    return ans

formula = input()
val = int(input())
if left2right(formula) == val:
    if eval(formula) == val:
        print('U')
    else:
        print('L')
else:
    if eval(formula) == val:
        print('M')
    else:
        print('I')