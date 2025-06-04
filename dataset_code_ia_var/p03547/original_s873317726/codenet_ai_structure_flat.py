li = list(input().split())
map_ = {'A':10 , 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
intli = []
for i in li:
    intli.append(map_[i])
if intli[0] < intli[1]:
    print('<')
else:
    if intli[0] > intli[1]:
        print('>')
    else:
        print('=')