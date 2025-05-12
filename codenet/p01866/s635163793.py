n = int(input())
x = input()
d = int(input())
swap = {}
for i in range(n):
  if d == 0:break
  if x[i] == "0":
   swap[i] = True
   d -= 1

for i in range(n - 1, -1, -1):
  if d == 0:break
  if x[i] == "1":
    swap[i] = True
    d -= 1
print("".join([x[i] if i not in swap else ("0" if x[i] == "1" else "1") for i in range(n)]))