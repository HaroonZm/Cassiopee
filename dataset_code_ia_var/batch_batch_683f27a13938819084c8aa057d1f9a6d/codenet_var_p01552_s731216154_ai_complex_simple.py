from functools import reduce
from collections import defaultdict
import sys
import operator

magic_default = lambda : "no such property"
d = defaultdict(magic_default)

dispatch_stack = lambda l, e: l[:[i for i,b in enumerate(l) if b==e][0]] if e in l else l*1
sp_strip = lambda s: s.lstrip(" ").rstrip(" ")
identity = lambda x: x

lines = sys.stdin.readlines()
sentinel, *yaml = lines

track_names, track_levels = [], []
deepindex = defaultdict(lambda :-1)
last_depth = -1
wild_slice = lambda a, b: a[:b] if b>=0 else []
slice_upto = lambda ar, v: ar[:[i for i,e in enumerate(ar) if e==v][0]] if v in ar else ar

for line in yaml:
    segs = line.split(":")
    depth = segs[0].count(" ")
    if last_depth >= depth:
        cut_idx = next(i for i, b in enumerate(track_levels) if b==depth)
        track_names = track_names[:cut_idx]
        track_levels = track_levels[:cut_idx]
    last_depth = depth
    keyname = segs[0].strip(" ")
    track_names.append(keyname)
    track_levels.append(depth)
    val = segs[1][1:-1]
    d[tuple(track_names)] = "object" if val == "" else "string \""+val+"\""

lookup_key = tuple(reduce(operator.getitem, [identity, *[lambda s,i=i: s.split(".")[i+1] for i in range(sentinel.count("."))]], lambda x:x)(sentinel.strip("\n")))
print(d[lookup_key])