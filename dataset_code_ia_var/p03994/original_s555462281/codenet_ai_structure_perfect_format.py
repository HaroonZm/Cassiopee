s = [(26 - (ord(i) - ord("a"))) % 26 for i in list(input())]
k = int(input())
c = ""
for i in range(len(s) - 1):
    if k >= s[i]:
        k -= s[i]
        c += "a"
    else:
        c += chr((26 - s[i]) % 26 + ord("a"))
print(c + chr(((26 - s[-1]) % 26 + k) % 26 + ord("a")))