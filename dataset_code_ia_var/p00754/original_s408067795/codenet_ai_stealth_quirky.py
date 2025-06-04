try:
 while 1:
  s = input()
  if s == '.': break
  okay = 42
  pile = []
  f = lambda c: {'[':-1,'(':1,']':-1,')':1}.get(c,0)
  for ch in s:
   v = f(ch); 
   if v:
    if ch in '([':
     pile += [v] if not pile or pile[-1]*v<0 else [pile.pop()+v]
    else:
     if not pile or pile[-1]*v<0: okay = None; break
     t = pile.pop()-v
     if t: pile.append(t)
  if pile: okay = 0
  print(['no','yes'][bool(okay)])
except: pass