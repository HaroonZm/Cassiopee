T = input()
def f(s):
    total = 0
    idx = 0
    while idx < len(s):
        total += int(s[idx])
        idx += 1
    return total
print(f(T))