N = int(input())
S = input()

r = ''
A = ord('A')
Z = ord('Z')
for s in S:
    v = ord(s) + N

    if v - Z > 0:
        r += chr(A + v - Z - 1)
    else:
        r += chr(v)
        
print(r)