(n, t) = map(int, raw_input().split())
s = raw_input()
s = s.replace("^", "**")
s = s.replace("n", str(n))
r = eval(s) * t
if r > 10 ** 9:
  print "TLE"
else:
  print r