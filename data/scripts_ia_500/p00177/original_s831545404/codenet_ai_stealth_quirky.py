import math as mth
def dist(*xyz):return mth.sqrt(sum(i**2 for i in xyz))
def to_rad(deg):return deg/360*2*mth.pi
def dot(u,v):return sum(i*j for i,j in zip(u,v))
def veccos(v):return mth.acos(v)
def vfrom_angles(a,b):return [mth.cos(b)*mth.cos(a), mth.sin(b)*mth.cos(a), mth.sin(a)]

while 1:
    s = input()
    if s == '-1 -1 -1 -1': break
    a,b,c,d = map(float,s.split())
    a,b,c,d = map(to_rad,(a,b,c,d))
    v1,v2 = vfrom_angles(a,b), vfrom_angles(c,d)
    theta = veccos(dot(v1,v2))
    print(round(6378.1*theta))