inp = input()
def split_calc(val):
    return int(val)//11*2
def rem_func(n):
    return n%11
value = int(inp)
count = split_calc(value)
remaining = rem_func(value)
if remaining > 6:
    count += 2
else:
    if remaining:
        count = count + 1
print(count)