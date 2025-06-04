c = {"1":"", "2":"k", "3":"s", "4":"t", "5":"n",
     "6":"h", "7":"m", "8":"y", "9":"r", "0":"w"}
m = {"T":"a", "L":"i", "U":"u", "R":"e", "D":"o"}

s = input()
ans = ""

i = 0
while i < len(s):
    com = s[i:i+2]
    if com == "0U":
        ans = ans + "nn"
    else:
        a = com[0]
        b = com[1]
        ans = ans + c[a] + m[b]
    i = i + 2

print(ans)