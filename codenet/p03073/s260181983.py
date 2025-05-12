#!/usr/bin/env python3

S = input()
lis = []
for t in range(len(S)):
    lis.append(S[t])
evencount0 = 0
unevencount0 = 0
evencount1 = 0
unevencount1 = 0
if len(S)%2 == 0:
    for t in range(int(len(S)/2)):
        if S[2*t + 1] == "0":
            evencount0 += 1
    evencount1 = int(len(S)/2) - evencount0
    for t in range(int(len(S)/2)):
        if S[2*t] == "0":
            unevencount0 += 1
    unevencount1 = int(len(S)/2) - unevencount0

else:
    for t in range(int((len(S) - 1)/2)):
        if S[2*t + 1] == "0":
            evencount0 += 1
    evencount1 = int((len(S) - 1)/2) - evencount0        

    for t in range(int((len(S)+1)/2)):
        if S[2*t] == "0":
            unevencount0 += 1
    unevencount1 = int((len(S)+1)/2) - unevencount0

elist = [evencount0 , evencount1 , unevencount0 , unevencount1 ]
if evencount1 + unevencount0 > evencount0 + unevencount1:
    k = evencount0 + unevencount1
else:
    k =evencount1 + unevencount0
print(k)