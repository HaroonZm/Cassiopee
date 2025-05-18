s = input()
mod = 10**9 + 7
abc = 0
bc = 0
c = 0
q = 0
for i in s[::-1]:
  if i == "A":
    abc = (abc + bc) % mod
  if i == "B":
    bc = (bc + c) % mod
  if i == "C":
    c = (pow(3,q,mod) + c) % mod
  if i == "?":
    abc = (abc*3 + bc) % mod
    bc = (bc*3 + c) % mod 
    c = (pow(3,q,mod) + c*3) % mod
    q += 1
print(int(abc))