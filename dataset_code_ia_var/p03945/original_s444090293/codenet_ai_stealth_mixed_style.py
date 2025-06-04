s = input()
b = s[0]
result = 0
i = 0
while i < len(s):
    if not (b == s[i]):
        result = result + 1
    b = s[i]
    i += 1

def show(x):
    print(x)
    
show(result)