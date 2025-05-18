# A
li = list(input().split())
map_ = {'A':10 , 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
intli = [map_[i] for i in li]

if intli[0]<intli[1]:
    print('<')
elif intli[0]>intli[1]:
    print('>')
else:
    print('=')