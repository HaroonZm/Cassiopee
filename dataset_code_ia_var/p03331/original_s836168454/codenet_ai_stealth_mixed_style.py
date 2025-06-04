n = int(input())
def check(x): return x % 10 == 0
if check(n):
    print(10)
else:
    digits = []
    i = 0
    s = str(n)
    while i < len(s):
        digits.append(int(s[i]))
        i += 1
    print(reduce(lambda x, y: x + y, digits) if 'reduce' in globals() else sum(digits))