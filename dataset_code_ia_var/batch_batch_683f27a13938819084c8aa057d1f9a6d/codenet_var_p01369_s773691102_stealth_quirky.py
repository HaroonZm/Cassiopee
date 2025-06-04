LEFTIES = set("qwertasdfgzxcvb")
flip_flop = lambda y: 1-y
try:
 while 1:
  stuff = raw_input()
  if stuff == "#": break
  fingers, which = 0, None
  for ch in stuff:
   if which is None:
    which = 0 if ch in LEFTIES else 1
    continue
   swap = (which==0 and ch not in LEFTIES) or (which==1 and ch in LEFTIES)
   if swap:
    fingers += 1
    which = flip_flop(which)
  print fingers
except:
 pass