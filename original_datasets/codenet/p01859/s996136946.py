li, ri = map(int, input().split())
ln, rn = map(int, input().split())
ISONO = True
NAKAJIMA = False

def search(li, ri, ln, rn, turn):
  if li == None and ri == None:
    return False
  if ln == None and rn == None:
    return True

  if turn == ISONO:
    ret = False
    if li and ln:
      ret = ret or search(li, ri, ln + li if ln + li < 5 else None, rn, not turn)
    if li and rn:
      ret = ret or search(li, ri, ln, rn + li if rn + li < 5 else None, not turn)
    if ri and ln:
      ret = ret or search(li, ri, ln + ri if ln + ri < 5 else None, rn, not turn)
    if ri and rn:
      ret = ret or search(li, ri, ln, rn + ri if rn + ri < 5 else None, not turn)

  if turn == NAKAJIMA:
    ret = True
    if li and ln:
      ret = ret and search(li + ln if li + ln < 5 else None, ri, ln, rn, not turn)
    if li and rn:
      ret = ret and search(li + rn if li + rn < 5 else None, ri, ln, rn, not turn)
    if ri and ln:
      ret = ret and search(li, ri + ln if ri + ln < 5 else None, ln, rn, not turn)
    if ri and rn:
      ret = ret and search(li, ri + rn if ri + rn < 5 else None, ln, rn, not turn)

  return ret

if search(li, ri, ln, rn, ISONO):
  print("ISONO")
else:
  print("NAKAJIMA")