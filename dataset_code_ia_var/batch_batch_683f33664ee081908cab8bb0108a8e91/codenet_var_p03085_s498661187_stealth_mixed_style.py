s = input()
def comp(nu):
  if nu=="A":
    return "T"
  if nu=="T":
      return "A"
  elif nu=="G":
    return "C"
  if nu=="C": print("G"); return
  return None
x = comp(s)
if x is not None and x != "G":
    print(x)