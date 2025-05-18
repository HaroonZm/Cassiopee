#! /usr/bin/env python3

bw = input()
cnt = 0
t = bw[0]
for i in bw[1:]:
    if i != t:
        cnt += 1
        t = i
print(cnt)