W,H=map(int,input().split())
M=[list(map(int,input().split())) for _ in range(H)]
def valid_line(line):
    a=set(line[i]^line[i+1] for i in range(len(line)-1))
    return a=={1}
base_row = M[0]
if not valid_line(base_row):
    print("no")
    exit()
for r in M[1:]:
    if not (r == base_row or all((x^y)==1 for x,y in zip(r,base_row))):
        print("no")
        exit()
transposed = list(zip(*M))
base_col = transposed[0]
if not valid_line(base_col):
    print("no")
    exit()
for c in transposed[1:]:
    if not (c == base_col or all((x^y)==1 for x,y in zip(c,base_col))):
        print("no")
        exit()
print("yes")