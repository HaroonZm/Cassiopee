t = input()
b = input()

table = [[0 for i in range(len(t))] for j in range(len(b))]

if len(t) > len(b):

    if t[0] == b[0]:
        table[0][0] = 1
    
    for i in range(1, len(t)):
        if t[i] == b[0]:
            table[0][i] = table[0][i-1] + 1
        else:
            table[0][i] = table[0][i-1]
    
    
    for i in range(1, len(b)):
        
        if b[i] == t[i]:
            table[i][i] = table[i-1][i-1]

        for j in range(i+1, len(t)):
            if b[i] == t[j]:
                table[i][j] = table[i-1][j-1] + table[i][j-1]
            else:
                table[i][j] = table[i][j-1]

    print(table[len(b)-1][len(t)-1] % 1000000007)

elif len(t) == len(b):
    if t == b:
        print(1)
    else:
        print(0)
        
else:
    print(0)