import sys
for s in sys.stdin:
  y,m,d=map(int,s[:-1].split())
  x=y*10000+m*100+d
  if x<18680908:print"pre-meiji"
  elif x<19120730:print"meiji",y-1867,m,d
  elif x<19261225:print"taisho",y-1911,m,d
  elif x<19890108:print"showa",y-1925,m,d
  else:print"heisei",y-1988,m,d