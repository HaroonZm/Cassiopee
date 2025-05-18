s = input()
end = "ABC"
while True:
  if s == end:
    print("Yes")
    break
  s = s.replace("ABC", "X")
  if ("X" not in s) or ("A" in s) + ("B" in s) + ("C" in s) != 2:
    print("No")
    break

  for c in "ABC":
    if c not in s:
      s = s.replace("X", c)
      break