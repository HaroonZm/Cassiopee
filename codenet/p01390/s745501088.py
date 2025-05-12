dic = {}
for num1 in range(ord("a"), ord("z") + 1):
  c1 = chr(num1)
  dic[c1] = []
  for num2 in range(ord("a"), ord("z") + 1):
    c2 = chr(num2)
    for num3 in range(ord("a"), ord("z") + 1):
      c3 = chr(num3)
      dic[c1].append(c1 + c2 + c3 + "a")

print("?" + dic["a"].pop())
used = set()
while True:
  s = input()
  if s in used or s[0] != "a":
    print("!OUT")
    break
  used.add(s)
  print("?" + dic[s[-1]].pop())