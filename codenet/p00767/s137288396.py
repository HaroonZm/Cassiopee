def compare(h,w):
    hw=h**2+w**2

    tmp_h=150
    tmp_w=150
    tmp_hw=150**2+150**2

    for j in range(1,150):
        for i in range(1,j):
            ij=i**2+j**2
            if (hw < ij) or (hw == ij and h < i) : # ??\????????\???
                #print ("1",h,w,hw,i,j,ij,tmp_h,tmp_w,tmp_hw)
                if  (tmp_hw > ij) or (tmp_hw == ij and tmp_h > i):
                    #print ("2",h,w,hw,i,j,ij,tmp_h,tmp_w,tmp_hw)
                    tmp_h=i
                    tmp_w=j
                    tmp_hw=ij

    print(tmp_h,tmp_w)

import sys

for line in sys.stdin:
    h,w=map(int,line.split())
    if h!=0 and w!=0:
        compare(h,w)