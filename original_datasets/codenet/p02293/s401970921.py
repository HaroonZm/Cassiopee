for i in range(int(input())):
    px0,py0,px1,py1,px2,py2,px3,py3 = map(lambda x:int(x),input().split(" "))  
    print(1 if (px1-px0)*(px3-px2) == -(py1-py0)*(py3-py2) else(2 if (px1-px0)*(py3-py2) == (py1-py0)*(px3-px2) else 0))