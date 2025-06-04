from sys import exit as bye
H,W=[*map(int,input().split())]
def o(x):print(x)
if 1 in (H,W):
 o(1);bye()
X=(H//2)*W
if H&1:
 if W&1:X+=W//2+1
 else:X+=W/2
o(int(X))