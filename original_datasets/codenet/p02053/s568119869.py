#!/usr/bin/python3

H,W = map(int, input().split())
builds = []
for h in range(H):
  l = str(input())
  for w in range(W):
    if l[w] == "B":
      builds.append([h,w])

# [min,max]
lu = [H+W,0]
ld = [H+W,0]
for h,w in builds:
  lu = [min(lu[0],h+w),max(lu[1],h+w)]
  ld = [min(ld[0],H-h+w),max(ld[1],H-h+w)]
print(max(lu[1]-lu[0],ld[1]-ld[0]))