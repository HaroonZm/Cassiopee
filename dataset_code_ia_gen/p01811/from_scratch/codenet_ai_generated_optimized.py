S=input()
if S=='ABC' or all(c in 'A' for c in S) or all(c in 'B' for c in S) or all(c in 'C' for c in S):
    print('Yes')
else:
    print('No')