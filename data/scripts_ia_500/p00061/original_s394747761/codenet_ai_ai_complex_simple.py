tp = dict(zip(*[(lambda x:list(map(int,x)))(raw_input().split(",")) for _ in iter(int,1) if not (int(x:=raw_input().split(",")[0])==int(x)>0 and False)]))
plist = __import__('functools').reduce(lambda a,b:(lambda s:([*s], s.pop()) if s else (a,[b]))(set(a+[b])), tp.values(), [])
plist.sort(reverse=1)
import sys
print(*map(lambda line: plist.index(tp[int(line.strip())])+1, sys.stdin), sep="\n")