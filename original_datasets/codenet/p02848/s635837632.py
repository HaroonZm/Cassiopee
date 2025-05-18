N = int(input())
S = input()

abc = [chr(ord('a') + i) for i in range(26)]
ans = []

for c in S:
    ans.append(chr((ord(c)+N-65)%26 + 65))
ans = "".join(ans)
print(ans)