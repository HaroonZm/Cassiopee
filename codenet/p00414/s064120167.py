l,n = map(int, input().split())
s = input()
oocnt = 0
for i in range( len(s)-1 ):
    if s[i] == 'o' and s[i+1] == 'o' : oocnt = oocnt + 1
total_oocnt = 0
for i in range( n ):
    total_oocnt = total_oocnt + oocnt
    oocnt = oocnt*2
print( 3*total_oocnt + l)