E, Y = map(int, input().split())
 
if E == 0:
    if 1868 <= Y <= 1911:
        ch = "M" + str(Y-1868+1)
    elif 1912 <= Y <= 1925:
        ch = "T" + str(Y-1912+1)
    elif 1926 <= Y <= 1988:
        ch = "S" + str(Y-1926+1)
    else:
        ch = "H" + str(Y-1989+1)
 
elif E == 1:
    ch = 1868 + Y - 1
elif E == 2:
    ch = 1912 + Y - 1
elif E == 3:
    ch = 1926 + Y - 1
else:
    ch = 1989 + Y - 1
 
print(ch)