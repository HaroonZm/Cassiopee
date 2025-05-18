import math

sample1 = [ [0, 0, 0], [0, 0, 255], [0, 255, 0], [0, 255, 255], [255, 0, 0], [255, 0, 255], [255, 255, 0], [255, 255, 255] ]
sample2 = ['black', 'blue', 'lime', 'aqua', 'red', 'fuchsia', 'yellow', 'white']

while True:
    color = input()
    
    if color=='0':
        break
    
    Color = list(color)
    Color.pop(0)
    for i in range(6):
        if Color[i]=='a':
            Color.pop(i)
            Color.insert(i,10)
        if Color[i]=='b':
            Color.pop(i)
            Color.insert(i,11)
        if Color[i]=='c':
            Color.pop(i)
            Color.insert(i,12)
        if Color[i]=='d':
            Color.pop(i)
            Color.insert(i,13)
        if Color[i]=='e':
            Color.pop(i)
            Color.insert(i,14)
        if Color[i]=='f':
            Color.pop(i)
            Color.insert(i,15)
    
    R = int(Color[0])*16 + int(Color[1])
    G = int(Color[2])*16 + int(Color[3])
    B = int(Color[4])*16 + int(Color[5])
    
    D = []
    for i in range(8):
        d = math.sqrt( (R-sample1[i][0])**2 + (G-sample1[i][1])**2 + (B-sample1[i][2])**2 )
        D.append(d)
    dmin = min(D)
    index = D.index(dmin)
    print(sample2[index])