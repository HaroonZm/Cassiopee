# 2019/08/13

sx,sy,tx,ty=map(int,input().split())

lr=tx-sx
ud=ty-sy

ans=[('R'*lr),
    ('U'*ud),
    ('L'*lr),
    ('D'*ud),
    ('D'),
    ('R'*(lr+1)),
    ('U'*(ud+1)),
    ('L'),
    ('U'),
    ('L'*(lr+1)),
    ('D'*(ud+1)),
    ('R')
    ]
print(''.join(ans))