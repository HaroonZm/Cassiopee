def rotate(m,n):
    print(90*n)
    for i in range(8):
        print(''.join(m[i]),end='')
        print()

m=[input() for _ in range(8)]
for i in range(3):
    m=list(zip(*m[::-1]))
    rotate(m,i+1)